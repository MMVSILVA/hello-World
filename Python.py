#!/usr/bin/env python
# coding: utf-8

# 1-Elaborar um algoritmo que leia o nome, sexo e idade de 5 pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. Deve-se mostrar:
# 
# -O percentual de homens e mulheres no grupo;
# -Uma lista com todas os homens. Se não existirem homens no grupo, deve-se apresentar uma mensagem ao usuário;
# -Uma lista com todas as pessoas com idade acima da média.

# In[ ]:


dados1 = list()
dados = dict()

for i in range(5):
    dados['nome'] = input("Entre com um nome: ")
    dados['idade'] = int(input("Entre com a idade: "))
    dados['sexo'] = input("Entre com o sexo: ")
    dados1.append(dados.copy())
    dados.clear()
print(dados1)
print()

total_homem = 0

total_mulher = 0

for i in dados1:
    if (i['sexo'] == 'masculino') or i['sexo'] == 'Masculino':
        total_homem = total_homem+1
    if (j['sexo'] == 'feminino') or (j['sexo'] == 'Feminino'):
        total_mulher = total_mulher+1

for dosos in dados1:
    for chave,valor in dados.items():
        print(f"\nO campo {chave} tem valor {valor}.")
    print()
pctg_masc = (total_homem/5)*100

print(f'A porcentagem de homens e mulheres é respectivamente: {pctg_masc}% e {100-pctg_masc}%')

