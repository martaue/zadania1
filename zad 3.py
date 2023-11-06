import random

def czy_parzysta(liczba):
    if liczba % 2 == 0:
        return True
    else:
        return False

losowa = random.randint(1, 1000)
wynik = czy_parzysta(losowa)

if wynik:
    print(f"Liczba {losowa} jest parzysta.")
else:
    print(f"Liczba {losowa} jest nieparzysta.")