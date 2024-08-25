from db_connection import create_connection, close_connection

def execute_query(query, params=None):
    connection = create_connection()
    result = None
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        result = cursor.fetchall()
        connection.commit()
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
    finally:
        close_connection(connection)
    return result

def insert_data(query, params):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            cursor.close()
            connection.close()

def update_data(query, params):
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            connection.commit()
        except Exception as e:
            print(f"Erro ao atualizar dados: {e}")
        finally:
            cursor.close()
            connection.close()
