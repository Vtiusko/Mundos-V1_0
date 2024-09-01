'''
Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
'''

frase = str(input('Quantas letras "A" tem na frase.\nDigite a frase: ')).upper().strip()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A letra "A" aparece primeiro na posição {}.'.format(frase.find('A')+1))
# o python começa contando com posição 0, pra resolver isso, foi só ter colocado "+ 1"
print('A letra "A" aparece última vez na posição {} .'.format(frase.rfind('A')+1))#começa da direita para esquerda
