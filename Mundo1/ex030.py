'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

% = Volta o resto da divisão, o que sobra
// = Volta o que fica abaixo da chave
'''
print('O número é ímpar ou par?\n')
num = int(input('Digite um número: '))
if num % 2 == 0: # Se o resto da divisão por dois for igual a 0
	print('O número {} é par'.format(num))
else:
	print('O número {} é ímpar'.format(num))