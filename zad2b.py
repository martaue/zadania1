def funkcja (liczby):
    pomnozone =[]
    for el in liczby:
        pomnozone.append(el * 2)
    return pomnozone
liczby = [3,6,8,2,5]
wynik = funkcja (liczby)
print (wynik)

def funkcja2 (liczby):
    return [el*2 for el in liczby]
print(funkcja2(liczby))