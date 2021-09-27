def h(horas):
    return horas * 3600
def min(minutos):
    return minutos * 60

horas = int(input(''))
minutos = int(input(''))
segundos = int(input(''))
soma = h(horas) + min(minutos) + segundos
print('',soma)
