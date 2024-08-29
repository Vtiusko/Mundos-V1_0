'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

Para converter uma temperatura em Celsius (°C) para Fahrenheit (°F), utilize a seguinte fórmula:
    °F = 32 + (°C x (9 / 5))
'''

print(f'{" CONVERSOR DE TEMPERATURAS °C → F° ":-^50}')

celsius = input('\nInforme quantos °C deseja converter para °F: ')

celsius = float(celsius)
fahrenheit = 32 + (celsius * (9 / 5))

print(f'{celsius}°C equivalem à {fahrenheit}°F')