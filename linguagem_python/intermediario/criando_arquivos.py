caminho_arquivo = '.\\arquivo'

continuar = 'a'

while (continuar != '@'):

    continuar = input("Digite '@' para para parar ou qualquer tecla para continuar: ")

    item = input("Digite o item a ser adcionado: ")

    with open(caminho_arquivo, 'a', encoding='utf-8')as arquivo:
        arquivo.write(f'{item}\n')

print('Itens adcionados: ')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())