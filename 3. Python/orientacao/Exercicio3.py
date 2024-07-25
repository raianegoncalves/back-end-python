#SOLICITAR AO USUÁRIO PARA INFORMAR A QUANTIDADE DE KM
km = float(input('Digite a quantidade de quilômetros: '))

def converter_km (km):
    metros = km * 1000
    centi = km * 100000
    mili = km * 1000000

    #RESULTADOS
    print(f'KM em metros: {metros}')
    print(f'KM em centímetros: {centi}')
    print(f'KM em milímetros: {mili}')

#CHAMAR FUNÇÃO
converter_km(km)