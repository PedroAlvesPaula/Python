name = input('Digite seu nome: ')
age = input('Digite sua idade: ')

size = len(name)

if name and age:
    print(f'seu nome é: {name}')
    print(f'Seu nome invertido é: {name[:: -1]}')

    if ' ' in name:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')

    print(f'seu nome tem {len(name)} letras')
    print(f'primeira letra do seu nome: {name[0:1]}')
    print(f'A ultima letra do seu nome é: {name[size - 1]}')
else:
    print('Voce inseriu campos vazios!')