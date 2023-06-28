def czy_przestepny(rok):
    if rok % 4 == 0 and (rok % 100 != 0 or rok % 400 == 0):
        return True
    else:
        return False

def dni_w_miesiacu(rok, miesiac):
    if miesiac > 12 or miesiac < 1:
        return
    
    if rok < 1:
        return
    
    liczba_dni_w_miesiacu = [31,28,31,30,31,30,31,31,30,31,30,31]
    if czy_przestepny(rok) == True:
        liczba_dni_w_miesiacu[1] = 29
    return liczba_dni_w_miesiacu[miesiac-1]

def dzien_w_roku(rok, miesiac, dzien):
    if miesiac > 12 or miesiac < 1:
        return
    
    if rok < 1:
        return
    
    if dzien > dni_w_miesiacu(rok, miesiac) or dzien < 1:
        return
    
    suma = 0
    for i in range(1,miesiac):
        suma = suma + dni_w_miesiacu(rok, i)
        
    return suma+dzien
        
print(dzien_w_roku(2001, 12, 31))
