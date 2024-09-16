from db_operations import insert_data, update_data, execute_query

def criar_consulta(paciente_id, medico_id, data_consulta, horario, motivo):
    query = """
        INSERT INTO consultas (paciente_id, medico_id, data_consulta, horario, motivo)
        VALUES (%s, %s, %s, %s, %s)
    """
    params = (paciente_id, medico_id, data_consulta, horario, motivo)
    insert_data(query, params)

def atualizar_consulta(consulta_id, paciente_id=None, medico_id=None, data_consulta=None, horario=None, motivo=None):
    update_fields = []
    params = []
    
    if paciente_id is not None:
        update_fields.append("paciente_id = %s")
        params.append(paciente_id)
    if medico_id is not None:
        update_fields.append("medico_id = %s")
        params.append(medico_id)
    if data_consulta is not None:
        update_fields.append("data_consulta = %s")
        params.append(data_consulta)
    if horario is not None:
        update_fields.append("horario = %s")
        params.append(horario)
    if motivo is not None:
        update_fields.append("motivo = %s")
        params.append(motivo)
    
    params.append(consulta_id)
    update_string = ", ".join(update_fields)
    query = f"UPDATE consultas SET {update_string} WHERE id = %s"
    
    update_data(query, params)

def cancelar_consulta(consulta_id):
    query = "DELETE FROM consultas WHERE id = %s"
    params = (consulta_id,)
    update_data(query, params)

def verificar_consulta(consulta_id=None):
    query = "SELECT * FROM consultas"
    params = ()
    
    if consulta_id is not None:
        query += " WHERE id = %s"
        params = (consulta_id,)
    
    return execute_query(query, params, fetch_one=(consulta_id is not None))

def historico_consultas_paciente(paciente_id):
    query = """
        SELECT c.id, c.data_consulta, c.horario, c.motivo, m.nome AS nome_medico
        FROM consultas c
        JOIN medicos m ON c.medico_id = m.id
        WHERE c.paciente_id = %s
        ORDER BY c.data_consulta DESC, c.horario DESC
    """
    params = (paciente_id,)
    return execute_query(query, params, fetch_all=True)

def historico_consultas_medico(medico_id):
    query = """
        SELECT c.id, c.data_consulta, c.horario, c.motivo, p.nome AS nome_paciente
        FROM consultas c
        JOIN pacientes p ON c.paciente_id = p.id
        WHERE c.medico_id = %s
        ORDER BY c.data_consulta DESC, c.horario DESC
    """
    params = (medico_id,)
    return execute_query(query, params, fetch_all=True)
