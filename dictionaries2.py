alline_o = {'color': 'blue', 'point': '5'}
print(alline_o['color'])
# adding new key value i dict
alline_o['x_position'] = 'frist'
alline_o['y_position'] = 'secod'
print(alline_o)
# delete key value
x = alline_o.get('color')
print(x)

for key, value in alline_o.items():
    print(f'{key}:{value}')
