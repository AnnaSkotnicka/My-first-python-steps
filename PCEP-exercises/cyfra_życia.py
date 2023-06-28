def spr_cyfry(s):
    if len(str(s)) == 1:
        print("Twoja szczęśliwa liczba to: ", s)
    else:
        suma(str(s))


def suma(data_urodzin):
    data_urodzin = list(data_urodzin)
    s = 0

    for i in data_urodzin:
        i = int(i)
        s += i

    spr_cyfry(s)


data = input("Podaj datę urodzin: ")
suma(data)
