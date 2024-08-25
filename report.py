import db_operations

def generate_monthly_report():
    query = """
    SELECT 
        'Relatório Mensal' AS tipo_relatorio,
        NOW() AS data_criacao,
        'Relatório de atividades do mês atual' AS descricao,
        GROUP_CONCAT(CONCAT('Consulta: ', c.id, ' - Data: ', c.data_hora) SEPARATOR '\n') AS conteudo
    FROM consultas c
    WHERE MONTH(c.data_hora) = MONTH(CURRENT_DATE())
    """
    return db_operations.execute_query(query)

def generate_annual_report():
    query = """
    SELECT 
        'Relatório Anual' AS tipo_relatorio,
        NOW() AS data_criacao,
        'Relatório anual de desempenho' AS descricao,
        GROUP_CONCAT(CONCAT('Tratamento: ', t.id, ' - Tipo: ', t.tipo_tratamento) SEPARATOR '\n') AS conteudo
    FROM tratamentos t
    WHERE YEAR(t.data_inicio) = YEAR(CURRENT_DATE())
    """
    return db_operations.execute_query(query)

def generate_exams_report():
    query = """
    SELECT 
        'Relatório de Exames' AS tipo_relatorio,
        NOW() AS data_criacao,
        'Relatório de exames realizados' AS descricao,
        GROUP_CONCAT(CONCAT('Exame: ', e.id, ' - Tipo: ', e.tipo_exame) SEPARATOR '\n') AS conteudo
    FROM exames e
    """
    return db_operations.execute_query(query)

def generate_consultations_report():
    query = """
    SELECT 
        'Relatório de Consultas' AS tipo_relatorio,
        NOW() AS data_criacao,
        'Relatório de consultas realizadas' AS descricao,
        GROUP_CONCAT(CONCAT('Consulta: ', c.id, ' - Data: ', c.data_hora) SEPARATOR '\n') AS conteudo
    FROM consultas c
    """
    return db_operations.execute_query(query)

def generate_treatments_report():
    query = """
    SELECT 
        'Relatório de Tratamentos' AS tipo_relatorio,
        NOW() AS data_criacao,
        'Relatório de tratamentos efetuados' AS descricao,
        GROUP_CONCAT(CONCAT('Tratamento: ', t.id, ' - Tipo: ', t.tipo_tratamento) SEPARATOR '\n') AS conteudo
    FROM tratamentos t
    """
    return db_operations.execute_query(query)
