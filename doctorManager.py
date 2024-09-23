from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class MedicoManager:
    
    @staticmethod
    def create_medico(nome, crm, cpf, especialidade_id, telefone, email):
        query = """
        INSERT INTO medicos (nome, crm, cpf, especialidade_id, telefone, email) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (nome, crm, cpf, especialidade_id, telefone, email)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Médico inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir médico: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_medico(medico_id):
        query = "SELECT * FROM medicos WHERE id = %s"
        params = (medico_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Médico não encontrado.")
                return None

    @staticmethod
    def update_medico(medico_id, nome, crm, cpf, especialidade_id, telefone, email):
        query = """
        UPDATE medicos
        SET nome = %s, crm = %s, cpf = %s, especialidade_id = %s, telefone = %s, email = %s
        WHERE id = %s
        """
        params = (nome, crm, cpf, especialidade_id, telefone, email, medico_id)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Médico atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar médico: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_medico(medico_id):
        query = "DELETE FROM medicos WHERE id = %s"
        params = (medico_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Médico deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar médico: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_medicos():
        query = "SELECT * FROM medicos"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
