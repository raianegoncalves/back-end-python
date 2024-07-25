def divisao(a,b):
    try:
        resultado = a/b
        print(resultado)
        #para mostrar que não se pode dividir um numero por zero
    except ZeroDivisionError:
        print('Erro: impossivel dividir um valor por zero')
    except TypeError as e: #o 'e' vai trazer aonde está o erro
        print(f'Erro: o tipo de dado está incorreto. Detalhes: {e}')
    else:
        print('Sem exceções')

#divisao (10, 0)
divisao (10, 'oi')