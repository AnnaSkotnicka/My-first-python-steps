def formatuj_date(d):
    d = d.replace(" ", "").replace("-", "").replace(".", "").replace(",", "")
    return d


def czy_data_jest_poprawna(d):
    if not d.isdigit():
        return False
    if len(d) != 8:
        return False
    if not 0 < int(d[0:2]) < 31:  # sprawdzanie dnia (nie uwględniłam krótszych miesięcy - 30 i 28 dni)
        return False
    if not 0 < int(d[2:4]) < 13:
        return False
    if not (2023 - 150) < int(d[4:9]) < 2013:  # True: między 10 a 150 lat
        return False
    return True


def suma(data_urodzin):
    data_urodzin = list(data_urodzin)
    suma_cyfr = 0

    for i in data_urodzin:
        i = int(i)
        suma_cyfr += i

    return suma_cyfr


def spr_cyfry(s):
    if len(str(s)) == 1:
        print("Twoja szczęśliwa liczba to:", s)
    else:
        spr_cyfry(suma(str(s)))


if __name__ == "__main__":
    data = input("Podaj datę urodzin (dzien miesiac rok): ")
    data = formatuj_date(data)
    while not czy_data_jest_poprawna(data):
        data = input("Podaj datę urodzenia (dzien miesiac rok): ")
        data = formatuj_date(data)
    spr_cyfry(suma(data))