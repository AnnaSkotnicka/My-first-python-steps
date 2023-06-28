def palindromy_tylko_litery(palindrom):
    nowy_palindrom = ""

    for i in palindrom:
        if i.isalpha():
            nowy_palindrom = nowy_palindrom + i
    return nowy_palindrom


def palindromy(slowo):
    slowo = palindromy_tylko_litery(slowo)
    print(slowo)
    slowo = slowo.lower()

    if len(slowo) == 0:
        return False

    wynik = slowo == slowo[::-1]

    return wynik


assert palindromy("k?aj ak") is True
assert palindromy("KAJ..ak") is True
assert palindromy("A krowa, paw, orka?") is True
assert palindromy("motyl") is False
assert palindromy("motyw") is False
assert palindromy("sofa") is False
assert palindromy("") is False
