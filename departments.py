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

class DepartmentManager:
    @staticmethod
    def create_department(nome, descricao):
        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    INSERT INTO departamentos (nome, descricao)
                    VALUES (%s, %s)
                    """
                    cursor.execute(query, (nome, descricao))
                    conn.commit()
                    logging.info("Departmento criado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar criar o departamento : {err}")

    @staticmethod
    def read_departments():
        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "SELECT * FROM departamentos"
                    cursor.execute(query)
                    departments = cursor.fetchall()
                    return departments
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar visualizar o departamento : {err}")
            return []

    @staticmethod
    def update_department(id, new_nome, new_descricao):
        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = """
                    UPDATE departamentos
                    SET nome = %s, descricao = %s
                    WHERE id = %s
                    """
                    cursor.execute(query, (new_nome, new_descricao, id))
                    conn.commit()
                    logging.info("Departmento atualizado com sucesso!")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar atualizar o departamento: {err}")

    @staticmethod
    def delete_department(id, user_is_admin):
        if not user_is_admin:
            logging.warning("Access negado. Apenas administradores podem deletar departamentos.")
            return

        try:
            with db_connection() as conn:
                with get_cursor(conn) as cursor:
                    query = "DELETE FROM departamentos WHERE id = %s"
                    cursor.execute(query, (id,))
                    conn.commit()
                    logging.info("Departmento deletado com sucesso")
        except mysql.connector.Error as err:
            logging.error(f"Erro ao tentar deletar o departamento : {err}")
