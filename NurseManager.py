from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class EnfermeiroManager:
    
    @staticmethod
    def create_enfermeiro(nome, coren, cpf, especialidade_id, telefone, email):
        query = """
        INSERT INTO enfermeiros (nome, coren, cpf, especialidade_id, telefone, email) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (nome, coren, cpf, especialidade_id, telefone, email)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Enfermeiro inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir enfermeiro: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_enfermeiro(enfermeiro_id):
        query = "SELECT * FROM enfermeiros WHERE id = %s"
        params = (enfermeiro_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Enfermeiro não encontrado.")
                return None

    @staticmethod
    def update_enfermeiro(enfermeiro_id, nome, coren, cpf, especialidade_id, telefone, email):
        query = """
        UPDATE enfermeiros
        SET nome = %s, coren = %s, cpf = %s, especialidade_id = %s, telefone = %s, email = %s
        WHERE id = %s
        """
        params = (nome, coren, cpf, especialidade_id, telefone, email, enfermeiro_id)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Enfermeiro atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar enfermeiro: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_enfermeiro(enfermeiro_id):
        query = "DELETE FROM enfermeiros WHERE id = %s"
        params = (enfermeiro_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Enfermeiro deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar enfermeiro: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_enfermeiros():
        query = "SELECT * FROM enfermeiros"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
