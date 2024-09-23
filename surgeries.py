from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class CirurgiaManager:
    
    @staticmethod
    def create_cirurgia(cirurgia_id, paciente_id, medico_id, enfermeiro_id, tipo_cirurgia, resultados, observacoes):
        query = """
        INSERT INTO cirurgias (cirurgia_id, paciente_id, medico_id, enfermeiro_id, tipo_cirurgia, resultados, observacoes) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (cirurgia_id, paciente_id, medico_id, enfermeiro_id, tipo_cirurgia, resultados, observacoes)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Cirurgia inserida com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir cirurgia: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_cirurgia(cirurgia_id):
        query = "SELECT * FROM cirurgias WHERE id = %s"
        params = (cirurgia_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Cirurgia não encontrada.")
                return None

    @staticmethod
    def update_cirurgia(cirurgia_id, paciente_id, medico_id, enfermeiro_id, tipo_cirurgia, resultados, observacoes):
        query = """
        UPDATE cirurgias
        SET paciente_id = %s, medico_id = %s, enfermeiro_id = %s, tipo_cirurgia = %s, resultados = %s, observacoes = %s
        WHERE id = %s
        """
        params = (cirurgia_id, paciente_id, medico_id, enfermeiro_id, tipo_cirurgia, resultados, observacoes)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Cirurgia atualizada com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar cirurgia: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_cirurgia(cirurgia_id):
        query = "DELETE FROM cirurgias WHERE id = %s"
        params = (cirurgia_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Cirurgia deletada com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar cirurgia: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_cirurgias():
        query = "SELECT * FROM cirurgias"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
