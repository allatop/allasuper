a = int(input())
b = int(input())
if ((a == 4) or (a == 6) or (a == 9) or (a == 11)) and (b == 30):
    print(f'1-{a + 1}-2022')
elif ((a == 1) or (a == 3) or (a == 5) or (a == 7) or (a == 8) or (a == 10) or (a == 12)) and (b == 31):
    print(f'1-{a + 1}-2022')
elif (a == 2) and (b == 28):
    print(f'1-{a + 1}-2022')
else:
    print(f'{b+1}-{a}-2022')
