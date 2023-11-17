import os

list = []

stop = False

while(stop == False):
    try:
        digitadopelousuario = input('[1] inserir, [2] apagar, [3] listar, [4] sair ')
        digitadopelousuario = int(digitadopelousuario)
    except:
        print('Digite uma opção valida')

    if digitadopelousuario == 1:
        os.system('cls')
        list.append(input('Digite o item a se inserido e tecle enter '))

    elif digitadopelousuario == 2:
        try:
            indice = input('Digite o indice a ser apagado e tecle enter:  ')
            del(list[int(indice)])
        except:
            print('índice inexistente')

    elif digitadopelousuario == 3:
        os.system('cls')
        for indice, name in enumerate(list):
            print(indice, name)

    elif digitadopelousuario == 4:
        os.system('cls')
        print('Obrigado por utilizar')
        stop = True

    else:
        print('Valor inserido inválido! Digite outra opção')

