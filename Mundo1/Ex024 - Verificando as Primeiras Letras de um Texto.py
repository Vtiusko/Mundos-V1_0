'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”
'''
from time import sleep

cidade = str(input('Digite o nome da cidade onde eu nasci: ').strip().title())

print('Eu nasci ai?...')
sleep(1)
print(cidade[:5] == 'Santo') #1° Forma
print('Santo' in cidade) #2° Forma
