import db_operations
import csv

def generate_report(report_type=None, start_date=None, end_date=None, format_type='txt'):
    if report_type == 'mensal':
        report_data = generate_monthly_report(start_date, end_date)
    elif report_type == 'anual':
        report_data = generate_annual_report(start_date, end_date)
    elif report_type == 'exames':
        report_data = generate_exams_report(start_date, end_date)
    elif report_type == 'consultas':
        report_data = generate_consultations_report(start_date, end_date)
    elif report_type == 'tratamentos':
        report_data = generate_treatments_report(start_date, end_date)
    elif report_type == 'medicamentos':
        report_data = generate_medicamentos_report(start_date, end_date)
    elif report_type == 'prescricoes':
        report_data = generate_prescricoes_report(start_date, end_date)
    else:
        raise ValueError("Tipo de relatório inválido.")

    file_name = f'relatorios_{report_type}.{format_type}'
    
    if format_type == 'txt':
        with open(file_name, 'w') as file:
            for row in report_data:
                file.write(f"{row}\n")
    elif format_type == 'csv':
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Tipo de Relatório', 'Data Criação', 'Descrição', 'Conteúdo'])
            writer.writerows(report_data)
    else:
        raise ValueError("Formato de relatório inválido.")
    
    print(f"Relatório '{file_name}' gerado com sucesso no formato '{format_type}'.")

def generate_monthly_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório Mensal' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório de atividades do mês atual' AS descricao,
            GROUP_CONCAT(CONCAT('Consulta: ', c.id, ' - Data: ', c.data_hora) SEPARATOR '\n') AS conteudo
        FROM consultas c
        WHERE MONTH(c.data_hora) = MONTH(CURRENT_DATE())
    """
    return db_operations.execute_query(query, fetch_all=True)

def generate_annual_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório Anual' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório anual de desempenho' AS descricao,
            GROUP_CONCAT(CONCAT('Tratamento: ', t.id, ' - Tipo: ', t.tipo_tratamento) SEPARATOR '\n') AS conteudo
        FROM tratamentos t
        WHERE YEAR(t.data_inicio) = YEAR(CURRENT_DATE())
    """
    return db_operations.execute_query(query, fetch_all=True)

def generate_exams_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório de Exames' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório de exames realizados' AS descricao,
            GROUP_CONCAT(CONCAT('Exame: ', e.id, ' - Tipo: ', e.tipo_exame) SEPARATOR '\n') AS conteudo
        FROM exames e
    """
    return db_operations.execute_query(query, fetch_all=True)

def generate_consultations_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório de Consultas' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório de consultas realizadas' AS descricao,
            GROUP_CONCAT(CONCAT('Consulta: ', c.id, ' - Data: ', c.data_hora) SEPARATOR '\n') AS conteudo
        FROM consultas c
    """
    return db_operations.execute_query(query, fetch_all=True)

def generate_treatments_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório de Tratamentos' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório de tratamentos efetuados' AS descricao,
            GROUP_CONCAT(CONCAT('Tratamento: ', t.id, ' - Tipo: ', t.tipo_tratamento) SEPARATOR '\n') AS conteudo
        FROM tratamentos t
    """
    return db_operations.execute_query(query, fetch_all=True)

def generate_medicamentos_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório de Medicamentos' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório de medicamentos e seu estoque' AS descricao,
            GROUP_CONCAT(CONCAT('Medicamento: ', m.id, ' - Nome: ', m.nome, ' - Estoque: ', m.estoque) SEPARATOR '\n') AS conteudo
        FROM medicamentos m
    """
    return db_operations.execute_query(query, fetch_all=True)

def generate_prescricoes_report(start_date=None, end_date=None):
    query = """
        SELECT 
            'Relatório de Prescrições' AS tipo_relatorio,
            NOW() AS data_criacao,
            'Relatório de prescrições realizadas' AS descricao,
            GROUP_CONCAT(CONCAT('Prescrição: ', p.id, ' - Paciente: ', p.paciente_id, ' - Medicamento: ', p.medicamento_id, ' - Quantidade: ', p.quantidade) SEPARATOR '\n') AS conteudo
        FROM prescricoes p
    """
    return db_operations.execute_query(query, fetch_all=True)

def list_available_report_types():
    return ['mensal', 'anual', 'exames', 'consultas', 'tratamentos', 'medicamentos', 'prescricoes']

def list_available_report_formats():
    return ['txt', 'csv']
