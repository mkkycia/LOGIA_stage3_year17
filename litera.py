def litera(lista):
    wynik = [' ']
    lista = ''.join(lista)
    for i in lista:
        pom = ''
        for j in lista:
            if j == i:
                pom += j
        if len(pom) > len(wynik[0]):
            wynik = [pom]
        elif len(pom) == len(wynik[0]):
            wynik.append(pom)
    wynik = list(set(''.join(wynik)))
    if len(wynik) == 1:
        return ''.join(wynik)
    else:
        return sorted(wynik)


print(litera(['julka','lubi','psy']))
