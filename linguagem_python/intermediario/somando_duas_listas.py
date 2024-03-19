lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma_listas(lista1, lista2):
    return[x + y for x, y in zip(lista1, lista2)]

resultado_soma_lista = soma_listas(lista_a, lista_b)

print(resultado_soma_lista)