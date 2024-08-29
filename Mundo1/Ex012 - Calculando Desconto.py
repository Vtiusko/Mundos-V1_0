'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
print(f'{" DESCONTASSO ":=^38}\n')

valor = float(input('Informe o preço do produto,\nE ganhe 5% de desconto: R$ '))


# Tem duas formas de calcular a porcentagem:
    # valor * 5 / 100 
    # valor * 0.05
desconto = valor * 0.05
valor_final = valor - desconto

print(f'\nDe R${valor:.2f} foi para R${valor_final:.2f}')
print(f'Desconto de R${desconto:.2f}')