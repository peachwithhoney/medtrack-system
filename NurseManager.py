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

class NurseManager:
    @staticmethod
    def create_nurse(nome, coren, cpf, especialidade_id, telefone, email):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    INSERT INTO enfermeiros (nome, coren, cpf, especialidade_id, telefone, email)
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                    cursor.execute(query, (nome, coren, cpf, especialidade_id, telefone, email))
                    conn.commit()
                    logging.info("Enfermeiro(a) criado(a) com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar criar o(a) enfermeiro(a): {err}")

    @staticmethod
    def read_nurse(nurse_id):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "SELECT * FROM enfermeiros WHERE id = %s"
                    cursor.execute(query, (nurse_id,))
                    nurse = cursor.fetchone()
                    if nurse:
                        return {
                            'id': nurse[0],
                            'nome': nurse[1],
                            'coren': nurse[2],
                            'cpf': nurse[3],
                            'especialidade_id': nurse[4],
                            'telefone': nurse[5],
                            'email': nurse[6]
                        }
                    else:
                        logging.info("Enfermeiro(a) não encontrado(a).")
                        return None
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar buscar o(a) enfermeiro(a): {err}")
            return None

    @staticmethod
    def update_nurse(nurse_id, nome, coren, cpf, especialidade_id, telefone, email):
        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    UPDATE enfermeiros
                    SET nome = %s, coren = %s, cpf = %s, especialidade_id = %s, telefone = %s, email = %s
                    WHERE id = %s
                    """
                    cursor.execute(query, (nome, coren, cpf, especialidade_id, telefone, email, nurse_id))
                    conn.commit()
                    logging.info("Enfermeiro(a) atualizado(a) com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar atualizar o(a) enfermeiro(a): {err}")

    @staticmethod
    def delete_nurse(nurse_id, user_is_admin):
        if not user_is_admin:
            logging.warning("Permissão negada: usuário não é administrador.")
            return

        try:
            with get_db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "DELETE FROM enfermeiros WHERE id = %s"
                    cursor.execute(query, (nurse_id,))
                    conn.commit()
                    logging.info("Enfermeiro(a) deletado(a) com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar deletar o(a) enfermeiro(a): {err}")
