from bmi import *

print("W celu wyznaczenia BMI dziecka podaj następujące wartości")
x=False
while x==False:
    print(x)
    waga=80#float(input("Waga[kg]: "))
    wzrost=180#float(input("Wzorst[cm] ")) 
    wiek=22#float(input("Wiek: "))
    #płeć=float(input())
    #x=is_true()
    x=input("Czy wprowadzone dane są prawidłowe?[t/n]")
    if x=="t":
        x = True
    elif x=="n":
        x = False
    else:
        print("Coś nie tak")
        x= False


bmi = oblicz_bmi(waga, wzrost)
print(co_wskazuje_bmi(bmi))