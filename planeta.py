def odl(a, b, r):
    x = abs(a[0]-b[0])
    if x > r/2:
        x = r - x
    y = abs(a[1]-b[1])
    if y > r/2:
        y = r - y
    return x + y

def planeta(r, lista):
    max_o = 0
    while len(lista) > 0:
        pom = []
        max_b = 1
        pom.append(lista.pop())
        while len(pom) > 0:
            e = pom.pop()
            for s in lista:
                if odl(e, s, r) <= 5:
                    lista.remove(s)
                    pom.append(s)
                    max_b += 1
        if max_b > max_o:
            max_o = max_b
    return max_o

