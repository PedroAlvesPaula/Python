def imprimir_opcoes(posicao):
    print(perguntas[posicao]['Pergunta'])

    for indice, opcao in enumerate(perguntas[posicao]['Opções']):
        print(f'({indice}) {opcao}')

def verificar_resposta_usuario(posicao, resposta):
    for indice, opcao in enumerate(perguntas[posicao]['Opções']):
        if perguntas[posicao]['Opções'][resposta] == perguntas[posicao]['Resposta']:
            return True

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

continuar = True
range = 0


while continuar == True:

    opcoes = perguntas[range]['Opções']
    qtd_opcoes = len(opcoes)

    imprimir_opcoes(range)
    resposta_usuario = input("Digite o indice da opção correta: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)

        if resposta_usuario < 0 or resposta_usuario > qtd_opcoes:
            print('')
            print('Índice inválido, digite um indice mostrado')
            print('')
            continue
    else:
        print('')
        print('Digite um numero inteiro')
        print('')
        continue

    resposta_verificada = verificar_resposta_usuario(range, resposta_usuario)

    if resposta_verificada == True:
        print("Resposta correta!!")
        print('')
        range += 1

        if range == len(perguntas):
            continuar = False
        continue
    else:
        print("Resposta errada, tente novamente!")
        print('')
        continue

print("Muito bem, ate mais")
print('')
    