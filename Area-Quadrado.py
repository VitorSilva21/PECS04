def area_quadrado(lado):
    return lado ** 2
def perimetro_quadrado(lado):
    return lado * 4
valor_lados= float(input())
print(f'%10.4f' % area_quadrado(valor_lados))
print(f'%10.4f' % perimetro_quadrado(valor_lados))
