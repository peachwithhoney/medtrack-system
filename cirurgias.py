import json
import os

FILENAME = 'cirurgias.json'

def load_data():
    if not os.path.exists(FILENAME):
        return {}
    with open(FILENAME, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(FILENAME, 'w') as file:
        json.dump(data, file, indent=4)

def create_cirurgia(id, paciente_id, medico_id, descricao, observacoes):
    data = load_data()
    data[id] = {'paciente_id': paciente_id, 'medico_id': medico_id, 'descricao': descricao, 'observacoes': observacoes}
    save_data(data)
    print("Cirurgia registrada com sucesso.")

def read_cirurgia(id):
    data = load_data()
    cirurgia = data.get(id, None)
    if cirurgia:
        print(f"ID: {id}, Paciente ID: {cirurgia['paciente_id']}, Médico ID: {cirurgia['medico_id']}, Descrição: {cirurgia['descricao']}, Observações: {cirurgia['observacoes']}")
    else:
        print("Cirurgia não encontrada.")

def update_cirurgia(id, paciente_id=None, medico_id=None, descricao=None, observacoes=None):
    data = load_data()
    if id in data:
        if paciente_id:
            data[id]['paciente_id'] = paciente_id
        if medico_id:
            data[id]['medico_id'] = medico_id
        if descricao:
            data[id]['descricao'] = descricao
        if observacoes:
            data[id]['observacoes'] = observacoes
        save_data(data)
        print("Cirurgia atualizada com sucesso.")
    else:
        print("Cirurgia não encontrada.")

def delete_cirurgia(id):
    data = load_data()
    if id in data:
        del data[id]
        save_data(data)
        print("Cirurgia removida com sucesso.")
    else:
        print("Cirurgia não encontrada.")

# Exemplo de uso
if __name__ == '__main__':
    # Testar CRUD
    create_cirurgia("1", "2", "3", "Apendicectomia", "Sem complicações")
    read_cirurgia("1")
    update_cirurgia("1", observacoes="Paciente se recuperando bem")
    read_cirurgia("1")
    delete_cirurgia("1")
    read_cirurgia("1")
