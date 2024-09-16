from db_operations import insert_data, update_data, execute_query

def registrar_entrada(enfermeiro_id, data_hora_entrada):
    query = """
        INSERT INTO pontos_enfermeiros (enfermeiro_id, data_hora_entrada)
        VALUES (%s, %s)
    """
    params = (enfermeiro_id, data_hora_entrada)
    insert_data(query, params)

def registrar_saida(ponto_id, data_hora_saida):
    query = """
        UPDATE pontos_enfermeiros
        SET data_hora_saida = %s
        WHERE id = %s
    """
    params = (data_hora_saida, ponto_id)
    update_data(query, params)

def deletar_ponto(ponto_id):
    query = "DELETE FROM pontos_enfermeiros WHERE id = %s"
    params = (ponto_id,)
    update_data(query, params)

def consultar_ponto(ponto_id=None):
    query = "SELECT * FROM pontos_enfermeiros"
    params = ()
    
    if ponto_id is not None:
        query += " WHERE id = %s"
        params = (ponto_id,)
    
    return execute_query(query, params, fetch_one=(ponto_id is not None))

def relatorio_horas_trabalhadas(enfermeiro_id, data_inicio, data_fim):
    query = """
        SELECT enfermeiro_id, data_hora_entrada, data_hora_saida,
               TIMESTAMPDIFF(HOUR, data_hora_entrada, data_hora_saida) AS horas_trabalhadas
        FROM pontos_enfermeiros
        WHERE enfermeiro_id = %s
          AND data_hora_entrada >= %s
          AND data_hora_saida <= %s
        ORDER BY data_hora_entrada ASC
    """
    params = (enfermeiro_id, data_inicio, data_fim)
    return execute_query(query, params, fetch_all=True)
