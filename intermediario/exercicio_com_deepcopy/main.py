import copy

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in produtos
]

produtos_ordenados_por_nome = sorted(copy.deepcopy(produtos), key=lambda p: p['nome'], reverse=True)


produtos_ordenados_por_preco = sorted(copy.deepcopy(produtos), key=lambda p: p['preco'])

print('Lista original: ')
print(*produtos, sep='\n')

print()

print('Lista ordenada por nome decrescente: ')
print(*produtos_ordenados_por_nome, sep='\n')

print()

print('Lista ordenada por preco: ')
print(*produtos_ordenados_por_preco, sep='\n')


