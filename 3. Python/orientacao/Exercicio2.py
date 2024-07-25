# Solicita ao usuário que informe o ano de nascimento
ano = int(input('Digite o ano do seu nascimento em YYYY: ')) 

def calcular_idade(ano):
    ano_atual = 2024
    idade = ano_atual - ano 
    print(f'Sua idade é: {idade} anos')

# Chama a função para calcular a idade
calcular_idade(ano)
