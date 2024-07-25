#PEDIR PARA O USUARIO INFORMAR A DISTANCIA DO PERCURSO EM KM
distancia = float(input('Digite a distância do percurso em quilômetros: '))

def calcular_tempo(distancia):
    carro = 100
    aviao = 600
    onibus = 80

    tempo_carro = distancia / carro
    tempo_aviao = distancia / aviao
    tempo_onibus = distancia / onibus

    print(f'Avião: {tempo_aviao:.2f} horas')
    print(f'Carro: {tempo_carro:.2f} horas')
    print(f'Ônibus: {tempo_onibus:.2f} horas')

calcular_tempo(distancia)