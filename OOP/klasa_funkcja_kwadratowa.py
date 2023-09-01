class FunkcjaKwadratowa:
    def __init__(self):
        print("y = ax2 + bx + c")
        self.a = int(input(f"a: "))
        self.b = int(input(f"b: "))
        self.c = int(input(f"c: "))
        print(f"y = {self.a}x2 + {self.b}x + {self.c}")

    def rozwiaz(self):
        delta = -self.b - 4 * self.a * self.c
        x1 = (-self.b - (delta ** (1 / 2))) / (2 * self.a)
        x2 = (-self.b + (delta ** (1 / 2))) / (2 * self.a)
        if delta >= 0:
            x1 = round(x1, 2)
            x2 = round(x2, 2)
        self.wyswietl(delta, x1, x2)
        return x1, x2, delta

    @staticmethod
    def wyswietl(delta, x1, x2):
        if delta > 0:
            print(f"Funkcja ma 2 miejsce zerowe: x1 = {x1}, x2 = {x2}")
        elif delta == 0:
            print(f"Funkcja ma 1 miejsce zerowe: x1 = {x1}")
        else:
            print("Brak miejsc zerowych")


if __name__ == "__main__":
    funkcja1 = FunkcjaKwadratowa()
    funkcja1.rozwiaz()