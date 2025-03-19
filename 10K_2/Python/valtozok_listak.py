sörök = ["köbi", "ászok", "arany fácán", "meggyes borsodi", "corona", "dreher", "soproni", "miller"]
kedvenc = ""

for sör in sörök:
    if(sör == "miller"):
        kedvenc = sör

keresett = input(f"Melyik a kedvenc betűd a {kedvenc}-ben? ")

megvane = False

for betu in kedvenc:
    if(betu == keresett):
        print("Megvan a kedvenc betűd te majom")
        megvane = True

if(megvane != True):
    print("Nincs meg a kedvenc betűd te telefosott búvárruha")