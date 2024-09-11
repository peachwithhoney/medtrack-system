import json
import os

FILENAME = 'medicos.json'

def load_data():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)

def create_medico(id, nome, especialidade):
    data = load_data()
    data[id] = {'nome': nome, 'especialidade': especialidade}
    save_data(data)
    print("Médico cadastrado com sucesso.")

def read_medico(id):
    data = load_data()
    medico = data.get(id, None)
    if medico:
        print(f"ID: {id}, Nome: {medico['nome']}, Especialidade: {medico['especialidade']}")
    else:
        print("Médico não encontrado.")

def update_medico(id, nome=None, especialidade=None):
    data = load_data()
    if id in data:
        if nome:
            data[id]['nome'] = nome
        if especialidade:
            data[id]['especialidade'] = especialidade
        save_data(data)
        print("Médico atualizado com sucesso.")
    else:
        print("Médico não encontrado.")

def delete_medico(id):
    data = load_data()
    if id in data:
        del data[id]
        save_data(data)
        print("Médico removido com sucesso.")
    else:
        print("Médico não encontrado.")

# Exemplo de uso
if __name__ == '__main__':
    # Testar CRUD
    create_medico("1", "Dr. Ana", "Cardiologia")
    read_medico("1")
    update_medico("1", especialidade="Neurologia")
    read_medico("1")
    delete_medico("1")
    read_medico("1")
