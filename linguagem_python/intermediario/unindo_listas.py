lista2 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista1 = ['BA', 'SP', 'MG', 'RJ']
# def zipper(lista1, lista2):

#     lista_de_tuplas = []
#     i = 0

#     if len(lista1) < len(lista2):
#         for item in lista1:
#             tupla = (item, lista2[i])
#             lista_de_tuplas.append(tupla)
#             i += 1

#         return lista_de_tuplas
#     else:
#         for item in lista2:
#             tupla = (item, lista1[i])
#             lista_de_tuplas.append(tupla)
#             i += 1

#         return lista_de_tuplas
        

# lista_uniao = zipper(lista1, lista2)

# print(lista_uniao)

### OU

uniao_listas = (list(zip(lista1, lista2)))

print(uniao_listas)
