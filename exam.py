from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class ExameManager:
    
    @staticmethod
    def create_exame(paciente_id, medico_id, enfermeiro_id, tipo_exame, data_hora, resultado, observacoes):
        query = """
        INSERT INTO exames (paciente_id, medico_id, enfermeiro_id, tipo_exame, data_hora, resultado, observacoes) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (paciente_id, medico_id, enfermeiro_id, tipo_exame, data_hora, resultado, observacoes)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Exame inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir exame: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_exame(exame_id):
        query = "SELECT * FROM exames WHERE id = %s"
        params = (exame_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Exame não encontrado.")
                return None

    @staticmethod
    def update_exame(paciente_id, medico_id, enfermeiro_id, tipo_exame, data_hora, resultado, observacoes):
        query = """
        UPDATE exames
        SET paciente_id = %s, medico_id = %s, enfermeiro_id = %s, tipo_exame = %s, data_hora = %s, resultado = %s, observacoes = %s
        WHERE id = %s
        """
        params = (paciente_id, medico_id, enfermeiro_id, tipo_exame, data_hora, resultado, observacoes)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Exame atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar exame: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_exame(exame_id):
        query = "DELETE FROM exames WHERE id = %s"
        params = (exame_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Exame deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar exame: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_exames():
        query = "SELECT * FROM exames"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
