'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude, lendo o nome deles e escrevendo o nome do escolhido
'''
from random import choice
from time import sleep
from emoji import emojize
from tqdm import tqdm

print('*'*50, '\n\033[33mSorteie dentre\033[m \033[32m4 alunos\033[m\033[33m, quem vai apagar o quadro!\033[m\n\n')

def sortear_aluno():
	n1 = input('Digite o nome do \033[33m1°\033[m aluno: ')
	n2 = input('\nDigite o nome do \033[33m2°\033[m aluno: ')
	n3 = input('\nDigite o nome do \033[33m3°\033[m aluno: ')
	n4 = input('\nDigite o nome do 4° aluno: ')
	nomes = [n1, n2, n3, n4]
	print(' ')
	print('*'*50 + '\n\n\033[32mEMBARALHANDO NOMES...\033[m\n\n' + '*'*50)
	for i in tqdm(range(10)):
		sleep(1)
	print('\nO aluno escolhido é o \033[33m{}\033[m'.format(choice(nomes)))

while True:
	sortear_aluno()
	sleep(1)
	perg = input('\nDeseja sortear novamente \033[33m[ S / N ]\033[m: ').upper().strip()
	print(' ')
	print('*'*50 + '\n\n   \033[32mLOADING...\033[m\n\n' + '*'*50)
	sleep(2)
	while (len(perg) != 1) or (perg not in 'SN'):
		sleep(0.7)
		print(emojize('\n\033[31mDigite algo válido\033[m :rage:', use_aliases=True))
		sleep(0.9)
		perg = input('\nDeseja sortear novamente \033[33m[ S / N ]\033[m: ').upper().strip()
		print('*'*50 + '\n\n   \033[32mLOADING...\033[m\n\n' + '*'*50)
		sleep(3)
	if perg == 'N':
		break
