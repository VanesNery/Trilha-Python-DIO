'''Escreva um programa que receba uma lista de temperaturas em Celsius, converta cada temperatura para Fahrenheit e imprima a lista resultante. A fórmula para converter Celsius para Fahrenheit é: F = (C * 9/5) + 32.'''
# Recebe a entrada do usuário como uma string e divide essa string nos caracteres ',' (vírgula),
temperaturas_celsius = input().split(',')

# função chamada converter_celsius_para_fahrenheit que recebe uma lista de strings
def converter_celsius_para_fahrenheit(temperaturas_celsius):
    temperaturas_celsius = [float(temp) for temp in temperaturas_celsius]
    
    # TODO: Calcule as temperaturas em Fahrenheit para cada temperatura em Celsius convertida para float
    temperaturas_fahrenheit = []
    for tc in temperaturas_celsius:
        tf = (tc * 9/5)+32
        temperaturas_fahrenheit.append(tf)
    
    return temperaturas_fahrenheit

# Imprime o resultado das temperaturas convertidas para Fahrenheit.
print(converter_celsius_para_fahrenheit(temperaturas_celsius))
