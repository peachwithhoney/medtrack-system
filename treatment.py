from mysql.connector import Error
import logging
from contextlib import contextmanager
from db_connection import get_db_connection

logging.basicConfig(level=logging.INFO)

class TratamentoManager:
    
    @staticmethod
    def create_tratamento(paciente_id, enfermeiro_id, tipo_tratamento, data_inicio, data_fim, custos, resultados, observacoes):
        query = """
        INSERT INTO tratamentos (paciente_id, enfermeiro_id, tipo_tratamento, data_inicio, data_fim, custos, resultados, observacoes) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (paciente_id, enfermeiro_id, tipo_tratamento, data_inicio, data_fim, custos, resultados, observacoes)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Tratamento inserido com sucesso!")
        except Error as e:
            logging.error(f"Erro ao inserir tratamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def read_tratamento(tratamento_id):
        query = "SELECT * FROM tratamentos WHERE id = %s"
        params = (tratamento_id,)
        with get_db_connection() as db:
            result = db.query(query, params)
            if result:
                return result[0]
            else:
                logging.info("Tratamento não encontrado.")
                return None

    @staticmethod
    def update_tratamento(paciente_id, enfermeiro_id, tipo_tratamento, data_inicio, data_fim, custos, resultados, observacoes):
        query = """
        UPDATE tratamentos
        SET paciente_id = %s, enfermeiro_id = %s, tipo_tratamento = %s, data_inicio = %s, data_fim = %s, custos = %s, resultados = %s, observacoes = %s
        WHERE id = %s
        """
        params = (paciente_id, enfermeiro_id, tipo_tratamento, data_inicio, data_fim, custos, resultados, observacoes)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Tratamento atualizado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao atualizar tratamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def delete_tratamento(tratamento_id):
        query = "DELETE FROM tratamentos WHERE id = %s"
        params = (tratamento_id,)
        try:
            with get_db_connection() as db:
                db.query(query, params)
                db.connection.commit()
                logging.info("Tratamento deletado com sucesso!")
        except Error as e:
            logging.error(f"Erro ao deletar tratamento: {e}")
            if db.connection:
                db.connection.rollback()

    @staticmethod
    def get_all_tratamentos():
        query = "SELECT * FROM tratamentos"
        with get_db_connection() as db:
            result = db.query(query)
            if result is not None:
                return result
            return []
