produto = {
    'nome': 'Notebook', 
    'preco': 3500.00, 
    'estoque': '15'
}
print(produto)

produto.pop('estoque')

print(produto)

produto['preco'] = 4000.00
print (produto)
print(f"{produto['nome']}: R${produto['preco']}")


