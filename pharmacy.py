from mysql.connector import Error
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

class MedicamentoManager:
    
    @staticmethod
    def create_medicamento(nome, descricao, estoque, alerta_estoque):
        query = """
        INSERT INTO medicamentos (nome, descricao, estoque, alerta_estoque) 
        VALUES (%s, %s, %s, %s)
        """
        params = (nome, descricao, estoque, alerta_estoque)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Medicamento inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir medicamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_medicamento(medicamento_id):
        query = "SELECT * FROM medicamentos WHERE id = %s"
        params = (medicamento_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Medicamento não encontrado.")
                return None

    @staticmethod
    def update_medicamento(medicamento_id, nome, descricao, estoque, alerta_estoque):
        query = """
        UPDATE medicamentos
        SET nome = %s, descricao = %s, estoque = %s, alerta_estoque = %s
        WHERE id = %s
        """
        params = (nome, descricao, estoque, alerta_estoque, medicamento_id)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Medicamento atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar medicamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_medicamento(medicamento_id):
        query = "DELETE FROM medicamentos WHERE id = %s"
        params = (medicamento_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Medicamento deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar medicamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_medicamentos():
        query = "SELECT * FROM medicamentos"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
