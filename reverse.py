a=[2,3,12,1]
b=[9,23,5,4]
for i in a:
    b.append(i)

for i in range(len(b)):
    for j in range(len(b)):
        if b[i] > b[j]:
            b[i],b[j] = b[j],b[i]
print(b)