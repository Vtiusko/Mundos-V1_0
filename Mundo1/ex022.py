'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
	- O nome com todas as letras maiúsculas;
	- o nome com todas as letras minúsculas;
	- Quantas letras ao todo(sem cosiderar espaços);
	- Quantas letras tem o primeiro nome.
	- Mostre somente o último nome
'''
nome = str(input('Deigite um nome, somente primeiro nome ou completo: ')).strip()

maiuscula = nome.upper() # Transforma em maiúsculas
minuscula = nome.lower() # Transforma em minúsculas
quantidade = len(nome.replace(' ', '')) # Retira os espaços entre os nomes
divisoes = nome.split() # Divide o nome em 5 palavras
quant_pri = len(divisoes[0]) # Mostra quantas letras tem o 1° nome

print('''\nO nome somente com 

as letras maiúsculas: \033[35m{}\033[m,
as letras minúsculas: \033[35m{}\033[m,
o nome possui: \033[35m{}\033[m caracteres,
o primeiro nome possui: \033[35m{}\033[m caracteres,
o último nome é: \033[35m{}\033[m.'''.format(maiuscula, minuscula, quantidade, quant_pri, divisoes[-1]))

# Esse -1 pega o último elemento da lista.

