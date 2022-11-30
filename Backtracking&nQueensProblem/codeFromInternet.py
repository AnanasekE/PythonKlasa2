def ustawHetmana(dane, n):
    ile = 0
    if (len(dane) == n):
        return 1
    else:
        for k in range(0, n):
            if (czyMoze(dane, len(dane), k)):
                dane.append(k)
                ile += ustawHetmana(dane, n)
                dane.pop()
    return ile


def czyMoze(dane, x, y):
    for i in range(0, len(dane)):
        przesx = abs(i - x);
        przesy = abs(dane[i] - y);
        if (dane[i] == y or przesx == przesy):
            return False
    return True


def szukajRozwiazan(n):
    dane = []
    return ustawHetmana(dane, n)


n = int(input("Podaj wielkość planszy\n n = "))
w = szukajRozwiazan(n)
print("Rozwiązań: " + str(w))
