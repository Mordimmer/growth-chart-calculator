#funkcja wyliczająca bmi przy pomocy parametru "wagi" i wzrost
def oblicz_bmi(waga, wzrost):
    bmi = waga/(wzrost*0.01)**2 #(waga[kg]/wzrost[m]^2)
    return bmi

#funkcja okreslajaca na co wskazuje twoje bmi, przy pomocy wyniku funkcji oblicz_bmi()
def co_wskazuje_bmi(bmi): #bardzo duże uproszczenie, do dopracowania
    if bmi<=18:
        return("Masz niedowagę, musisz więcej jeść")
    elif 18<bmi<=25:
        return("Masz prawidłową wagę ciała, oby tak dalej")
    elif 25<bmi<=30:
        return("Masz nadwagę, lepej uważaj")
    elif 30<bmi:
        return("Jesteś otyły, lepiej sobie trochę odpuść")    
    else:
        return("coś poszło nie tak")
    