def zawody(wyniki):
    n = len(wyniki[0])
    zawodnicy = [chr(i+65) for i in range(n)]
    for wynik in wyniki:
        m = min(wynik)
        i = wynik.index(m)
        del zawodnicy[i:i+1]
    return zawodnicy[0]
