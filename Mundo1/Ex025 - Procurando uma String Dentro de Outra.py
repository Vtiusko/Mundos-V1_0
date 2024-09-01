'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
'''

nome = str(input('Verifique se tem "Silva" em seu nome e em qual microespaço está localizado, digite seu nome completo.\n\nDigite seu nome: ')).strip().title()

print('\nTem silva no nome: {}'.format('Silva' in nome))

n = nome.replace(' ', '')

print(f'\nSilva começa à partir do microespaço {n.find("Silva")}')
