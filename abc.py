def abc(napis):
    max_n = 0
    max_c = 0
    max_z = 0
    for e in napis:
        if e not in "ncz":
            max_n += 1
            max_c += 1
            max_z += 1
        else:
            if e == "n":
                max_n += 1
            if e == "c":
                max_c = 1 + max(max_n, max_c)
            if e == "z":
                max_z = 1 + max(max_n, max_c, max_z)
    return len(napis) - max(max_n, max_c, max_z)
