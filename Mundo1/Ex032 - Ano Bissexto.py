'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto. Nesta aula vamos pegar o ano atual também.
'''
from datetime import date
from tqdm import tqdm
from time import sleep


ano = int(input('°'*40+'\n\nInforme o ano que deseja saber\n\nSe é bissexto ou não.\n\nPara saber do ano atual digite \033[37m0\033[m\n\n'+'°'*40+'\n\nInforme o ano: '))

print('\n\033[32mAnalisando...\033[m')
for i in range(10):
	sleep(0.2)

if ano == 0:
	ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('\nO ano {} é BISSEXTO'.format(ano))
else:
	print('\nO ano {} \033[37mNÃO\033[m é BISSEXTO'.format(ano))
