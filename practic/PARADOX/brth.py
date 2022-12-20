import random


def brthd(itr, n=23):
    count = 0
    for m in range(itr):
        d = []
        for i in range(n):
            age = random.randint(1, 365)
            if age in d:
                count += 1
                break
            d.append(age)
    return count / (itr / 100)
