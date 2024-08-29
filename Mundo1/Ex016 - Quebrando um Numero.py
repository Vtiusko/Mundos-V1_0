'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

    Digite um número: "6.137"
    O número tem a parte inteira: "6"

'''

# 1ª Forma - Importando a biblioteca "math"
from math import trunc

print(f'{" PEGANDO A PARTE INTEIRA ":=^40}')
num1 = float(input('\nDigite um número qualquer: '))

print(f'A parte inteira de {num1} é: {trunc(num1)}\n')


print('=' * 40)


# 2ª Forma - Convertendo o tipo do valor
num2 = float(input('\nDigite um outro número qualquer: '))
print(f'\nA parte inteira de {num2} é: {int(num2)}')
