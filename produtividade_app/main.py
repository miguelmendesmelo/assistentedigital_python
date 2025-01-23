import json
import datetime

def main_menu():
    print("\n=== ASSISTENTE DIGITAL 0.1 ===")
    print("1. Agenda")
    print("2. Bloco de Notas")
    print("3. Gerenciador de Tarefas")
    print("4. Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def agenda():
    print("\=== Agenda ===")
    eventos = carregar_dados("agenda.json")
    while True:
        print("\n1. Adicionar Evento")
        print("2. Visualizar Eventos")
        print("3. Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            evento = input("Descrição do evento: ")
            data = input("Data: ")
            hora = input("Hora: ")
            eventos.append({"evento": evento, "data": data, "hora": hora})
            salvar_dados("agenda.json", eventos)
            print("Evento adicionado!")
        elif escolha == "2":
            for e in eventos:
                print(f"{e['data']} {e['hora']} - {e['evento']}")
        elif escolha == "3":
            break
def bloco_de_notas():
    print("\n=== Bloco de Notas ===")
    notas = carregar_dados("notas.json")
    while True:
        print("\n1. Adicionar Nota")
        print("2. Visualizar Notas")
        print("3. Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            nota = input("Escreva sua nota: ")
            notas.append(nota)
            salvar_dados("notas.json", notas)
            print("Nota salva!")
        elif escolha == "2":
            for i, nota in enumerate(notas, 1):
                print(f"{i}. {nota}")
        elif escolha == "3":
            break

def task_manager():
    print("\n=== Gerenciador de Tarefas ===")
    tarefas = carregar_dados("tarefas.json")
    while True:
        print("\n1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Atualizar Status")
        print("4. Voltar")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            tarefa = input("Descrição da tarefa: ")
            tarefas.append({"tarefa": tarefa, "status": "Pendente"})
            salvar_dados("tarefas.json", tarefas)
            print("Tarefa adicionada!")
        elif escolha == "2":
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t['tarefa']} - {t['status']}")
        elif escolha == "3":
            for i, t in enumerate(tarefas, 1):
                print(f"{i}. {t['tarefa']} - {t['status']}")
            num = int(input("Escolha o número da tarefa para atualizar: ")) - 1
            if 0 <= num < len(tarefas):
                novo_status = input("Novo status (Pendente, Em Andamento, Concluída): ")
                tarefas[num]['status'] = novo_status
                salvar_dados("tarefas.json", tarefas)
                print("Status atualizado!")
        elif escolha == "4":
            break

def carregar_dados(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_dados(nome_arquivo, dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
        
if __name__ == "__main__":
    while True:
        escolha = main_menu()
        if escolha == "1":
            agenda()
        elif escolha == "2":
            bloco_de_notas()
        elif escolha == "3":
            task_manager()
        elif escolha == "4":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")