import mysql.connector
import logging
from contextlib import contextmanager
import db_connection

logging.basicConfig(level=logging.INFO)

@contextmanager
def get_cursor(conn):
    cursor = conn.cursor()
    try:
        yield cursor
    finally:
        cursor.close()

class SurgeryManager:
    @staticmethod
    def create_surgery(paciente_id, medico_id, data, tipo, descricao):
        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    INSERT INTO cirurgias (paciente_id, medico_id, tipo_cirurgia, descricao)
                    VALUES (%s, %s, %s, %s)
                    """
                    cursor.execute(query, (paciente_id, medico_id, tipo, descricao))
                    conn.commit()
                    logging.info("Surgery recorded successfully!")
        except mysql.connector.Error as err:
            logging.error(f"Error creating surgery: {err}")

    @staticmethod
    def read_surgeries():
        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "SELECT * FROM cirurgias"
                    cursor.execute(query)
                    surgeries = cursor.fetchall()
                    return surgeries
        except mysql.connector.Error as err:
            logging.error(f"Error reading surgeries: {err}")
            return []

    @staticmethod
    def update_surgery(id, new_paciente_id, new_medico_id, new_data, new_tipo, new_descricao):
        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    UPDATE cirurgias
                    SET paciente_id = %s, medico_id = %s, tipo_cirurgia = %s, descricao = %s
                    WHERE id = %s
                    """
                    cursor.execute(query, (new_paciente_id, new_medico_id, new_tipo, new_descricao, id))
                    conn.commit()
                    logging.info("Surgery updated successfully!")
        except mysql.connector.Error as err:
            logging.error(f"Error updating surgery: {err}")

    @staticmethod
    def delete_surgery(id, user_is_admin):
        if not user_is_admin:
            logging.warning("Access denied. Only administrators can delete surgeries.")
            return

        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "DELETE FROM cirurgias WHERE id = %s"
                    cursor.execute(query, (id,))
                    conn.commit()
                    logging.info("Surgery deleted successfully!")
        except mysql.connector.Error as err:
            logging.error(f"Error deleting surgery: {err}")
