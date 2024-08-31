'''
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from tqdm import tqdm
from time import sleep
from random import randint

num = int(input('''
\033[33m--------------------------\033[m

\033[37mPensei num número de\033[m \033[33m0\33[m \033[37mà\033[m \033[33m5\033[m,
\033[37mTente advinhar qual é...\033[m

\033[33m--------------------------\033[m
\033[37mQual o número: \033[m'''))

n = randint(0, 5)
def sortear():
	if num == n:
		print('''
\033[33mUau\033[m. \033[37mSua mente é de uma máquina?
Eu pensei no número\033[m \033[33m{}\033[m\n'''.format(n))
	else:
		print('''
\033[33mEu ganhei\033[m! \033[37mHAHAHA ...
Faltam anos luzes pra vc me superar! 
Eu pensei no número\033[m \033[33m{}\033[m\n'''.format(n))

print('\n\033[33mA n a l i s a n d o...\033[m')
for i in tqdm(range(10)):
	sleep(0.32)
sortear()
