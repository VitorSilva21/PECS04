preco= float(input().strip())
valor_percentual= float(input().strip()) 
preco_acres= preco + (preco*valor_percentual/100)
preco_desc= preco - (preco*valor_percentual/100)
print('%.2f' % preco_acres)
print('%.2f' % preco_desc)
