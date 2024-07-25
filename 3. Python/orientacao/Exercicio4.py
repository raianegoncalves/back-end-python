#PEDIR AO USUÁRIO PARA INFORMAR A DISTANCIA PERCORRIDA E A QUANTIDADE DE COMBUSTIVEL CONSUMIDO
distancia = float(input('Digite a distância percorrida em quilômetro: '))
combustivel = float(input('Digite a quantidade de combustivel consumido em litros: '))

def calcular_consumo_medio(distancia, combustivel):
    media = distancia / combustivel
    print(f'O consumo médio é {media:.2f} km/l')

calcular_consumo_medio(distancia, combustivel)