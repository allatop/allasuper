import random
a=[]
b=0
for i in range(23):
    a.append(random.randint(1,365))
print(a)
for i in range(len(a)):
    for j in range((i+1),len(a)):
        if(a[i]==a[j]):
            b+=1
            print(a[i],a[j])
print(b)
print(b/253)
if((b/253)>=0.5):
    print("Правда")
else:
    print("Ложь")

