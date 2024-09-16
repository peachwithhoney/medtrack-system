from db_operations import insert_data, execute_query

def contar_feedbacks():
    query = """
    SELECT 
        SUM(CASE WHEN avaliacao BETWEEN 1 AND 2 THEN 1 ELSE 0 END) AS negativos,
        SUM(CASE WHEN avaliacao = 3 THEN 1 ELSE 0 END) AS neutros,
        SUM(CASE WHEN avaliacao BETWEEN 4 AND 5 THEN 1 ELSE 0 END) AS positivos
    FROM feedbacks
    """
    result = execute_query(query)
    if result and len(result) > 0:
        data = result[0]
        return {
            'positivos': data.get('positivos', 0),
            'negativos': data.get('negativos', 0),
            'neutros': data.get('neutros', 0)
        }
    return {
        'positivos': 0,
        'negativos': 0,
        'neutros': 0
    }



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
    return execute_query(query, params, fetch_all=True)

def visualizar_feedbacks_tratamento(tratamento_id):
    query = """
        SELECT f.rating, f.comentario, p.nome AS nome_paciente
        FROM feedbacks f
        JOIN pacientes p ON f.paciente_id = p.id
        WHERE f.tratamento_id = %s
    """
    params = (tratamento_id,)
    return execute_query(query, params, fetch_all=True)

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
    return execute_query(query, params, fetch_all=True)

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
    return execute_query(query, params, fetch_all=True)
