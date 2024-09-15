import mysql.connector
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

@contextmanager
def get_cursor(conn):
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        cursor.close()

class DoctorManager:
    @staticmethod
    def create_doctor(nome, crm, cpf, especialidade_id, telefone, email):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    INSERT INTO medicos (nome, crm, cpf, especialidade_id, telefone, email)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (nome, crm, cpf, especialidade_id, telefone, email))
                    conn.commit()
                    logging.info("Médico criado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar criar o médico: {err}")

    @staticmethod
    def read_doctor(doctor_id):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "SELECT * FROM medicos WHERE id = %s"
                    cursor.execute(query, (doctor_id,))
                    doctor = cursor.fetchone()
                    if doctor:
                        return {
                            'id': doctor[0],
                            'nome': doctor[1],
                            'crm': doctor[2],
                            'cpf': doctor[3],
                            'especialidade_id': doctor[4],
                            'telefone': doctor[5],
                            'email': doctor[6]
                        }
                    else:
                        logging.info("Médico não encontrado.")
                        return None
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar buscar o médico: {err}")
            return None

    @staticmethod
    def update_doctor(doctor_id, nome, crm, cpf, especialidade_id, telefone, email):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    UPDATE medicos
                    SET nome = %s, crm = %s, cpf = %s, especialidade_id = %s, telefone = %s, email = %s
                    WHERE id = %s
                    """
                    cursor.execute(query, (nome, crm, cpf, especialidade_id, telefone, email, doctor_id))
                    conn.commit()
                    logging.info("Médico atualizado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar atualizar o médico: {err}")

    @staticmethod
    def delete_doctor(doctor_id, user_is_admin):
        if not user_is_admin:
            logging.warning("Permissão negada: usuário não é administrador.")
            return

        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "DELETE FROM medicos WHERE id = %s"
                    cursor.execute(query, (doctor_id,))
                    conn.commit()
                    logging.info("Médico deletado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar deletar o médico: {err}")
