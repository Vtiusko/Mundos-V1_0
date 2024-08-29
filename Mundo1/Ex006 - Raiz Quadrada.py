def operando():
    num = int(input('\nDigite um número: '))
    opr = int(input('\nDentre as opções abaixo:\n\n\033[033m 1 \033[m- Calcular o quadrado\n\033[33m 2 \033[m- Calcular o Cubo\n\033[33m 3 \033[m- Calcular a Raíz\n\nEscolha: '))

    if opr == 1:
        opr = num * num
        msg = f'{num}² = {opr}\n'

    elif opr == 2:
        opr = (num * num) * 3
        msg = f'{num}³ = {opr}\n'

    elif opr == 3:
        opr = num ** (1 / 2)
        msg = f'√{num} = {opr}\n'

    else:
        print('Digite uma opção válida!')

    print(msg)


while True:
    print('\033[33mCALCULE A RAÍZ QUADRADA & EXPONÊNCIAÇÃO\033[m')
    operando()

    continuar = input('Deseja continuar \033[33m [ S / N ]\033[m: ').upper()[0]
    while (len(continuar) != 1) or (continuar not in 'SN'):
        print('\033[31mDigite apenas "S" ou "N"!\033[m')

        continuar = input('Deseja continuar \033[33m [ S / N ]\033[m: ').upper()[0]
        if continuar == 'N':
            print('\nTchauuu!')
            break
