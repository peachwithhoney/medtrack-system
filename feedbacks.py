from db_operations import insert_data, query_data

def enviar_feedback(paciente_id, consulta_id, tratamento_id, rating, comentario):
    query = """
        INSERT INTO feedbacks (paciente_id, consulta_id, tratamento_id, rating, comentario)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (paciente_id, consulta_id, tratamento_id, rating, comentario)
    insert_data(query, params)

def visualizar_feedbacks_consulta(consulta_id):
    query = """
        SELECT f.rating, f.comentario, p.nome AS nome_paciente
        FROM feedbacks f
        JOIN pacientes p ON f.paciente_id = p.id
        WHERE f.consulta_id = %s
    """
    params = (consulta_id,)
    return query_data(query, params, fetch_all=True)

def visualizar_feedbacks_tratamento(tratamento_id):
    query = """
        SELECT f.rating, f.comentario, p.nome AS nome_paciente
        FROM feedbacks f
        JOIN pacientes p ON f.paciente_id = p.id
        WHERE f.tratamento_id = %s
    """
    params = (tratamento_id,)
    return query_data(query, params, fetch_all=True)

def visualizar_feedbacks_paciente(paciente_id):
    query = """
        SELECT f.rating, f.comentario, c.data_consulta, m.nome AS nome_medico
        FROM feedbacks f
        JOIN consultas c ON f.consulta_id = c.id
        JOIN medicos m ON c.medico_id = m.id
        WHERE f.paciente_id = %s
        ORDER BY c.data_consulta DESC
    """
    params = (paciente_id,)
    return query_data(query, params, fetch_all=True)

def visualizar_feedbacks_medico(medico_id):
    query = """
        SELECT f.rating, f.comentario, c.data_consulta, p.nome AS nome_paciente
        FROM feedbacks f
        JOIN consultas c ON f.consulta_id = c.id
        JOIN pacientes p ON f.paciente_id = p.id
        WHERE c.medico_id = %s
        ORDER BY c.data_consulta DESC
    """
    params = (medico_id,)
    return query_data(query, params, fetch_all=True)
