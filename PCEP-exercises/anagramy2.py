def tylko_litery(slowo):
    slowo = slowo.lower().strip()
    for i in slowo:  # iteruj po literkach w słowie
        if not i.isalpha():  # Jeśli nie jest literką
            nowe_slowo = input("Wpisz ponownie slowo: ")  # Wpisz ponownie slowo
            return tylko_litery(nowe_slowo)  # sprawdz wpisane nowe słowo
    return slowo


def anagramy(slowo1, slowo2):
    if slowo1 == slowo2:
        return False

    lista_liter_slowa_1 = list(slowo1)
    lista_liter_slowa_2 = list(slowo2)

    lista_liter_slowa_1.sort()
    lista_liter_slowa_2.sort()

    return lista_liter_slowa_1 == lista_liter_slowa_2


def komunikat():
    if anagramy(slowo1, slowo2):
        print("To sa anagramy")
    else:
        print("To nie są anagramy")


slowo1 = input("Wpisz slowo1: ")
slowo1 = tylko_litery(slowo1)
slowo2 = input("Wpisz slowo2: ")
slowo2 = tylko_litery(slowo2)
komunikat()