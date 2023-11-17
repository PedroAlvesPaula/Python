# Exercicio 1

number = input('Digite um número inteiro: ')

if number.isdigit():

    number = int(number)

    if number is float:
        print('O numero digitado nao é um inteiro')

    if (number % 2) == 0:
        print(f"O numero {number} é par")
    else:
        print(f"O numero {number} é impar")
else:
    print('Não é um número inteiro')
