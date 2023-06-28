wzor_rzad_kolumna = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def wiersze(sudoku):
    lista_wierszy = []
    for wiersz in sudoku:
        lista_wiersza = list(wiersz)  # lista 1 wiersza

        lista_wierszy.append(lista_wiersza)

    return sprawdz(lista_wierszy)


def sprawdz(lista_list_cyfr):
    for i in range(0, 9):
        lista_list_cyfr[i].sort()

    for i in range(0, 9):
        if lista_list_cyfr[i] != wzor_rzad_kolumna:
            return False
    return True


def kolumny(sudoku):

    lista_kolumn = []
    for i in range(0, 9):
        tmp = []
        for j in range(0, 9):
            tmp.append(sudoku[i][j])

        lista_kolumn.append(tmp)

    return sprawdz(lista_kolumn)


def kwadraty_3_3(sudoku):

    lista_kwadratów_3_3 = []
    for i in range(0, 3):
        for j in range(0, 3):
            tmp = list(sudoku[i*3][3*j:3+3*j] + sudoku[1+i*3][3*j:3+3*j] + sudoku[2+i*3][3*j:3+3*j])
            lista_kwadratów_3_3.append(tmp)

    return sprawdz(lista_kwadratów_3_3)


def sprawdz_sudoku(dane):
    if wiersze(dane):
        print("Wiersze poprawne")
    else:
        print("Nie poprawne")

    if kolumny(dane):
        print("Kolumny poprawne")
    else:
        print("Nie poprawne")

    if kwadraty_3_3(dane):
        print("Kwadraty poprawne")
    else:
        print("Nie poprawne")


dane1 = [
    "295743861",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "154938672"]

dane = [
    "195743862",
    "431865927",
    "876192543",
    "387459216",
    "612387495",
    "549216738",
    "763524189",
    "928671354",
    "254938671"]


sprawdz_sudoku(dane)
