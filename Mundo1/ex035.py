'''
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
'''
from time import sleep
from emoji import emojize
from tqdm import tqdm

print(emojize('Verifique se as suas retas \033[37mPODEM\033[m ou \033[37mNÃO\033[m formar um triangulo\nSiga os passos abaixo:selfie:', use_aliases=True))

print('\n\n\033[32mCarregando...\033[m\n')
for i in tqdm(range(10)): 
	sleep(0.3)

r1 = float(input('\n\nDigite o valor do primeiro angulo: '))
r2 = float(input('\nDigite o valor do segundo angulo: '))
r3 = float(input('\nDigite o valor do terceiro angulo: '))


if r1 + r2 > r3 and r3 + r1 > r2 and r3 + r2 > r1:
	print('\nSuas medidas {}, {}, {},\n\033[37mPODEM\033[m formar um triangulo'.format(r1, r2, r3))
else:
	print('\nSuas medidas {}, {}, {},\n\033[31mNÃO PODEDM\033[m formar um triangulo'.format(r1, r2, r3))