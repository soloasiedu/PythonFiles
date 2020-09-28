


def dotproduct(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] * b[i])
    return c

a = [1,3,5,6]
b = [3,2,1,3]

print(dotproduct(a, b))
