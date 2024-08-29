'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

def calculo_escolar():
    nota1 = float(input('Digite a nota do 1º trimestre: '))
    nota2 = float(input('Digite a nota do 2º trimestre: '))
    nota3 = float(input('Digite a nota do 3º trimestre: '))
    nota4 = float(input('Digite a nota do 4º trimestre: '))

    media = float(nota1 + nota2 + nota3 + nota4) / 4

    return media

while True:
    print('-' * 10, 'CÁLCULO DE MÉDIA ESCOLAR', '-' * 10)

    media = calculo_escolar()

    if 0 < media <= 2.9:
        msg = f'{media:.1f} (PÉSSIMO). Você assistiu às aulas mesmos?'
    elif 3 <= media <= 4.9:
        msg = f'{media:.1f} (RUIM). Você tem que estudar mais!'
    elif 5 <= media <= 5.9:
        msg = f'{media:.1f} (REGULAR), passou raspando hein!'
    elif 6 <= media <= 8.9:
        msg = f'{media:.1f} (BOA), você passou!'
    elif 9 <= media <= 10:
        msg = f'{media:.1f} (EXCÊLENTE). Seus esforços valeram a pena, parabéns!'
    else:
        print('[  T_T]')
        
    print(f'\nSua nota foi: {msg}')

    pergunta = input('Deseja continuar [ S / N ]: ').upper()[0]
    while pergunta not in ['S', 'N']:
        print('\nVocê deve digitar "S" ou "N".')
        
        pergunta = input('Deseja continuar [ S / N ]: ').upper()[0]

    if pergunta == 'N':
        break

