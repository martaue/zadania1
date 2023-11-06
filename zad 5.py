def sprawdz(lista, wartosc):
    if wartosc in lista:
        return True
    else:
        return False


lista_1 = [5, 89, 7, 15, 21, 52]
wartosc = 7
wynik = sprawdz(lista_1, wartosc)
print(wynik)