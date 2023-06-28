import time

t1 = time.time()  # mierzy liczbę sekund od 1.01.1970
t2 = time.gmtime()  # konwertuje do formy struct_time
t3 = time.strftime("Dzisiaj jest %j dzień roku", time.gmtime())  # %j - specyfikator. Za jego pomoca można wyciągnąć jedną wartość z obiektu struct_time

# print(t1, t2)
# print(t3)


def czekaj():
    for s in range(1, 11):
        print(s)
        if s == 5:
            time.sleep(s)





czekaj()
