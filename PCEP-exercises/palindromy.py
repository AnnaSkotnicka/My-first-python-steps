def palindromy_tylko_litery(palindrom):
    nowy_palindrom = ""

    for i in palindrom:
        if i.isalpha():
            nowy_palindrom = nowy_palindrom + i
    return nowy_palindrom


def palindromy(slowo):
    slowo = palindromy_tylko_litery(slowo)
    slowo = slowo.lower()
    dlugosc_slowa = len(slowo)
    polowa_slowa = dlugosc_slowa // 2

    if dlugosc_slowa == 0:
        return False

    for i in range(polowa_slowa):
        if slowo[i] != slowo[-i-1]:
            return False
    return True


assert palindromy("k?aj ak") is True
assert palindromy("KAJ..ak") is True
assert palindromy("A krowa, paw, orka?") is True
assert palindromy("motyl") is False
assert palindromy("motyw") is False
assert palindromy("sofa") is False
assert palindromy("") is False
