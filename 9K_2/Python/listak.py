gyumolcsok = ["alma", "banán", "körte"]
print(len(gyumolcsok)) #Lista elemek számát írja ki
print(gyumolcsok) #Listát írja ki
print(gyumolcsok[0])
print(gyumolcsok[1])
print(gyumolcsok[2])

gyumolcsok.append("durian")

for gyum in gyumolcsok:
    print(gyum)