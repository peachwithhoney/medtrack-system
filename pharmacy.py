from db_operations import insert_data, update_data, query_data

def add_medicamento(nome, descricao, estoque, alerta_estoque):
    query = """
        INSERT INTO medicamentos (nome, descricao, estoque, alerta_estoque)
        VALUES (%s, %s, %s, %s)
    """
    params = (nome, descricao, estoque, alerta_estoque)
    insert_data(query, params)

def update_medicamento(id, nome=None, descricao=None, estoque=None, alerta_estoque=None):
    update_fields = []
    params = []
    
    if nome is not None:
        update_fields.append("nome = %s")
        params.append(nome)
    if descricao is not None:
        update_fields.append("descricao = %s")
        params.append(descricao)
    if estoque is not None:
        update_fields.append("estoque = %s")
        params.append(estoque)
    if alerta_estoque is not None:
        update_fields.append("alerta_estoque = %s")
        params.append(alerta_estoque)
    
    params.append(id)
    update_string = ", ".join(update_fields)
    query = f"UPDATE medicamentos SET {update_string} WHERE id = %s"
    
    update_data(query, params)

def get_medicamentos(medicamento_id=None):
    query = "SELECT * FROM medicamentos"
    params = ()
    
    if medicamento_id is not None:
        query += " WHERE id = %s"
        params = (medicamento_id,)
    
    return query_data(query, params, fetch_one=(medicamento_id is not None))

def check_estoque():
    query = "SELECT * FROM medicamentos WHERE estoque < alerta_estoque"
    return query_data(query, fetch_all=True)

def create_prescricao(paciente_id, medico_id, medicamento_id, quantidade, data_prescricao):
    query = """
        INSERT INTO prescricoes (paciente_id, medico_id, medicamento_id, quantidade, data_prescricao)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (paciente_id, medico_id, medicamento_id, quantidade, data_prescricao)
    insert_data(query, params)

def search_medicamentos_by_name(name):
    query = "SELECT * FROM medicamentos WHERE nome LIKE %s"
    params = (f"%{name}%",)
    return query_data(query, params, fetch_all=True)

def filter_medicamentos_by_estoque(min_estoque, max_estoque):
    query = "SELECT * FROM medicamentos WHERE 1=1"
    params = []

    if min_estoque is not None:
        query += " AND estoque >= %s"
        params.append(min_estoque)

    if max_estoque is not None:
        query += " AND estoque <= %s"
        params.append(max_estoque)

    return query_data(query, params, fetch_all=True)

def filter_medicamentos_by_alerta():
    query = "SELECT * FROM medicamentos WHERE estoque < alerta_estoque"

    return query_data(query, fetch_all=True)