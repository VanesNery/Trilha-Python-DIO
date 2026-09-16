'''Escreva um programa que receba uma string contendo várias datas no formato "DD-MM-YYYY" separadas por ponto e vírgula, e retorne uma lista de strings com as datas formatadas no estilo "YYYY/MM/DD".'''
# Recebe a entrada e armazena na variável "entrada"
entrada = input()

# Função responsável por receber as datas e transformar cada data para o formato "YYYY/MM/DD"
def transformar_datas(datas):
    # Divide a string de entrada nas datas individuais
    datas_lista = datas.split(';')
    
    datas_transformadas = []
    
    # TODO: Implemente a lógica necessária para formatar as datas
    for data in datas_lista:
        dia, mes, ano = data.split('-')
        nova_data = f"{ano}/{mes}/{dia}"
        datas_transformadas.append(nova_data)
    
    return datas_transformadas
    
# Imprime a lista de datas formatadas
print(transformar_datas(entrada))