#MANIPULAÇÃO DE ARQUIVOS

def multiplicacao():
    multi = 10*2
    file = 'arquivo.txt'

    #open somente para escrita
    arquivo_escrita = open(file, "w") 
    arquivo_escrita.write("Texto a ser escrito")
    arquivo_escrita.close() #fechar a escrita

    #open para leitura
    arquivo_leitura = open(file, "r") 
    leitura = arquivo_leitura.read()
    print(leitura)
    arquivo_leitura.close() #fechar a leitura  

    #open para aquivos binários
    #arquivo_binario = open(file, "wb") 

multiplicacao() #chamada da função