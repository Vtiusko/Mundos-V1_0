'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
* Cotação do Dólar no momento do código: $5.17
'''
while True:
    msg = 'Cotação dólar: $5.17'
    print(f'=' * 9,' Conversor de REAL para DÓLAR ', '=' * 9, f'\n{msg:>50}\n')

    carteira = float(input('→ Informe quantos reais você possuí: R$ '))
    dolar = 5.17
    total_dolares = carteira / dolar

    print(f'\nCom R${carteira:.2f}, é possível comprar ${total_dolares:.2f}')

    
    pergunta = input('\nDeseja calcular novamente [ S / N ]: ').upper()[0]
    while pergunta not in 'SN' or pergunta == '':
        print('Você deve digitar "S" ou "N"!')

        pergunta = input('\nDeseja calcular novamente [ S / N ]: ').upper()[0]

    if pergunta == 'N':
        break
