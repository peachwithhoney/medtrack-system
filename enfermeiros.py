import json
import os

FILENAME = 'enfermeiros.json'

def load_data():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)

def create_enfermeiro(id, nome, departamento_id=None, paciente_ids=None):
    data = load_data()
    paciente_ids = paciente_ids or []
    data[id] = {'nome': nome, 'departamento_id': departamento_id, 'paciente_ids': paciente_ids}
    save_data(data)
    print("Enfermeiro cadastrado com sucesso.")

def read_enfermeiro(id):
    data = load_data()
    enfermeiro = data.get(id, None)
    if enfermeiro:
        print(f"ID: {id}, Nome: {enfermeiro['nome']}, Departamento ID: {enfermeiro['departamento_id']}, Pacientes IDs: {enfermeiro['paciente_ids']}")
    else:
        print("Enfermeiro não encontrado.")

def update_enfermeiro(id, nome=None, departamento_id=None, paciente_ids=None):
    data = load_data()
    if id in data:
        if nome:
            data[id]['nome'] = nome
        if departamento_id:
            data[id]['departamento_id'] = departamento_id
        if paciente_ids:
            data[id]['paciente_ids'] = paciente_ids
        save_data(data)
        print("Enfermeiro atualizado com sucesso.")
    else:
        print("Enfermeiro não encontrado.")

def delete_enfermeiro(id):
    data = load_data()
    if id in data:
        del data[id]
        save_data(data)
        print("Enfermeiro removido com sucesso.")
    else:
        print("Enfermeiro não encontrado.")

# Exemplo de uso
if __name__ == '__main__':
    # Testar CRUD
    create_enfermeiro("1", "Maria", departamento_id="2", paciente_ids=["3", "4"])
    read_enfermeiro("1")
    update_enfermeiro("1", paciente_ids=["5", "6"])
    read_enfermeiro("1")
    delete_enfermeiro("1")
    read_enfermeiro("1")
