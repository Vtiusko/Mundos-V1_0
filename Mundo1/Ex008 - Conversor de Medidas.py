'''
Crie um programa que exiba um valor em "Metros" e converta para "Centímetros" e "Milímetros".
'''

print('Conversor de Metros - Centímetros - Milímetros\n\nOlá Bem-Vindo ao: Conversor de Medidas!\n\n')

opcao = int(input('-' * 5, 'OPÇÕES DE MEDIDAS', '-' * 5, '\n\n1 - Metros\n2 - Centímetros\n3 - Milímetros\n\nSelecione a medida: '))
quantidade = float(input('\Informe a quantidade a ser convertida: '))

if opcao == 1:
    print(f'\nSua quantidade equivale à {quantidade}m')
elif opcao == 2:
    print(f'\nSua quantidade equivale à {quantidade}cm')
elif opcao == 3:
    print(f'\nSua quantidade equivale à {quantidade}mm')

conversao = int(input('-' * 5, 'OPÇÕES DE CONVERSÕES', '-' * 5, '\n\n1 - Metros\n2 - Centímetros\n3 - Milímetros\n\nPara qual medida deverá ser convertida: '))

# Converter de Metros para...
if opcao == 1 and conversao == 2:
    resultado = quantidade * 100
    print(f'\n{quantidade}m equivale à: {resultado}cm!')
elif opcao == 1 and conversao == 3:
    resultado = quantidade * 1000
    print(f'\n{quantidade}m equivale à: {resultado}mm!')


# Converter de Centímetros para...
if opcao == 2 and conversao == 1:
    resultado = quantidade / 100
    print(f'\n{quantidade}cm equivale à: {resultado}m!')
elif opcao == 2 and conversao == 3:
    resultado = quantidade * 10
    print(f'\n{quantidade}cm equivale à: {resultado}mm!')


# Converter de Milímetros para...
if opcao == 3 and conversao == 1:
    resultado = quantidade / 100
    print(f'\n{quantidade}mm equivale à: {resultado}m!')
elif opcao == 3 and conversao == 2:
    resultado = quantidade / 10
    print(f'\n{quantidade}mm equivale à: {resultado}cm!')
