import os

list = []

stop = False

while(stop == False):
    try:
        digitadopelousuario = input('[1] inserir, [2] apagar, [3] listar, [4] sair ')
        digitadopelousuario = int(digitadopelousuario)
    except:
        print('Digite uma opção valida')
        continue

    if digitadopelousuario == 1:
        os.system('cls')
        list.append(input('Digite o item a se inserido e tecle enter '))
        continue

    elif digitadopelousuario == 2:
        try:
            indice = input('Digite o indice a ser apagado e tecle enter:  ')
            del(list[int(indice)])
        except:
            print('índice inexistente')
            continue

    elif digitadopelousuario == 3:
        os.system('cls')
        for indice, name in enumerate(list):
            print(indice, name)
        continue

    elif digitadopelousuario == 4:
        os.system('cls')
        print('Obrigado por utilizar')
        stop = True
        continue
    else:
        print('Valor inserido inválido! Digite outra opção')

