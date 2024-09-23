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

class ConsultationManager:
    from db_connection import RealDB, get_db_connection

class ConsultationManager:
    @staticmethod
    def create_consultation(paciente_id, medico_id, data_hora_consulta, observacoes):
        query = """
        INSERT INTO consultas (paciente_ID, medico_ID, data_hora, observacoes) 
        VALUES (%s, %s, %s, %s)
        """
        params = (paciente_id, medico_id, data_hora_consulta, observacoes)
        with get_db_connection() as db:
            db.query(query, params)
            try:
                db.query(query, params)
                db.connection.commit() 
                print("Consulta inserida com sucesso!")
            except Error as e:
                print(f"Erro ao inserir consulta: {e}")
                db.connection.rollback()

    @staticmethod
    def read_consultation(consulta_id):
        query = "SELECT * FROM consultas WHERE id = %s"
        params = (consulta_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]  
            else:
                logging.info("Consulta não encontrada.")
                return None

    @staticmethod
    def update_consultation(consulta_id, paciente_id, medico_id, data_consulta, hora_consulta, observacoes):
        query = """
        UPDATE consultas
        SET paciente_id = %s, medico_id = %s, data_consulta = %s, hora_consulta = %s, observacoes = %s
        WHERE id = %s
        """
        params = (paciente_id, medico_id, data_consulta, hora_consulta, observacoes, consulta_id)
        with get_db_connection() as db:
            db.query(query, params)
            db.connection.commit()
            logging.info("Consulta atualizada com sucesso!")

    @staticmethod
    def delete_consultation(consulta_id):

        query = "DELETE FROM consultas WHERE id = %s"
        params = (consulta_id,)
        
        try:
            with get_db_connection() as db:
                db.query(query, params)  
                db.connection.commit() 
                logging.info("Consulta deletada com sucesso!")
                print("Consulta deletada com sucesso!") 
        except Error as e:
            logging.error(f"Erro ao deletar consulta: {e}")
            print(f"Erro ao deletar consulta: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_consultations():
        query = "SELECT * FROM consultas"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []

