from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class PacienteManager:
    
    @staticmethod
    def create_paciente(nome, data_nascimento, cpf, endereco, telefone, email):
        query = """
        INSERT INTO pacientes (nome, data_nascimento, cpf, endereco, telefone, email) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        params = (nome, data_nascimento, cpf, endereco, telefone, email)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Paciente inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir paciente: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_paciente(paciente_id):
        query = "SELECT * FROM pacientes WHERE id = %s"
        params = (paciente_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Paciente não encontrado.")
                return None

    @staticmethod
    def update_paciente(paciente_id, nome, data_nascimento, cpf, endereco, telefone, email):
        query = """
        UPDATE pacientes
        SET nome = %s, data_nascimento = %s, cpf = %s, endereco = %s, telefone = %s, email = %s
        WHERE id = %s
        """
        params = (nome, data_nascimento, cpf, endereco, telefone, email, paciente_id)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Paciente atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar paciente: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_paciente(paciente_id):
        query = "DELETE FROM pacientes WHERE id = %s"
        params = (paciente_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Paciente deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar paciente: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_pacientes():
        query = "SELECT * FROM pacientes"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
