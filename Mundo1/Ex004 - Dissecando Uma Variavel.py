'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
'''

dado = input('Digite qualquer coisa (número, letra, símbolo, nada...etc): ')

print('\nOs métodos ".is...()" retornam True ou False\n')

print('\nO valor digitado é alfabético? ', dado.isalpha())
print('O valor digitado é letra e número? ', dado.isalnum())
print('O valor digitado é somente letras maiúsculas? ', dado.isupper())
print('O valor digitado é um conjunto de carácteres ASCII? ', dado.isascii())
print('O valor digitado é somente decimal (0 - 9)? ', dado.isdecimal())
print('O valor digitado é somente dígitos? ', dado.isdigit()) # Valores como expoêntes ², são considerados dígitos
print('O valor digitado é um identificador válido? ', dado.isidentifier()) # Não começa com número, ou contenha espaços
print('O valor digitado é somente letras minúsculas? ', dado.islower())
print('O valor digitado é imprimível? ', dado.isprintable())
print('O valor digitado é somente espaços em branco? ', dado.isspace())
print('A(s) palavra(s) do valor digitado, começa(m) com letra maiúscula? ', dado.istitle())
