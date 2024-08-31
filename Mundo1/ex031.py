'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''
from time import sleep
from tqdm import tqdm

print('Cálculo de viagem')

km = float(input('\nDigite quantos Km terão a sua viagem: '))

print('\nCalculando...\n')
for i in tqdm(range(10)):
	sleep(0.2)
	
if km <= 200:
	print('\nO valor total da sua viagem será de R${:.2f}\n'.format(km * 0.5))
else:
	print('nO valor total da sua viagem será de R${:.2f}\n'.format(km * 0.45))
print('\n-------fim-------'.upper())
