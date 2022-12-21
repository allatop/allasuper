def scramble(strl, str):
    strl = " ".join(strl).split()
    str = " ".join(str).split()
    count = 0
    strl = list(set(strl))
    for i in range(len(strl)):
        for j in range(len(str)):
            if strl[i] == str[j]:
                count += 1


    if count >= len(str):
        print(True)
    else:
        print(False)


scramble('rkqodlw', 'world')
scramble('cedewaraaossoqqyt', 'codewars')
scramble('katas', 'steak')
