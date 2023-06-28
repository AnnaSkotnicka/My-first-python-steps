import pygame

pygame.init()

szer = 500
wys = 800
okno = pygame.display.set_mode((szer, wys))

zagadka = "wisielec"
dlugosc_zagadki = len(zagadka)


class Napis:
    def __init__(self, tresc_napisu, wielkosc_cz, x, y):
        self.tresc_napisu = tresc_napisu
        self.rodzaj_cz = "Aristocrat"
        self.wielkosc_cz = wielkosc_cz
        self.kolor_cz = 'white'
        self.x = x
        self.y = y

    def napisz_napis(self):
        czcionka = pygame.font.SysFont(self.rodzaj_cz, self.wielkosc_cz)
        obraz_napisu = czcionka.render(self.tresc_napisu, 1, self.kolor_cz)
        okno.blit(obraz_napisu, (self.x - obraz_napisu.get_width()/2, self.y))


class Linia:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.g = 6
        self.kolor = "white"

    def rysuj(self):
        pygame.draw.line(okno, self.kolor, (self.x1, self.y1), (self.x2, self.y2), self.g)


class Kolo:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.g = 6
        self.kolor = "white"

    def rysuj(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.r, self.g)


class ZgadywanaLiterka:
    def __init__(self, x, y, a, b, litera):
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.litera = litera
        self.kolor = "white"
        self.odkryta = False

    def rysuj_haslo(self):
        pygame.draw.rect(okno, self.kolor, (self.x, self.y, self.a, self.b))
        if self.odkryta:
            Napis(self.litera.upper(), 50, self.x + self.a/2, self.y - 40).napisz_napis()   # x+a/2 wrzuca jako x w klasę napis


class Haslo:
    def __init__(self, zagadka):
        self.litery_hasla = []
        x = szer / 2 - ((dlugosc_zagadki * 60 - 20) / 2) # Wyśrodkowany napis i litery

        for litera_hasla in zagadka:  # tworzy prostokąty - dany x to prostokąt i literka z hasła
            self.litery_hasla.append(ZgadywanaLiterka(x, 300, 40, 5, litera_hasla))
            x += 60

    def czy_trafiona(self, zgadywana_literka):
        for litera_hasla in self.litery_hasla:
            if zgadywana_literka == litera_hasla.litera:
                return True
        return False

    def odkryj(self, litera):
        for litera_hasla in self.litery_hasla:
            if litera == litera_hasla.litera:
                litera_hasla.odkryta = True

    def rysuj(self):
        for litera in self.litery_hasla:
            litera.rysuj_haslo()

    def czy_wygrana(self):
        for litera_hasla in self.litery_hasla:
            if not litera_hasla.odkryta:
                return False
        return True


class Wisielec:

    def __init__(self):

        self.x = szer / 2
        self.y = ((wys - 80 - 400 - 5) / 2) + 400 + 5

        self.elementy_wisielca = [Linia(self.x - 120, self.y + 125, self.x - 80, self.y + 95), #1
                                  Linia(self.x - 80, self.y + 95, self.x - 40, self.y + 125), #2
                                  Linia(self.x - 80, self.y + 95, self.x - 80, self.y - 125), #3
                                  Linia(self.x - 80, self.y - 125, self.x + 80, self.y - 125), #4
                                  Linia(self.x + 80, self.y - 125, self.x + 80, self.y - 75), #5
                                  Kolo(self.x + 80, self.y - 55, 20), #6
                                  Linia(self.x + 80, self.y - 35, self.x + 80, self.y - 5), #7
                                  Linia(self.x + 80, self.y - 25, self.x + 60, self.y - 5), #8
                                  Linia(self.x + 80, self.y - 25, self.x + 100, self.y - 5), #9
                                  Linia(self.x + 80, self.y - 5, self.x + 60, self.y + 35), #10
                                  Linia(self.x + 80, self.y - 5, self.x + 100, self.y + 35),] #11

        self.nieudane_proby = 0

    def odkryj_element(self):
        self.nieudane_proby += 1

    def czy_caly_odkryty(self):
        if len(self.elementy_wisielca) <= self.nieudane_proby:
            Napis("Przegrałeś", 50, szer / 2, 150).napisz_napis()

    def rysuj(self):
        for i in range(self.nieudane_proby):
            self.elementy_wisielca[i].rysuj()


haslo = Haslo(zagadka)
wisielec = Wisielec()

while True:
    okno.fill((25, 103, 25))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key < 123 and event.key > 96:
                trafiona = False
                wprowadzona_literka = event.unicode  # Zamienia kod ASCII na literkę
                if haslo.czy_trafiona(wprowadzona_literka):
                    haslo.odkryj(wprowadzona_literka)
                    haslo.czy_wygrana()
                else:
                    wisielec.odkryj_element()

    haslo.rysuj()
    wisielec.rysuj()

    if wisielec.czy_caly_odkryty():
        Napis("Przegrałeś", 50, szer / 2, 100).napisz_napis()

    Napis("\"Wisielec\"", 50, szer / 2, 50).napisz_napis()

    if haslo.czy_wygrana():
        Napis("Wygrałeś", 50, szer / 2, 100).napisz_napis()

    pygame.display.update()