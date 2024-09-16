from db_operations import insert_data, update_data, execute_query

def criar_tratamento(nome, descricao, duracao, medico_id):
    query = """
        INSERT INTO tratamentos (nome, descricao, duracao, medico_id)
        VALUES (%s, %s, %s, %s)
    """
    params = (nome, descricao, duracao, medico_id)
    insert_data(query, params)

def atualizar_tratamento(tratamento_id, nome=None, descricao=None, duracao=None, medico_id=None):
    update_fields = []
    params = []
    
    if nome is not None:
        update_fields.append("nome = %s")
        params.append(nome)
    if descricao is not None:
        update_fields.append("descricao = %s")
        params.append(descricao)
    if duracao is not None:
        update_fields.append("duracao = %s")
        params.append(duracao)
    if medico_id is not None:
        update_fields.append("medico_id = %s")
        params.append(medico_id)
    
    params.append(tratamento_id)
    update_string = ", ".join(update_fields)
    query = f"UPDATE tratamentos SET {update_string} WHERE id = %s"
    
    update_data(query, params)

def deletar_tratamento(tratamento_id):
    query = "DELETE FROM tratamentos WHERE id = %s"
    params = (tratamento_id,)
    update_data(query, params)

def consultar_tratamento(tratamento_id=None):
    query = "SELECT * FROM tratamentos"
    params = ()
    
    if tratamento_id is not None:
        query += " WHERE id = %s"
        params = (tratamento_id,)
    
    return execute_query(query, params, fetch_one=(tratamento_id is not None))

def registrar_tratamento_paciente(paciente_id, tratamento_id, data_inicio, data_fim):
    query = """
        INSERT INTO paciente_tratamentos (paciente_id, tratamento_id, data_inicio, data_fim)
        VALUES (%s, %s, %s, %s)
    """
    params = (paciente_id, tratamento_id, data_inicio, data_fim)
    insert_data(query, params)

def consultar_tratamentos_paciente(paciente_id):
    query = """
        SELECT pt.data_inicio, pt.data_fim, t.nome, t.descricao, t.duracao, m.nome AS nome_medico
        FROM paciente_tratamentos pt
        JOIN tratamentos t ON pt.tratamento_id = t.id
        JOIN medicos m ON t.medico_id = m.id
        WHERE pt.paciente_id = %s
        ORDER BY pt.data_inicio DESC
    """
    params = (paciente_id,)
    return execute_query(query, params, fetch_all=True)

def consultar_pacientes_tratamento(tratamento_id):
    query = """
        SELECT pt.data_inicio, pt.data_fim, p.nome AS nome_paciente, p.data_nascimento, p.genero
        FROM paciente_tratamentos pt
        JOIN pacientes p ON pt.paciente_id = p.id
        WHERE pt.tratamento_id = %s
        ORDER BY pt.data_inicio DESC
    """
    params = (tratamento_id,)
    return execute_query(query, params, fetch_all=True)
