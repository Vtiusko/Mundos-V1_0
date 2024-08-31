'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

    → Primeiro, convertemos para radiano e depois para uma das três opções.
'''
from math import sin, cos,tan, radians, ceil
from time import sleep
from emoji import emojize


while True:
    texto1 = ' CONVERSOR: SENO, COSSENO E TANGENTE '
    texto2 = ' (\033[32mRADIANO\033[m) '
    print(f'{texto1:=^45}\n{texto2:-^53}\n')

    sleep(0.6)

    angulo = float(input('\033[32m>>>\033[m Digite um ângulo de \033[32m0°\033[m à \033[32m360°\033[m: '))
    opcoes = input('\nOpções de Conversão:\n\n\033[32m1\033[m - SENO\n\033[32m2\033[m - COSSENO\n\033[32m3\033[m - TANGENTE\n\nEscolha: ')

            
    while (len(opcoes) != 1) or (opcoes not in '123'):
        sleep(0.6)
        print(emojize('\n\033[31mDigie alguma opção válida:cursing_face:!\033[m', use_aliases=True))
        sleep(1)
        
        opcoes = input('\nOpções de Conversão:\n\n\033[32m1\033[m - SENO\n\033[32m2\033[m - COSSENO\n\033[32m3\033[m TANGENTE\nEscolha: ')
   
    opcoes = int(opcoes)

    if opcoes == 1:
        print(f'\n\033[32m>>>\033[m O SENO de \033[32m{angulo}\033[m é igual à: \033[32m{sin(radians(angulo)):.2f}\033[m ou \033[32m{ceil(sin(radians(angulo)))}\033[m')
    elif opcoes == 2:
        print(f'\n\033[32m>>>\033[m O COSSENO de \033[32m{angulo}\033[m é igual à: \033[32m{cos(radians(angulo)):.2f}\033[m ou \033[32m{ceil(cos(radians(angulo)))}\033[m')
    elif opcoes == 3:
        print(f'\n\033[32m>>>\033[m A TANGENTE de \033[32m{angulo}\033[m é igual à: \033[32m{tan(radians(angulo)):.2f}\033[m ou \033[32m{ceil(tan(radians(angulo)))}\033[m')

    pergunta = input('\nDeseja calcular novamente [ S / N ]: ').upper()
    while pergunta not in 'SN' or pergunta == '':
        print('Você deve digitar "S" ou "N"!')

        pergunta = input('\nDeseja calcular novamente [ \033[mS\033[32m / \033[mN\033[32m ]: ').upper()

    if pergunta == 'N':
        print('\nAté mais!')
        break
    else:
        print('\n')
