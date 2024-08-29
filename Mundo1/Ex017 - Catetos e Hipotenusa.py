'''
    ========== TEOREMA DE PITÁGORAS

    Fórmula: a² = b² + c²
    "O quadrado da hipotenusa é igual à soma dos quadrados dos catetos"

Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

# 1ª Forma - Biblioteca Math → Módulo "Hypot"
from math import hypot

print(f'{" DESCUBRA O COMPRIMENTO DA HIPOTENUSA ":=^46}\n')

co = float(input('Informe o Valor do "Cateto Oposto": '))
ca = float(input('Informe o Valor do "Cateto Adjacente": '))

print(f'\nA hipotenusa {hypot(co, ca):.1f} é igual a soma dos quadrados dos catetos {co} e {ca}!\n')


print('=' * 40)


# 2ª Forma - Criando uma variável à partir da fórmula
hipo = (co ** 2 + ca ** 2) ** (1 / 2)
print(f'\nA hipotenusa {hipo:.1f} é igual a soma dos quadrados dos catetos {co} e {ca}!\n')


