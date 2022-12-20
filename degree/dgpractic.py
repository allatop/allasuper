import degree


def create(*args, **kwargs):
    p = []
    for i in range(len(args)):
        p.append(f'point_{i} = {degree.gms(args[i])}')
    for name, ged in kwargs.items():
        p.append(f'{name}={degree.gms(ged)}')
    return p


print(create(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))
