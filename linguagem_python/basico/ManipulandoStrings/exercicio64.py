name = input('Digite seu nome: ')

cont = 0

new_name = ''

while cont < len(name):
    letra = name[cont]
    new_name += f'*{letra}'
    cont += 1

print(new_name)