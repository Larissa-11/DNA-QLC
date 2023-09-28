a = [1, 2, 3, 4, 6]
b = [12, 13, 14, 15, 16]
c = [22, 23, 24, 25, 26]
d = [32, 33, 34, 35, 36]
A = [a, b, c, d]
C=list()

def getPlans(lis, CC, jude=True):
    if jude: lis = [[[i] for i in lis[0]]] + lis[1:]
    if len(lis) > 2:
        for i in lis[0]:
            for j in lis[1]:
                getPlans([[i + [j]]] + lis[2:], CC, False)
    elif len(lis) == 2:
        for i in lis[0]:
            for j in lis[1]:
                CC.append(i + [j])
    return CC


AA = getPlans(A,C)
print(AA)
