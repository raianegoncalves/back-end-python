# PEDIR DOIS NUMEROS AO USUÁRIO PARA REALIZAR OPERAÇÕES MATEMÁTICAS
def soma(num1, num2):
    calculo = num1 + num2
    print(f'O resultado da soma é: {calculo}')

def subtracao(num1, num2):
    sub = num1 - num2
    print(f'O resultado da subtração é: {sub}')

def multiplicacao(num1, num2):
    multi = num1 * num2
    print(f'O resultado da multiplicação é: {multi}')

def divisao(num1, num2):
    div = num1 // num2
    print(f'O resultado da divisão é: {div}')

# PEDIR AO USUÁRIO FINAL PARA ENTRAR COM NUMEROS
num1 = int(input('Digite o primeiro número: ')) 
num2 = int(input('Digite o segundo número: '))

#CHAMADA DE CADA FUNÇÃO
soma(num1, num2) 
subtracao(num1, num2)
multiplicacao(num1, num2)
divisao(num1, num2)