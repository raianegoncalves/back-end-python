"""
- LISTAS: são listas que PODEM ter valores alterados;
lista = []
lista.append ('Maçã) - inserir mais informações na lista
print (lista)

- TUPLAS: são listas que NÃO PODEM ter valores alterados;
tupla = ('maçã', 'uva')
print(tupla)

- DICIONÁRIOS: associar valores em significados.
dicionario = {}
print(dicionario)
"""

#LISTAS
lista_frutas = [] # declarando variavél com colchetes
# como se quisesse que o usuário adicionasse na lista - aqui pedindo ao usuário
fruta = input('Digite sua fruta: ')
lista_frutas.append(fruta)
#inserindo os valores dentro do código direto
lista_frutas.append('Maçã') 
lista_frutas.append('Banana')
lista_frutas.append('Uva')
print(lista_frutas)


#TUPLAS
tupla = ('Maçã', 'Uva', 'Banana', 'Morango') #declarando variavél com parenteses.
print(tupla)


#DICIONÁRIOS
dicionario = {'Chave': 'Valor'} #declarando variavél com chaves.
dicionario ['maça'] = 'É uma fruta'
dicionario ['carro'] = 'É um veículo'
print (dicionario)