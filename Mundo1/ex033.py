'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
print('Qual número é o maior e o menor?\n')

num1 = int(input('Digite o número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite um último número: '))


# QUEM É O MENOR:
menor = num1
if num2 < num1 and num2 < num3:
	menor = num2
elif num3 < num1 and num3 < num2:
	menor = num3

# QUEM É O MAIOR:
maior = num1
if num2 > num1 and num2 > num3:
	maior = num2
elif num3 > num1 and num3 > num2:
	maior = num3

print('\nO menor número é o {},\nO maior número é o {}'.format(menor, maior))