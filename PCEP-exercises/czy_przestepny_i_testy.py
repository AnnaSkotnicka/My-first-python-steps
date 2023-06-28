def czy_przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    if miesiac <= 12:
        liczba_dni_w_miesiacu = [31,28,31,30,31,30,31,31,30,31,30,31]
        if czy_przestepny(rok) == True and miesiac <=12:
            liczba_dni_w_miesiacu[1] = 29
        return liczba_dni_w_miesiacu[miesiac-1]
    else:
        return 


testuj_lata = [1900, 2000, 2016, 1987, 2020]
testuj_miesiace = [2, 2, 1, 11, 13]
testuj_wynik = [28, 29, 31, 30,31]
for i in range(len(testuj_lata)):
    r = testuj_lata[i]
    m = testuj_miesiace[i]
    print(r, m, "-> ", end="")
    wynik = dni_w_miesiacu(r, m)
    print(wynik)
    if wynik == testuj_wynik[i]:
        print("OK\n\n")
    else:
        print("Nie powiodło się\n\n")