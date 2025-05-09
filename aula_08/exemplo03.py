# Cadastro
def cadastra_pessoa(num):
    for i in range(num):
        nome = input('Informe o nome do vendedor: ')
        valor = float(input('Informe o valor da venda: '))
        
        pessoa = {
            'Nome': nome,
            'Valor': valor
        }

        lst_cadastro.append(pessoa)

# MEDIA E TOTAL
def calcula_total_media():
    tot = 0
    for pessoa in lst_cadastro:
        tot += pessoa['Valor']

    med = tot/len(lst_cadastro)
    return tot, med

# BUSCA MAIOR VENDA E VENDEDOR
def busca_maior():
    maior = 0
    vendedor = ''
    for v in lst_cadastro:
        if v['Valor'] > maior:
            maior = v['Valor']
            vendedor = v['Nome']
        
    return maior, vendedor


def buscar_vendedor(nome):
    resposta = ''
    vl = 0

    for cadastro in lst_cadastro:
        if cadastro['Nome'] == nome:
            resposta = cadastro['Nome']
            vl = cadastro['Valor']
            return resposta, vl
    return resposta, vl

#  EXEMPLO 01 - CADASTRA FUNCIONARIOS
lst_cadastro = []

qtd = int(input('Quantas pessoas? '))
cadastra_pessoa(qtd)
print(lst_cadastro)


# CALCULA TOTAL E MEDIA
total, media = calcula_total_media()
print(30* '=')
print(f'Total: {total}')
print(f'Media: {media}')

#EXEMPLO 03 - MAIOR VALOR E VENDEDOR
maior_venda, maior_vendedor = busca_maior()
print (30 * '=')
print(f'Maior venda: {maior_venda}')
print(f'Nome do Vendedor: {maior_vendedor}')

#EXEMPLO 04 - BUSCA VENDEDOR
vendedor = input('Informe o nome do vendedor: ')
nome_vendedor, valor = buscar_vendedor(vendedor)

if nome_vendedor:
    print(f' O vendedor {nome_vendedor} está presente')
else:
    print(f'{nome_vendedor} não encontrado')

