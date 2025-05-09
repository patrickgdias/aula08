aluno = {
    'Nome': 'Maria', 
    'Idade': '29', 
    'curso': 'analista de dados'

}

print(aluno)
aluno['nome'] = 'Pedro'
aluno ['E-mail'] = 'pedro@gmail.com'
print (aluno)

if 'tel' in aluno:
    aluno.pop('E-mail')

print(aluno)

# aluno.clear


for chave, valor in aluno.items():
    print(chave)

for chave, valor in aluno.values():
    print(chave)

for chave, valor in aluno.keys():


