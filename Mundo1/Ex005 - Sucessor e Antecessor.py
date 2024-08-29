'''
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
'''

print('=' * 15, 'Calucule um Sucessor & Antecessor', '=' * 15)

num = int(input('Digite um número: '))

sucessor = num + 1
antecessor = num - 1

print(f'\nAntecessor: {antecessor}\nNúmero: {num}\nSucessor: {sucessor}')
