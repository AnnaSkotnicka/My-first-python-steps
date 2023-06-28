def tylko_litery(slowo):
    nowe_slowo = ""

    for i in slowo:
        if i.isalpha():
            nowe_slowo = nowe_slowo + i
    return nowe_slowo


def anagramy(slowo1, slowo2):

    slowo1 = tylko_litery(slowo1)
    slowo2 = tylko_litery(slowo2)

    if len(slowo1) != len(slowo2):
        return False

    if slowo1 == slowo2:
        return False

    lista_liter_slowa_1 = list(slowo1)
    lista_liter_slowa_2 = list(slowo2)

    lista_liter_slowa_1.sort()
    lista_liter_slowa_2.sort()

    return lista_liter_slowa_1 == lista_liter_slowa_2


slowo1 = input("Wpisz slowo1: ")
slowo2 = input("Wpisz slowo2: ")

if anagramy(slowo1, slowo2):
    print("To sa anagramy")
else:
    print("To nie są anagramy")