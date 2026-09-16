'''Separando domínios de emails em Python'''
'''O desafio é receber uma string contendo uma lista de emails separados por ponto e vírgula, extrair os domínios dos emails e retornar uma lista de strings com os domínios.'''
# Recebe a entrada e armazena na variável "entrada"
entrada = input()

# Função reponsável por extrair os domínios dos emails
def extrair_dominios(emails):
    # Separa os emails por ponto e vírgula
    lista_emails = emails.split(';')
    
    # TODO: Implemente a lógica necessária para extrair os domínios
    dominios = []
    for email in lista_emails:
        dominio = email.split('@')[1]
        dominios.append(dominio)
    return dominios

# Imprime a lista de strings com os domínios
print(extrair_dominios(entrada))