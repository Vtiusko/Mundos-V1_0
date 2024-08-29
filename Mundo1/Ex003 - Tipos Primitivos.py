'''
Se não definirmos o tipo primitivo:
    - INT
    - FLOAT
    - BOOL
    - STR (É O TIPO PADRÃO)

    O Python irá concatenar ao invés de somar
'''

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

total = num1 + num2

print(f'{num1} + {num2} = {total}')