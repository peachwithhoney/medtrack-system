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

class PatientManager:
    @staticmethod
    def create_patient(nome, data_nascimento, cpf, endereco, telefone, email):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    INSERT INTO pacientes (nome, data_nascimento, cpf, endereco, telefone, email)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (nome, data_nascimento, cpf, endereco, telefone, email))
                    conn.commit()
                    logging.info("Paciente criado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar criar o paciente: {err}")

    @staticmethod
    def read_patient(patient_id):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "SELECT * FROM pacientes WHERE id = %s"
                    cursor.execute(query, (patient_id,))
                    patient = cursor.fetchone()
                    if patient:
                        return {
                            'id': patient[0],
                            'nome': patient[1],
                            'data_nascimento': patient[2],
                            'cpf': patient[3],
                            'endereco': patient[4],
                            'telefone': patient[5],
                            'email': patient[6]
                        }
                    else:
                        logging.info("Paciente não encontrado.")
                        return None
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar buscar o paciente: {err}")
            return None

    @staticmethod
    def update_patient(patient_id, nome, data_nascimento, cpf, endereco, telefone, email):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    UPDATE pacientes
                    SET nome = %s, data_nascimento = %s, cpf = %s, endereco = %s, telefone = %s, email = %s
                    WHERE id = %s
                    """
                    cursor.execute(query, (nome, data_nascimento, cpf, endereco, telefone, email, patient_id))
                    conn.commit()
                    logging.info("Paciente atualizado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar atualizar o paciente: {err}")

    @staticmethod
    def delete_patient(patient_id, user_is_admin):
        if not user_is_admin:
            logging.warning("Permissão negada: usuário não é administrador.")
            return

        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "DELETE FROM pacientes WHERE id = %s"
                    cursor.execute(query, (patient_id,))
                    conn.commit()
                    logging.info("Paciente deletado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar deletar o paciente: {err}")
