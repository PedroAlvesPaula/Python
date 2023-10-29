name = input('Digite o seu primeiro nome: ')

size_name = len(name)

if size_name > 0 and size_name <= 4:
    print('Seu nome é curto')
elif size_name > 4 and size_name <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')