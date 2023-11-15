cpf = '122.513.066-25'

cpf_valido = False

lista = cpf.split('-')

digito = lista[1]

digito1 = int(digito[0])
digito2 = int(digito[1])

del(lista[1])

aux = lista[0].split('.')

cpf_separado = ''.join(aux)

cont = 10
soma_digitos_cpf = 0

for num in cpf_separado:
    numero = int(num)
    soma_digitos_cpf = soma_digitos_cpf + (numero * cont)
    cont -= 1

soma_digitos_cpf *= 10

primeiro_digito = 0 if soma_digitos_cpf % 11 > 9 else soma_digitos_cpf%11



cpf_separado = cpf_separado + str(primeiro_digito)

cont_2 = 11
soma_digitos_cpf_completo = 0

for num in cpf_separado:
    numero = int(num)
    soma_digitos_cpf_completo = soma_digitos_cpf_completo + (numero * cont_2)
    cont_2 -= 1

soma_digitos_cpf_completo *= 10

segundo_digito = 0 if soma_digitos_cpf_completo%11 > 9 else soma_digitos_cpf_completo%11


if segundo_digito == digito2 and primeiro_digito == digito1:
    print('CPF válido')
