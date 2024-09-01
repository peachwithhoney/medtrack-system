from db_operations import insert_data, update_data, query_data

def criar_exame(nome, descricao, paciente_id, medico_id, data_exame):
    query = """
        INSERT INTO exames (nome, descricao, paciente_id, medico_id, data_exame)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (nome, descricao, paciente_id, medico_id, data_exame)
    insert_data(query, params)

def atualizar_exame(exame_id, nome=None, descricao=None, paciente_id=None, medico_id=None, data_exame=None):
    update_fields = []
    params = []
    
    if nome is not None:
        update_fields.append("nome = %s")
        params.append(nome)
    if descricao is not None:
        update_fields.append("descricao = %s")
        params.append(descricao)
    if paciente_id is not None:
        update_fields.append("paciente_id = %s")
        params.append(paciente_id)
    if medico_id is not None:
        update_fields.append("medico_id = %s")
        params.append(medico_id)
    if data_exame is not None:
        update_fields.append("data_exame = %s")
        params.append(data_exame)
    
    params.append(exame_id)
    update_string = ", ".join(update_fields)
    query = f"UPDATE exames SET {update_string} WHERE id = %s"
    
    update_data(query, params)

def deletar_exame(exame_id):
    query = "DELETE FROM exames WHERE id = %s"
    params = (exame_id,)
    update_data(query, params)

def consultar_exame(exame_id=None):
    query = "SELECT * FROM exames"
    params = ()
    
    if exame_id is not None:
        query += " WHERE id = %s"
        params = (exame_id,)
    
    return query_data(query, params, fetch_one=(exame_id is not None))

def registrar_resultado_exame(exame_id, resultado, observacoes):
    query = """
        UPDATE exames
        SET resultado = %s, observacoes = %s, data_resultado = NOW()
        WHERE id = %s
    """
    params = (resultado, observacoes, exame_id)
    update_data(query, params)

def consultar_resultados_paciente(paciente_id):
    query = """
        SELECT e.id, e.nome, e.descricao, e.data_exame, e.resultado, e.observacoes, e.data_resultado, m.nome AS nome_medico
        FROM exames e
        JOIN medicos m ON e.medico_id = m.id
        WHERE e.paciente_id = %s
        ORDER BY e.data_exame DESC
    """
    params = (paciente_id,)
    return query_data(query, params, fetch_all=True)
