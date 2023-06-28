# Szyfr Cezara

# tekst = input("Wpisz wiadomosc: ")
tekst = "szyfr"

def zapytaj_o_krok():
    krok = int(input("Wpisz liczbę z przedziału od 1 do 25 włącznie: "))
    if 1 < krok and krok < 26:
        return krok
    else:
        print("Wprowadzono błędną wartość.")
        krok = zapytaj_o_krok()
        return krok


def tworzenie_szyfru_cezara(tekst, krok):
    szyfr = ''
    for char in tekst:
        if not char.isalpha():  # Jeśli bieżący znak jest niealfabetyczny to pozostaje w kodzie bez zmian
            szyfr = szyfr + char
        else:
            kod = zaszyfruj_literke(char, krok)
            szyfr += kod
    return szyfr


def zaszyfruj_literke(char, krok):
    if ord(char) in range(65, 91):
        kod = ord(char) + krok
        if kod in range(65, 91):
            return chr(kod)
        else:
            tmp = kod - 91
            kod = 65 + tmp
            if kod in range(65, 91):
                return chr(kod)
            return zaszyfruj_literke(chr(kod), krok)

    if ord(char) in range(97, 123):
        kod = ord(char) + krok
        if kod in range(97, 123):
            return chr(kod)
        else:
            tmp = kod - 123
            kod = 97 + tmp
            if kod in range(97, 123):
                return chr(kod)
            return zaszyfruj_literke(chr(kod), krok)


krok = zapytaj_o_krok()
wynik = tworzenie_szyfru_cezara(tekst, krok)

print(wynik)

assert tworzenie_szyfru_cezara("abcdefghijklmnopqrstuvwxyz", 1) == "bcdefghijklmnopqrstuvwxyza"
assert tworzenie_szyfru_cezara("abcdefghijklmnopqrstuvwxyz", 25) == "zabcdefghijklmnopqrstuvwxy"
assert tworzenie_szyfru_cezara("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1) == "BCDEFGHIJKLMNOPQRSTUVWXYZA"
assert tworzenie_szyfru_cezara("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25) == "ZABCDEFGHIJKLMNOPQRSTUVWXY"
assert tworzenie_szyfru_cezara("ABC  @  def  61  XYZ", 1) == "BCD  @  efg  61  YZA"


#rozkodowywanie