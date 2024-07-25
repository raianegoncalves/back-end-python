"""ESTRUTURA CONDICIONAL:
- IF e ELSE;
- WHILE: se a condição for verdadeira, está condição será executada;
- FOR: para cada maçã na lista de frutas, será executada essa condição;
"""
#IF e ELSE

numero = int(input('Digite seu numero: '))
if numero > 0:
    print ('Numero é positivo!')
else:
    print ('Numero é negativo!')


# WHILE - enquanto
numero = -1 #estamos iniciando uma variável com -1
while numero <0:
    numero = int(input('Digite seu numero: '))
 print ('Numero positivo inserido com sucesso!')


# FOR - "para cada" - for maçã in frutas:
frutas = ['Maçã', 'Banana', 'Uva'] #declarando uma lista com os colchetes.
for fruta in frutas:
    print(fruta)

