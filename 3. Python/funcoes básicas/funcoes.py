"""FUNÇÕES: grupo de de instruções relacionadas que executa uma tarefa
- declaração:
def mostrar_mensagem(): #instruções ficam dentro da função
- chamada da função:
mostrar_mensagem()
"""
def soma(num1, num2): #definição da função soma
    calculo = num1 + num2
    print(f'O resultado da soma é: {calculo}')

def subtracao(num1, num2): 
    sub = num1 - num2
    print(f'O resultado da subtracao é: {sub}')

def multiplicacao(num1, num2): 
    multi = num1 * num2
    print(f'O resultado da multiplicacao é: {multi}')


# PARAMETROS (colcoar dentro dos parenteses de cada funçao para chamar os numeros digitados pelo usuario para cada def)
num1 = int(input('Digite o primeiro número: ')) 
num2 = int(input('Digite o segundo número: '))
#chamada da função
soma(num1, num2) 
subtracao(num1, num2)
multiplicacao(num1, num2)