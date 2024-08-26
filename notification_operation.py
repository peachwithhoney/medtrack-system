from db_operations import insert_data, update_data, delete_data, query_data
import logging

def create_notification(paciente_id, medico_id, consulta_id, mensagem, data_hora, lida=False):
    if not all([paciente_id, medico_id, consulta_id, mensagem, data_hora]):
        logging.error("Erro: Parâmetros obrigatórios ausentes ao criar notificação.")
        return None
    
    query = """
    INSERT INTO notificacoes (paciente_id, medico_id, consulta_id, mensagem, data_hora, lida)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params = (paciente_id, medico_id, consulta_id, mensagem, data_hora, lida)
    try:
        notification_id = insert_data(query, params, fetch_lastrowid=True)
        return notification_id
    except Exception as e:
        logging.error(f"Erro ao criar notificação: {e}")
        return None

def update_notification_status(notification_id, lida):
    if notification_id is None:
        logging.error("Erro: ID da notificação ausente ao atualizar status.")
        return False

    query = """
    UPDATE notificacoes
    SET lida = %s
    WHERE id = %s
    """
    params = (lida, notification_id)
    try:
        rows_affected = update_data(query, params)
        return rows_affected > 0
    except Exception as e:
        logging.error(f"Erro ao atualizar status da notificação: {e}")
        return False

def delete_notification(notification_id):
    if notification_id is None:
        logging.error("Erro: ID da notificação ausente ao deletar.")
        return False
    
    query = "DELETE FROM notificacoes WHERE id = %s"
    params = (notification_id,)
    try:
        rows_affected = delete_data(query, params)
        return rows_affected > 0
    except Exception as e:
        logging.error(f"Erro ao deletar notificação: {e}")
        return False

def get_notifications(paciente_id=None, medico_id=None, consulta_id=None):
    query = "SELECT * FROM notificacoes WHERE 1=1"
    params = []
    
    if paciente_id is not None:
        query += " AND paciente_id = %s"
        params.append(paciente_id)
    
    if medico_id is not None:
        query += " AND medico_id = %s"
        params.append(medico_id)
    
    if consulta_id is not None:
        query += " AND consulta_id = %s"
        params.append(consulta_id)
    
    try:
        return query_data(query, tuple(params))
    except Exception as e:
        logging.error(f"Erro ao buscar notificações: {e}")
        return []
