#--------------------------
'''
A teglalap_atloja nevű függvény, 
bemenetként megkapja az oldalak hosszát és 
az átló hosszával tér vissza.
'''
def teglalap_atloja(a, b):
    return (a**2+b**2)**0.5


#--------------------------
'''
A paros nevű függvény,
egy számot kap bemenetként, 
majd True-val tér vissza, ha a szám páros és 
False-al ha a szám páratlan.
'''
def paros(szam):
    if (szam%2==0):
        return True
    else:
        return False


#--------------------------
'''
A teglatest_terfogat nevű függvény, 
bemenetként megkapja a téglatest oldalainak hosszúságát és 
a téglatest térfogatával tér vissza.
'''

def teglatest_terfogat(a,b,c):
    return a*b*c


#--------------------------
'''
A kocka_terfogat nevű függvény,
bemenetként megkapja a kocka oldal hosszúságát és 
a kocka térfogatával tér vissza.
'''

def kocka_terfogat(a):
    return a**3

#--------------------------
'''
A derekszogu_haromszog_terulet nevű függvény, 
bemenetként megkapja a befogók hosszát és 
a háromszög területével tér vissza.
'''

def derekszogu_haromszog_terulet(a, b):
    return a * b / 2

#--------------------------
'''
A negyzet_kerulet nevű függvény, 
egy négyzet oldalhosszát kapja bemenetként és 
visszatér a négyzet kerületével.
'''

def negyzet_kerulet(a):
    return a*4


#--------------------------
'''
A negyzet_terulet nevű függvény,
egy négyzet oldalhosszát kapja bemenetként és 
visszatér a négyzet területével.
'''

def negyzet_terulet(a):
    return a**2


#--------------------------
'''
A kor_kerulete nevű függvény 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör kerületével.
'''

def kor_kerulete(r):
    import math
    return 2*r*math.pi

#--------------------------
'''
A harommal_oszthato nevű függvény,
egy számot kap bemenetként és 
True-val tér vissza, ha a szám hárommal osztható és 
False-al ha nem.
'''

def harommal_oszthato(szam):
    if(szam%3==0):
        return True
    else:
        return False

#--------------------------
'''
A kisebb nevű függvény,
két számot kap és 
visszatér a kisebbik számmal.

Nem használhatod a min nevű függvényt

'''

def kisebb(szam1, szam2):
    if(szam1 < szam2):
        return szam1
    else:
        return szam2

#--------------------------
'''
A kor_terulete nevű függvény, 
bemenő paraméterként kapja a kör sugarát és 
visszatér a kör területével.
'''

def kor_terulete(r):
    import math
    return r**2 * math.pi

#--------------------------
'''
A negyzet_atloja nevű függvény, 
bemenetként megkapja a négyzet oldalának hosszát és 
az átló hosszával tér vissza.
'''

def negyzet_atloja(a):
    return (a**2+a**2)**0.5


#--------------------------
'''
A hettel_oszthato nevű függvény, 
egy számot kap bemenetként és 
True-val tér vissza, ha a szám héttel osztható és 
False-al ha nem.
'''

def hettel_oszthato(szam):
    if(szam%7==0):
        return True
    else:
        return False

#--------------------------
'''
A derekszogu_haromszog_atfogo nevű függvény, 
bemenetként megkapja a befogók hosszát és 
az átfogó hosszával tér vissza.
'''

def derekszogu_haromszog_atfogo(a, b):
    return (a**2+b**2)**0.5


#--------------------------
'''
A kettovel_oszthato nevű függvény, 
egy számot kap bemenetként és 
visszatér True-val, ha a szám kettővel osztható és 
visszatér False-al ha a szám kettővel nem ossztható.
'''

def kettovel_oszthato(szam):
    if(szam%2==0):
        return True
    else:
        return False

#--------------------------
'''
A maradek nevű függvény,
két számot kap bemenetként és 
visszatér a két szám hányadosának maradékával.
'''

def maradek(szam1, szam2):
    return szam1 % szam2

#--------------------------
'''
Az abszolut nevű függvény, 
a bemenő paraméterként kapott szám 
abszolút értékével tér vissza.
'''

def abszolut(szam):
    if(szam < 0):
        return -szam
    else:
        return szam


#--------------------------
'''
Az osszead nevű nevű függvény,
két számot kap és 
visszatér a két szám összegével.

Nem használhatod a sum nevű függvényt!
    
'''

def osszead(a,b):
    return a+b


#--------------------------
'''
A teglalap_kerulet nevű függvény, 
egy téglalap oldalhosszait kapja bemenetként és 
visszatér a téglalap kerületével.
'''

def teglalap_kerulet(a,b):
    return (a+b)*2

#--------------------------
'''
A kulonbseg nevű függvény,
két számot kap bemenetként és 
visszatér a két szám különbségével.
'''

def kulonbseg(szam1, szam2):
    return szam1 - szam2


#--------------------------
'''
A nagyobb nevű függvény,
két számot kap és 
visszatér a nagyobb számmal.

Nem használhatod a max nevű függvényt.
'''

def nagyobb(szam1, szam2):
    if(szam1 > szam2):
        return szam1
    else:
        return szam2


#--------------------------
'''
A teglalap_terulet nevű függvény,
egy téglalap oldalhosszait kapja bemenetként és 
visszatér a téglalap területével.
'''

def teglalap_terulet(a, b):
    return a * b


#--------------------------
'''
A szamtani_kozep nevű függvény, 
két számot kap és 
visszatér a számtani középpel.
'''

def szamtani_kozep(a,b):
    return (a + b) / 2

#======================================================================================================================/home/adiz/Repos/Oktatas/10K_2/Python/10k2-0224p1-446ce4e7-tesztelok-0224p1-python1