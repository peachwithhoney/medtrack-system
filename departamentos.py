import json
import os

FILENAME = 'departamentos.json'

def load_data():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)

def create_departamento(id, nome):
    data = load_data()
    if id in data:
        print("Departamento já existe.")
        return
    data[id] = {'nome': nome}
    save_data(data)
    print("Departamento cadastrado com sucesso.")

def read_departamento(id):
    data = load_data()
    departamento = data.get(id, None)
    if departamento:
        print(f"ID: {id}, Nome: {departamento['nome']}")
    else:
        print("Departamento não encontrado.")

def update_departamento(id, nome=None):
    data = load_data()
    if id in data:
        if nome:
            data[id]['nome'] = nome
        save_data(data)
        print("Departamento atualizado com sucesso.")
    else:
        print("Departamento não encontrado.")

def delete_departamento(id):
    data = load_data()
    if id in data:
        del data[id]
        save_data(data)
        print("Departamento removido com sucesso.")
    else:
        print("Departamento não encontrado.")

# Exemplo de uso
if __name__ == '__main__':
    # Testar CRUD
    create_departamento("1", "Emergência")
    read_departamento("1")
    update_departamento("1", "Urgência")
    read_departamento("1")
    delete_departamento("1")
    read_departamento("1")
