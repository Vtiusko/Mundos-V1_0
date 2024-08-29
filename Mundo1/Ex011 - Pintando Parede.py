'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
'''

altura = float(input('Informe a ALTURA da parede: '))
largura = float(input('Informe a LARGURA da parede: '))

area = altura * largura

print(f'Sua parede tem a área de {area:.2f}m²')
print(f'Serão necessárias {area / 2:.1f}L para pintar a sua parede')