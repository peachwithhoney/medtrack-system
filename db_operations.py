from db_connection import get_db_connection

def execute_query(query, params=None):
    result = None
    try:
        with get_db_connection() as db:
            result = db.query(query, params)
        return result
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None

def insert_data(query, params):
    try:
        with get_db_connection() as db:
            db.query(query, params)
            db.connection.commit()
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def update_data(query, params):
    try:
        with get_db_connection() as db:
            db.query(query, params)
            db.connection.commit()
    except Exception as e:
        print(f"Erro ao atualizar dados: {e}")

def query_user_by_email(email):
    query = "SELECT * FROM usuarios WHERE email = %s"
    return execute_query(query, (email,))
