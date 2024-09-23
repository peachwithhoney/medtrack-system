from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class DepartamentoManager:
    
    @staticmethod
    def create_departamento(nome, localizacao, recursos):
        query = """
        INSERT INTO departamentos (nome, localizacao, recursos) 
        VALUES (%s, %s, %s)
        """
        params = (nome, localizacao, recursos)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Departamento inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir departamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_departamento(departamento_id):
        query = "SELECT * FROM departamentos WHERE id = %s"
        params = (departamento_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Departamento não encontrado.")
                return None

    @staticmethod
    def update_departamento(departamento_id, nome, localizacao, recursos):
        query = """
        UPDATE departamentos
        SET nome = %s, localizacao = %s, recursos = %s
        WHERE id = %s
        """
        params = (nome, localizacao, recursos, departamento_id)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Departamento atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar departamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_departamento(departamento_id):
        query = "DELETE FROM departamentos WHERE id = %s"
        params = (departamento_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Departamento deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar departamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_departamentos():
        query = "SELECT * FROM departamentos"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
