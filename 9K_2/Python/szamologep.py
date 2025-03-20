szam1 = int(input("Kérek egy számot: ")) #Bekérek valamit a felhasználótól, és átalakítom számmá
szam2 = int(input("Kérek mégegy számot: ")) #Mégegyszer a fentit

muv = input("Kérek egy műveleti jelet(+,-,/,*):") #Bekérek egy műveleti jelet

if (muv == "+"): #Ellenőrzöm, hogy a műveleti jel egyenlő-e a '+'-jellel
    print(szam1+szam2) #Ha igaz, kiírom az eredményt.
elif (muv == "-"):
    print(szam1-szam2)
elif (muv == "/"):
    print(szam1/szam2)
elif (muv == "*"):
    print(szam1*szam2)
else:
    print("Nem műveleti jelet adtál meg!")