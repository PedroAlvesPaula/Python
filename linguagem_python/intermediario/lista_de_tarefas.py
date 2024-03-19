import os
import json

def salvar_em_json(lista_tarefas):
    with open('.//lista_tarefa.json', 'w') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=2)

def ler_arquivo(caminho_arquivo):
    tarefas = []
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            tarefas = json.load(arquivo)
    except:
        salvar_em_json(tarefas)

    return tarefas


def print_menu():
    print("Digite uma tarefa ou um dos comandos a seguir: desfazer, refazer, listar, clear, sair")

def listar(lista_tarefas):
    if not lista_tarefas:
        print('Nenhuma tarefa a listar')
        return
    for indice, tarefa in enumerate(lista_tarefas):
        print(f'\t {indice+1}: {tarefa}')

def desfazer(lista_tarefas, lista_tarefas_refazer):
    if not lista_tarefas:
        print("Lista vazia, nada a desfazer")
        return
    
    lista_tarefas_refazer.append(lista_tarefas.pop())

def refazer(lista_tarefas, lista_tarefas_refazer):
    if not lista_tarefas_refazer:
        print("Lista vazia, nada a refazer")
        return
    
    lista_tarefas.append(lista_tarefas_refazer.pop())

def adcionar(tarefa, lista_tarefas):
    if not tarefa.split():
        print("Nenhuma tarefa passada")
        return
    
    lista_tarefas.append(tarefa)

CAMINHO_ARQUIVO = ('lista_tarefa.json')

lista_tarefas = ler_arquivo(CAMINHO_ARQUIVO)

lista_tarefas_refazer = []

continuar = True

while continuar:
    print_menu()
    
    input_user = input()

    if input_user == 'listar':
        listar(lista_tarefas)

    elif input_user == 'desfazer':
        desfazer(lista_tarefas, lista_tarefas_refazer)
        listar(lista_tarefas)
        salvar_em_json(lista_tarefas)

    elif input_user == 'refazer':
        refazer(lista_tarefas, lista_tarefas_refazer)
        listar(lista_tarefas)
        salvar_em_json(lista_tarefas)
        
    elif input_user == 'clear':
        os.system('cls')
    elif input_user == 'sair':
        break
    else:
        adcionar(input_user, lista_tarefas)
        salvar_em_json(lista_tarefas)
