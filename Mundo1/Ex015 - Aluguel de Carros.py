'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

print('Bem-vindo ao Cálculo de Pgto. de Carros Alugados')

dias = int(input('\nInforme a quantidade de dias alugados: '))
quilometros = float(input('Informe a quantidade de Km percorridos: '))

calculo_dias = (dias * 60) + (quilometros * 0.15)

print(f'O valor total por {dias} dias alugados: R${calculo_dias:.2f}')