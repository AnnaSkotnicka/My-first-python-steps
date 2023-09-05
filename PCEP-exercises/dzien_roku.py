def sprawdz_poprawnosc_daty(podany_rok, podany_miesiac, podany_dzien):
    if 1 > podany_miesiac or podany_miesiac > 12:
        print("Błędny miesiąc")
        return False
    if podany_rok < 1:
        print("Błędny rok")
        return False
    if podany_dzien == 1:
        return True
    if podany_dzien > dni_w_miesiacu(rok, miesiac) or podany_dzien < 1:
        print("Błędny dzień")
        return False
    return True


def czy_przestepny(podany_rok):
    if podany_rok % 4 == 0 and (podany_rok % 100 != 0 or podany_rok % 400 == 0):
        return True
    return False


def dni_w_miesiacu(podany_rok, podany_miesiac):
    if not sprawdz_poprawnosc_daty(podany_rok, podany_miesiac, 1):
        raise Exception("Podaj miesiąc od 1 do 12")
    if podany_rok < 1:
        raise Exception("Podaj rok > 1")

    liczba_dni_w_miesiacu = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if czy_przestepny(podany_rok):
        liczba_dni_w_miesiacu[1] = 29
    return liczba_dni_w_miesiacu[podany_miesiac-1]


def dzien_w_roku(podany_rok, podany_miesiac, podany_dzien):
    if podany_miesiac < 1 or podany_miesiac > 12:
        raise Exception("Podaj miesiąc od 1 do 12")
    if podany_rok < 1:
        raise Exception("Podaj rok > 1")

    suma = 0
    for i in range(1, podany_miesiac):
        suma = suma + dni_w_miesiacu(rok, i)
    return suma + podany_dzien


rok, miesiac, dzien = 2015, 1, 31
if sprawdz_poprawnosc_daty(rok, miesiac, dzien):
    print(dzien_w_roku(rok, miesiac, dzien))
