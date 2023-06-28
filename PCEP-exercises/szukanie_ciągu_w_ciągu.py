def szukaj(first_string, second_string):
    length_first_string = len(first_string)
    indeks = 0

    for i in range(length_first_string):
        indeks = second_string.find(str(first_string[i]), indeks) #zwraca index szukanej literki (i) tylko że z drugiego stringa
        if indeks != -1:
            indeks = indeks + 1
        else:
            return False
    return True


def test(a, b):

    example = szukaj(a, b)

    if example:
        print("tak")
    else:
        print("Nie")


test("motyl", "lokomotywownia")
test("motyw", "lokomotykwownia")
test("sofa", "vcxzxduybfdsofawuefga")