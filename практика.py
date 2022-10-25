import библ

def create(*args, **kwargs):
    p= []
    for i, deg in enumerate(args):
        p.append(f'point_{i} = {библ.gms(deg)}')
    for name, ged in kwargs.items():
        p.append(f'{name}={библ.gms(ged)}')
    return p

print(create(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1= 140.85706440))
