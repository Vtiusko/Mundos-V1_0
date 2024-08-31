'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
'''
from time import sleep
from tqdm import tqdm

print('Vamos ver se voce foi multado?\n\nSiga as instruçoes abaixo...\n')
sleep(2)
opção = int(input('''
\033[37m-----------------------------------------------------------------\033[m

\033[37m1 -\033[m Via Local (LIMITE: 30Km/h)
\033[37m2 -\033[m Via Coletora (LIMITE: 40Km/h)
\033[37m3 -\033[m Via Arterial (LIMITE: 60Km/h)
\033[37m4 -\033[m Via Transito Rapido (LIMITE: 80Km/h)
\033[37m5 -\033[m Via Dupla (LIMITE: 110Km/h)
	\033[37m- Somente para carro e moto, demais veiculos LIMITE: 90Km/h.\033[m

\033[37m-----------------------------------------------------------------\033[m

Escolha uma opção: '''))

def via_local():
	multa = (velocidade - 30) * 7
	km = velocidade - 30
	if velocidade > 30:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n> \033[31mMULTADO!!!O limite de 30Km/h em via local, foi excedido em\033[m \033[33m{:.2f}\033[m km\n\n> \033[31mO valor da multa a ser paga é de\033[m \033[33mR${:.2f}\033[m\n\n\033[37m----FIM----\033[m'.format(km, multa));
	else:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n\033[32mTudo Limpo! \nDirija sempre com segurança!\033[m\n\n\033[37m----FIM----\033[m')

def via_coletora():
	multa = (velocidade - 40) * 7
	km = velocidade - 40
	if velocidade > 40:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n> \033[31mMULTADO!!!O limite de 40Km/h em via coletora, foi excedido em\033[m \033[33m{:.2f}\033[m km\n\n> \033[31mO valor da multa a ser paga é de\033[m \033[33mR${:.2f}\033[m\n\n\033[37m----FIM----\033[m'.format(km, multa));
	else:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n\033[32mTudo Limpo! \nDirija sempre com segurança!\033[m\n\n\033[37m----FIM----\033[m')

def via_arterial():
	multa = (velocidade - 60) * 7
	km = velocidade - 60
	if velocidade > 60:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n> \033[31mMULTADO!!!O limite de 60Km/h em via arterial, foi excedido em\033[m \033[33m{:.2f}\033[m km\n\n> \033[31mO valor da multa a ser paga é de\033[m \033[33mR${:.2f}\033[m\n\n\033[37m----FIM----\033[m'.format(km, multa));
	else:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n\033[32mTudo Limpo! \nDirija sempre com segurança!\033[m\n\n\033[37m----FIM----\033[m')

def via_transito_rapido():
	multa = (velocidade - 80) * 7
	km = velocidade - 80
	if velocidade > 80:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n> \033[31mMULTADO!!!O limite de 80Km/h em via transito rápido, foi excedido em\033[m \033[33m{:.2f}\033[m km\n\n> \033[31mO valor da multa a ser paga é de\033[m \033[33mR${:.2f}\033[m\n\n\033[37m----FIM----\033[m'.format(km, multa));
	else:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n\033[32mTudo Limpo! \nDirija sempre com segurança!\033[m\n\n\033[37m----FIM----\033[m')

def demais():
	multa = (velocidade - 90) * 7
	km = velocidade - 90
	if velocidade > 90:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n> \033[31mMULTADO!!!O limite de 90Km/h em via dupla por demias veículos, foi excedido em\033[m \033[33m{:.2f}\033[m km\n\n> \033[31mO valor da multa a ser paga é de\033[m \033[33mR${:.2f}\033[m\n\n\033[37m----FIM----\033[m'.format(km, multa));
	else:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n\033[32mTudo Limpo! \nDirija sempre com segurança!\033[m\n\n\033[37m----FIM----\033[m')

def via_dupla():
	multa = (velocidade - 110) * 7
	km = velocidade - 110
	if velocidade > 110:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n> \033[31mMULTADO!!!O limite de 110Km/h em via dupla, foi excedido em\033[m \033[33m{:.2f}\033[m km\n\n> \033[31mO valor da multa a ser paga é de\033[m \033[33mR${:.2f}\033[m\n\n\033[37m----FIM----\033[m'.format(km, multa));
	else:
		print('\n\033[33mCalculando...\033[m\n')
		for i in tqdm(range(10)):
			sleep(0.2)
		print('\n\033[32mTudo Limpo! \nDirija sempre com segurança!\033[m\n\n\033[37m----FIM----\033[m')

if opção == 1:
	velocidade = float(input('\nDigite quantos \033[33mKm/h\033[m o carro estava: '))
	via_local()	
elif opção == 2:
	velocidade = float(input('\nDigite quantos \033[33mKm/h\033[m o carro estava: '))
	via_coletora()
elif opção == 3:
	velocidade = float(input('\nDigite quantos \033[33mKm/h\033[m o carro estava: '))
	via_arterial()
elif opção == 4:
	velocidade = float(input('\nDigite quantos \033[33mKm/h\033[m o carro estava: '))
	via_transito_rapido()
elif opção == 5:
	perg = int(input('\nTipos de veículos:\n\n1 - Carros e Motos\n2 - Demais Veículos\n\nEscolha uma opção [ 1 / 2 ]: '))
	if perg == 1:
		velocidade = float(input('\nDigite quantos \033[33mKm/h\033[m o carro estava: '))
		via_dupla()
	elif perg == 2:
		velocidade = float(input('\nDigite quantos \033[33mKm/h\033[m o carro estava: '))
		demais()
else:
	print('Até logo!')
