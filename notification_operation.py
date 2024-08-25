from db_operations import insert_data, update_data, delete_data, query_data

def create_notification(paciente_id, medico_id, consulta_id, mensagem, data_hora, lida=False):
    query = """
    INSERT INTO notificacoes (paciente_id, medico_id, consulta_id, mensagem, data_hora, lida)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (paciente_id, medico_id, consulta_id, mensagem, data_hora, lida)
    insert_data(query, params)

def update_notification_status(notification_id, lida):
    query = """
    UPDATE notificacoes
    SET lida = %s
    WHERE id = %s
    """
    params = (lida, notification_id)
    update_data(query, params)

def delete_notification(notification_id):
    query = "DELETE FROM notificacoes WHERE id = %s"
    params = (notification_id,)
    delete_data(query, params)

def get_notifications(paciente_id=None, medico_id=None, consulta_id=None):
    query = "SELECT * FROM notificacoes WHERE 1=1"
    params = []
    
    if paciente_id:
        query += " AND paciente_id = %s"
        params.append(paciente_id)
    
    if medico_id:
        query += " AND medico_id = %s"
        params.append(medico_id)
    
    if consulta_id:
        query += " AND consulta_id = %s"
        params.append(consulta_id)
    
    return query_data(query, tuple(params))