# Podaje datę najbliższej ostatniej niedzieli w miesiącu

import datetime


def znajdz_ost_nd(dzien):
    slownik_miesiecy = {"1": 31,
                        "2": 28,
                        "3": 31,
                        "4": 30,
                        "5": 31,
                        '6': 30,
                        "7": 31,
                        "8": 31,
                        "9": 30,
                        "10": 31,
                        "11": 30,
                        "12": 31}

    ilosc_dni_miesiaca = slownik_miesiecy[str(dzien.tm_mon)]

    for d in range(ilosc_dni_miesiaca, dzien.tm_mday, -1):
        data_dnia = datetime.date(dzien.tm_year, dzien.tm_mon, d)  # Dzień tygodnia dla np. 30 dnia obecnego miesiąca
        d = data_dnia.timetuple().tm_wday
        if d == 6:
            return data_dnia
    return False


dzis = datetime.date.today()  # Pobiera dzisiejszą datę-format daty
dzisiejsza_data = dzis.timetuple()  # Tworzy krotkę z dziesiejszą datą

inna_data = datetime.timedelta(weeks=3)  # Tworzy 3 tygodnie
nastepny_miesiac = dzis + inna_data  # Tworzy datę za trzy tygodnie
krotka_nastepny_miesiac = nastepny_miesiac.timetuple()


if znajdz_ost_nd(dzisiejsza_data):
    print("Tego dnia wypada ostatnia najbliższa niedziela bieżącego miesiąca: ", znajdz_ost_nd(dzisiejsza_data))
    print("Pozostało dni: ", (znajdz_ost_nd(dzisiejsza_data) - dzis).days)
else:
    print("W tym miesiącu nie ma już niedzieli. W kolejnym miesiącu ostatnia niedziela wypada dnia: ", end="")
    print(znajdz_ost_nd(krotka_nastepny_miesiac))
    print("Pozostało dni : ", (znajdz_ost_nd(krotka_nastepny_miesiac) - dzis).days)

