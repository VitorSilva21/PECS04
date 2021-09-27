h_sala=int(input())
lag_sala=int(input())
com_sala=int(input())
area_sala= lag_sala * com_sala
esp_sala= lag_sala * h_sala
vol_sala= lag_sala * com_sala * h_sala
area_das_paredes = 2 * (esp_sala + com_sala * h_sala)
print(f'%.f' % area_sala)
print(f' %.f' % vol_sala)
print(f'%.f' % area_das_paredes)
