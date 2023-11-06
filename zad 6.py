def laczenie(lista_1, lista_2):
    polaczona = lista_1 + lista_2
    polaczona = list(set(polaczona))

    wynik = [i ** 3 for i in polaczona]

    return wynik


lista_1 = [4, 7, 8, 9, 0]
lista_2 = [4, 3, 5, 6, 7]

wynik = laczenie(lista_1, lista_2)
print(wynik)