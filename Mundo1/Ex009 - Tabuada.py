'''
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''

def operacao():
    num = int(input('A tabuada de qual número deverá ser mostrada: '))

    for operador in range(0, 11):
        print(f'\33[32m{num}\33[m x \33[32m{operador}\033[m = \33[32m{num * operador}\033[m')


while True:
    print('< Bem-Vindo a sua TABUADA INTERATIVA />\n')
    operacao()

    pergunta = input('\nDeseja calcular novamente [ S / N ]: ').upper()
    while (pergunta not in 'SN') or (pergunta == ''):
        print('Você deve digitar "S" ou "N"!')
        
        pergunta = input('Deseja calcular novamente [ S / N ]: ').upper()
        
    if pergunta == 'N':
        break
