from db_connection import get_db_connection

def execute_query(query, params=None, fetch_one=False, fetch_all=False):
    result = None
    try:
        with get_db_connection() as db:
            if fetch_one:
                result = db.query(query, params)
                if result:
                    result = result[0] 
            elif fetch_all:
                result = db.query(query, params)
            else:
               
                db.query(query, params)
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
    return result

def insert_data(query, params):
    try:
        with get_db_connection() as db:
            db.query(query, params)
            db.connection.commit()
    except Exception as e:
        print(f"Erro ao inserir dados: {e}")

def delete_data(query, params):
    try:
        with get_db_connection() as db:
            db.query(query, params)
            db.connection.commit()
    except Exception as e:
        print(f"Erro ao deletar dados: {e}")

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
