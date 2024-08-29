'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Informe seu salário: R$ '))

# Podemos calcular o valor do novo salário desta maneira:
    # salario + (salario * (15 / 100))

aumento = salario * 0.15
salario_final = salario + aumento

print(f'\nSalário de R${salario:.2f} foi para R${salario_final:.2f}')
print(f'Aumento de R${aumento:.2f}')
