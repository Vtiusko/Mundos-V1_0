'''
Faça um programa que leia um número de 0 a 9999 
e mostre na tela cada um dos dígitos separados

 ex.: digite um número: 1834
- unidade: 4
- dezena: 3
- centena: 8
- milhare: 1
'''

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

'''
O QUE ACONTECEU?

O programa pegou o número escolhido pelo usuário, pegou o resto da divisão inteira(// - é o valor que fica abaixo da chave, ) por 1 e, pegou o modulo de 10 (% - é o resto da divisão por aqui no caso 10)
'''

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar {}'.format(m))
