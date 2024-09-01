'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.

'''
nome = str(input('Deigite um nome, somente primeiro nome ou completo: ')).strip()

maiuscula = nome.upper() # Transforma em maiúsculas
minuscula = nome.lower() # Transforma em minúsculas
quantidade = len(nome.replace(' ', '')) # Retira os espaços entre os nomes
divisoes = nome.split() # Divide o nome em 5 palavras
quant_pri = len(divisoes[0]) # Mostra quantas letras tem o 1° nome

print('''
	\nO nome somente com 
	>>> Letras maiúsculas: \033[35m{}\033[m,
	>>> Letras minúsculas: \033[35m{}\033[m,
	>>> Nome possui: \033[35m{}\033[m caracteres,
	>>> Primeiro nome possui: \033[35m{}\033[m caracteres,
	>>> Último nome é: \033[35m{}\033[m.'''
      .format(maiuscula, minuscula, quantidade, quant_pri, divisoes[-1]))

# Esse -1 pega o último elemento da lista.

