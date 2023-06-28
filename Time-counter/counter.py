import datetime
import pygame

pygame.init()

szer = 500
wys = 800
okno = pygame.display.set_mode((szer, wys))


class Napis:
    def __init__(self, tresc_napisu, wielkosc_cz, x, y):
        self.tresc_napisu = tresc_napisu
        self.rodzaj_cz = "Arial"
        self.wielkosc_cz = wielkosc_cz
        self.kolor_cz = 'white'
        self.x = x
        self.y = y

    def napisz_napis(self):
        czcionka = pygame.font.SysFont(self.rodzaj_cz, self.wielkosc_cz)
        obraz_napisu = czcionka.render(self.tresc_napisu, True, self.kolor_cz)
        okno.blit(obraz_napisu, (self.x - obraz_napisu.get_width()/2, self.y))


class Gracz:
    def __init__(self, nazwa_gracza, czas):
        self.nazwa_gracza = nazwa_gracza
        self.czas = datetime.timedelta(seconds=czas)  # w sekundach
        self.pozostaly_czas = self.czas

    def licz_pozostaly_czas(self, roznica_czasu):
        self.pozostaly_czas = self.pozostaly_czas - roznica_czasu

    def display(self):
        Napis(str(self.pozostaly_czas)[0:7], 40, szer / 2, 300).napisz_napis()


gracz1 = Gracz("Gracz1", 60)
poprzedni_czas = datetime.datetime.now()
while True:
    teraz = datetime.datetime.now()
    okno.fill((153, 50, 204))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    Napis("Licznik czasu", 50, szer / 2, 150).napisz_napis()
    roznica = teraz - poprzedni_czas
    poprzedni_czas = teraz

    gracz1.licz_pozostaly_czas(roznica)
    gracz1.display()

    pygame.display.update()


