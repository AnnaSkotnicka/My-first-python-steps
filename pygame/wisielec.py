import pygame

pygame.init()

szer = 800
wys = 600
okno = pygame.display.set_mode((szer, wys))

zagadka = "len"
dlugosc_zagadki = len(zagadka)
x = 0


class Linia():
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.g = 6
        self.kolor = "white"

    def rysuj(self):
        pygame.draw.line(okno, self.kolor, (self.x1, self.y1), (self.x2, self.y2), self.g)


class Kolo():
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.g = 6
        self.kolor = "white"

    def rysuj(self):
        pygame.draw.circle(okno, self.kolor, (self.x, self.y), self.r, self.g)


class ZgadywanaLiterka():
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
            czcionka = pygame.font.SysFont("Aristocrat", 50)
            obraz_napisu = czcionka.render(self.litera.upper(), 1, 'white')
            okno.blit(obraz_napisu, (self.x+(self.a/2)-obraz_napisu.get_width()/2, self.y-40))


elementy_wisielca = [Linia(400, 500, 440, 470),
                     Linia(440, 470, 480, 500),
                     Linia(440, 470, 440, 250),
                     Linia(440, 250, 600, 250),
                     Linia(600, 250, 600, 300),
                     Kolo(600, 320, 20),
                     Linia(600, 340, 600, 370),
                     Linia(600, 350, 580, 370),
                     Linia(600, 350, 620, 370),
                     Linia(600, 370, 580, 410),
                     Linia(600, 370, 620, 410),]

litery_hasla = []

for litera_hasla in zagadka:
    x += 60
    litery_hasla.append(ZgadywanaLiterka(x, 180, 40, 5, litera_hasla))

nieudane_proby = 0


def czy_wygrana():
    for litera_hasla in litery_hasla:
        if not litera_hasla.odkryta:
            return False
    return True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key < 123 and event.key > 96:
                trafiona = False
                zgadywana_literka = chr(int(event.key)) #Zamienia kod ASCII na literkę
                print(zgadywana_literka)
                for litera_hasla in litery_hasla:
                    if zgadywana_literka == litera_hasla.litera:
                        litera_hasla.odkryta = True
                        trafiona = True

                if not trafiona:
                    nieudane_proby += 1

    okno.fill((25, 103, 25))

    for i in range(nieudane_proby):
        elementy_wisielca[i].rysuj()

    for l in litery_hasla:
        l.rysuj_haslo()

    if czy_wygrana():
        czcionka = pygame.font.SysFont("Aristocrat", 50)
        obraz_napisu = czcionka.render("Wygrałeś", 1, 'white')
        okno.blit(obraz_napisu, (szer / 2 - obraz_napisu.get_width() / 2, 100))

    if len(elementy_wisielca) <= nieudane_proby:
        czcionka = pygame.font.SysFont("Aristocrat", 50)
        obraz_napisu = czcionka.render("Przegrałeś", 1, 'white')
        okno.blit(obraz_napisu, (szer / 2 - obraz_napisu.get_width() / 2, 100))

    czcionka = pygame.font.SysFont("Aristocrat", 50)
    obraz_napisu = czcionka.render("\"Wisielec\"", 1, 'white')
    okno.blit(obraz_napisu, (szer / 2 - obraz_napisu.get_width() / 2, 50))

    pygame.display.update()


    #napis na środku
    #klasa dla hasła
    #funkcja odkryj
    #nie działają polskie znaki
    #klasa napis
    #więcej funkcji