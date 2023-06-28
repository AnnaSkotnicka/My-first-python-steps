def readint(prompt, min, max):

    try:
        value = int(input(prompt))
        if min < value < max:
            return value
        else:
            print("Błąd: podana liczba jest spoza dozwolonego zakresu (min..max)")
            return readint(prompt, min, max)
    except ValueError:
        print("Błąd: wprowadzono nieprawidłową liczbę.")
        return readint(prompt, min, max)


v = readint("Podaj liczbe od -10 do 10: ", -10, 10)

print("Liczba to:", v)