def salvar_em_json(lista_tarefas):
    with open('.//lista_tarefa.json', 'w') as arquivo:
        json.dump(lista_tarefas, arquivo, indent=2)