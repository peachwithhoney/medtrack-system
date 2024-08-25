import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conectado ao banco de dados")
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: '{e}' ")

    return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexão com o banco de dados fechada .")

