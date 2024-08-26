import db_operations
import logging
from werkzeug.security import generate_password_hash

def cadastrar_usuario(nome, email, senha, tipo_usuario, status='ativo'):
    senha_hash = generate_password_hash(senha)
    query = '''
        INSERT INTO usuarios (nome, email, senha, tipo_usuario, status)
        VALUES (%s, %s, %s, %s, %s)
    '''
    values = (nome, email, senha_hash, tipo_usuario, status)
    try:
        usuario_id = db_operations.execute_query(query, values, fetch_lastrowid=True)
        return usuario_id
    except Exception as e:
        logging.error(f"Erro ao cadastrar usuário: {e}")
        return None

def cadastrar_profissional(tipo, nome, identificador, cpf, especialidade_id, telefone, email, usuario_id):
    query = f'''
        INSERT INTO {tipo} (nome, identificador, cpf, especialidade_id, telefone, email, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    values = (nome, identificador, cpf, especialidade_id, telefone, email, usuario_id)
    try:
        db_operations.execute_query(query, values)
    except Exception as e:
        logging.error(f"Erro ao cadastrar {tipo}: {e}")

def cadastrar_medico(nome, crm, cpf, especialidade_id, telefone, email, usuario_id):
    cadastrar_profissional('medicos', nome, crm, cpf, especialidade_id, telefone, email, usuario_id)

def cadastrar_enfermeiro(nome, coren, cpf, especialidade_id, telefone, email, usuario_id):
    cadastrar_profissional('enfermeiros', nome, coren, cpf, especialidade_id, telefone, email, usuario_id)

def cadastrar_paciente(nome, data_nascimento, cpf, endereco, telefone, email, usuario_id):
    query = '''
        INSERT INTO pacientes (nome, data_nascimento, cpf, endereco, telefone, email, usuario_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    values = (nome, data_nascimento, cpf, endereco, telefone, email, usuario_id)
    try:
        db_operations.execute_query(query, values)
    except Exception as e:
        logging.error(f"Erro ao cadastrar paciente: {e}")

def cadastrar_administrador(nome, email, senha):
    return cadastrar_usuario(nome, email, senha, tipo_usuario=1)

def deletar_usuario(usuario_id, admin_id):
    query_admin = '''
        SELECT tipo_usuario FROM usuarios WHERE id = %s
    '''
    try:
        tipo_usuario = db_operations.execute_query(query_admin, (admin_id,), fetch_one=True)
        if tipo_usuario and tipo_usuario['tipo_usuario'] == 1:
            query_delete = '''
                DELETE FROM usuarios WHERE id = %s
            '''
            db_operations.execute_query(query_delete, (usuario_id,))
        else:
            logging.warning("Permissão negada: usuário não é administrador.")
            return False
    except Exception as e:
        logging.error(f"Erro ao deletar usuário: {e}")
        return False
    return True
