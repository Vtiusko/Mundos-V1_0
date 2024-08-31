'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

while True:
    quantidade_alunos = int(input("Digite a quantidade de alunos: "))

    nomes = []
    for i in range(quantidade_alunos):
        nome = input("Digite o nome do aluno {}: ".format(i+1))
        nomes.append(nome)

    random.shuffle(nomes)

    print("A ordem de apresentação dos alunos é:")
    for nome in nomes:
        print(nome)

    resposta = input("Deseja executar novamente? [ S / N ]: ")
    if resposta.upper() != "S":
        break
