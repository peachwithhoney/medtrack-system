# db_connection.py

import mysql.connector
from mysql.connector import Error

class RealDB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Conexão com o banco de dados estabelecida.")
        except Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.connection = None

    def query(self, query, params=None):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Error as e:
            print(f"Erro ao executar a consulta: {e}")
            return None

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexão com o banco de dados encerrada.")


db = RealDB(host='localhost', database='nome_do_banco', user='seu_usuario', password='sua_senha')
db.connect()
