'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Qual o valor do seu salário: R$'))

aumento1 = salario + (salario * 0.1) # Aumento de 10%
aumento2 = salario + (salario * 0.15) # Aumento de 15%

if salario <= 1250:
	print('O seu salário de \033[32mR${}\033[m, teve um aumento de 15%,\nPassou a ser: \033[32mR${}\033[m'.format(salario, aumento2))
elif salario > 1250:
	print('O seu salário de \033[32mR${}\033[m, teve um aumento de 10%,\nPassou a ser: \033[32mR${}\033[m'.format(salario, aumento1))
