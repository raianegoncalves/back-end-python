# mensagens iniciais para usúario.
'''
INT = 1, 5, 20, 2000, 400
FLOAT 1.5, 5.2, 2000.4
STRING 'ISADORA', 'WOMAKERSCODE'
BOOL TRUE, FALSE
'''
print ('Olá, mundo')

# TIPO INTEIRO - INT

numero = int(input('Digite seu número: '))
print(numero)

#TIPO COM VIRGULA - FLOAT

numero = float(input('Digite um numero float: '))
print (numero)

# TIPO TEXTUAL - STRING

frase = input('Digite sua frase: ')
print (frase)

# OPERAÇÕES MATEMÁTICAS

# SOMA = +

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
print(soma)

# SUBTRAÇÃO = 1

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

subtracao = numero1 - numero2
print(subtracao)

# MULTIPLICAÇÃO = *

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

multiplicacao = numero1 * numero2
print(multiplicacao)

# DIVISÃO = /

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

divisao = numero1/numero2
print(divisao)

# DIVISÃO INTEIRA = //

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

divisao = numero1//numero2
print(divisao)


# RESTO %
# INREMENTO: somar
valor = 5
valor +=1
print(valor)

# DECREMENTO: subtrair
valor = 5
valor -=1
print(valor)

#ORDEM DE PRECEDÊNCIA
calculo = (2+5)*5
print(calculo)

#OPERADORES RELACIONAIS
# ==: igual
5==5

# >: maior
5 > 5

# >=: maior ou igual
5 >= 5
# <: menor
5 < 5

# <=: menor ou igual
5 <= 5

# !=: diferente
5 != 5

# FORMATAÇÃO DE ENSAGENS
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

soma = numero1 + numero2
print(f'a soma dos números digitados é {soma}')

# str.format = f. o 2f é a quantidade de casas decimais.
valor = 45.00
print (f'{valor:.2f}')

print('Olá {}, você tem {} anos'. format ('Raiane', 28))