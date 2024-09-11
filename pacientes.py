import json
import os

FILENAME = 'pacientes.json'

def load_data():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)

def create_paciente(id, nome, idade):
    data = load_data()
    data[id] = {'nome': nome, 'idade': idade}
    save_data(data)
    print("Paciente cadastrado com sucesso.")

def read_paciente(id):
    data = load_data()
    paciente = data.get(id, None)
    if paciente:
        print(f"ID: {id}, Nome: {paciente['nome']}, Idade: {paciente['idade']}")
    else:
        print("Paciente não encontrado.")

def update_paciente(id, nome=None, idade=None):
    data = load_data()
    if id in data:
        if nome:
            data[id]['nome'] = nome
        if idade:
            data[id]['idade'] = idade
        save_data(data)
        print("Paciente atualizado com sucesso.")
    else:
        print("Paciente não encontrado.")

def delete_paciente(id):
    data = load_data()
    if id in data:
        del data[id]
        save_data(data)
        print("Paciente removido com sucesso.")
    else:
        print("Paciente não encontrado.")

# Exemplo de uso
if __name__ == '__main__':
    # Testar CRUD
    create_paciente("1", "João da Silva", 30)
    read_paciente("1")
    update_paciente("1", idade=31)
    read_paciente("1")
    delete_paciente("1")
    read_paciente("1")
