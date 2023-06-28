import datetime
import time
import random

k = random.randint(1, 10)
print(k)

enter = input("")
if enter == "":
    t_poczatkowy = time.time()
enter = input("")
tt = time.time()

czas_uzytkownika = tt-t_poczatkowy
print(czas_uzytkownika) #Różnica użytkownika

roznica = czas_uzytkownika - k
if roznica > 0:
    print(f"Byłeś za wolny o {roznica}")
elif roznica < 0:
    print(f"Byłeś za szybki o {roznica}")
else:
    print("Gratulacje")









