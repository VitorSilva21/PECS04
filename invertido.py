num= int(input())
u = num % 10
num= num // 10
d= num % 10
num= num // 10
c= num % 10
num= num // 10
m= num % 10
num_invertido= (u * 1000) + (d * 100) + (c * 10) + (m * 1)
print('%.f' % num_invertido)
