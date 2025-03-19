import pytest, cssutils, os, bs4

def get_html():
    with open("index.html", encoding="utf-8") as f: #HTML fájl beolvasása
        return bs4.BeautifulSoup(f, 'html.parser') #Visszadobás egyben
    
def get_css():
    with open("style.css", encoding="utf-8") as f: #CSS fájl beolvasása
        css = cssutils.parseString(f.read())
        return [x for x in css.cssRules if x.type == x.STYLE_RULE]#Visszadobás egyben

def test_file_structure():
    expected = ["index.html",
                "style.css", 
                "szoveg.txt", 
                "hetfo_csirkecomb.jpg", 
                "kedd_makosteszta.jpg", 
                "szerda_halaszle.jpg", 
                "csutortok_rantotthus.jpg",
                "pentek_borsofozelek.jpg"] #Az elvárt fájlstruktúra
    
    files = os.listdir("./") #Helyi fájlok listája
    for f in expected:
        assert files.__contains__(f), f"A hiányzik a(z) {f} fájl!" #Az elvárt és jelenlegi struktúra összehasonlítása, ha hiányzik a jelenlegiből akkor AssertionError

#Fájlok beolvasása/átalakítása
html_soup = get_html() #bs4 html oldal
css_list = get_css() #cssutils lista

#Megjegyzések:
#Ha CSS-t kell ellenőrizni, a GetPropertyValue függvényt csináltam hozzá.
#Egyszerű a használata: Az első paramétere a css selector, a második a tulajdonság,
#és ha mind a kettő létezik, akkor visszadobja az értéket, amit lehet assert-el ellenőrizni.

#Ha HTML-t kell ellenőrizni, akkor a html_soup.find-al lehet
#elementet keresni, első paramétere az element típusa.
#A második paramétere lehet class, id, stb.
#A class-okat (és gondolom az id-kat is) listaként dobja vissza,
#szóval az első elemre kell ellenőrizni, ha csak egy class van megadva.
#A .name tulajdonság az element típusát adja vissza.
#Az elementek pozícióját személy szerint én az előző/következő elementekkel ellenőrzöm,
#és ha kell akkor a parent/children-el is.

def GetPropertyValue(selector: str, propName: str):
    assert any(x for x in css_list if x.selectorText == selector), f"Nincs {selector} osztály!" #Osztály létezés ellenőrzés
    assert next(x for x in css_list if x.selectorText == selector).style.getPropertyValue(propName), f"Nincs {propName} tulajdonság!" #Tulajdonság ellenőrzés az osztályban
    return next(x for x in css_list if x.selectorText == selector).style.getPropertyValue(propName) #Tulajdonság értékének visszadobása

#Feladatok
@pytest.mark.points(1)
def test_feladat_1():
    assert GetPropertyValue("body", "color") == "#006", "Helytelen az oldal betűszíne!"
    assert GetPropertyValue("body", "background-color") == "#EF6", "Helytelen a beállított háttérszín!"

@pytest.mark.points(1)
def test_feladat_2():
    assert GetPropertyValue("body", "font-style") == "italic", "Nincs dőlt beállítás az oldalon!"

@pytest.mark.points(1)
def test_feladat_3():
    assert GetPropertyValue("body", "width") == "50%", "Helytelen az oldal szélessége!"
    assert GetPropertyValue("body", "margin") == "auto", "Nincs középre igazítva az oldal!" 

@pytest.mark.points(2)
def test_feladat_4():
    assert html_soup.find("h1") != None, "Nem létezik egyes szintű fejezetcím!"
    assert html_soup.find("h1").text == "Heti étlap", "Helytelen a cím szövege!"
    #Meg kell nézni, hogy hol van pontosan a h1, ebben az esetben a body-nak 
    #konkrét leszármazottja, és az első. (Mindkettőt tudja a bs4)

@pytest.mark.points(2)
def test_feladat_5():
    assert html_soup.find(class_="hetek") != None, "Nem létezik hetek osztály az oldalon!"
    assert html_soup.find(class_="hetek").name == "div", "A hetek osztályú elem nem div!"

@pytest.mark.points(2)
def test_feladat_6():
    elems = [("a", "Előző hét"),
             ("span", "Aktuális hét"),
             ("a", "Következő hét")]
    
    for tag, text in elems:
        assert html_soup.find(class_="hetek").find(name=tag) != None, f"Nem létezik {tag} típusú elem a .hetek div-ben!"
        assert html_soup.find(class_="hetek").find(name="span") != None, f"Nem létezik olyan elem a .hetek div-ben, aminek a szövege '{text}' lenne!"

@pytest.mark.points(1)
def test_feladat_7():
    assert GetPropertyValue(".hetek", "display") == "flex", "Nincs flex rendezés a .hetek kiválasztón!"
    assert GetPropertyValue(".hetek", "justify-content") == "space-evenly", "Helytelen a rendezés módja!"

@pytest.mark.points(1)
def test_feladat_8():
    assert GetPropertyValue("hr", "background-color") == "red", "Helytelen/hiányzik a háttérszín beállítás!"
    assert GetPropertyValue("hr", "border-color") == "red", "Helytelen/hiányzik a szegélyszín beállítás!"

@pytest.mark.points(1)
def test_feladat_9():
    prev_sibl = None #Előző element
    target = None #Keresett element
    next_sibl = None #Következő element

    target = html_soup.find("hr")
    prev_sibl = target.find_previous_sibling()
    next_sibl = target.find_next_sibling()

    assert isinstance(target, bs4.Tag), "Nem található hr elem az oldalon!"
    assert prev_sibl.get("class")[0] == "hetek", "Helytelen a hr elem elhelyezése!"
    assert next_sibl.name == "hr", "Hiányzik a második hr elem!"

@pytest.mark.points(2)
def test_feladat_10():
    target = None

    target = html_soup.find(class_="egynap")
    children = target.findChild("div")

    assert isinstance(target, bs4.Tag), "Nincs egynap osztályú elem!"
    assert target.name == "div", "Az egynap osztályú elem nem div típusú!"
    assert target.find_previous_siblings()[0].name == "hr", "Helytelen az egynap elem elhelyezése!"
    assert target.find_previous_siblings()[1].name == "hr", "Helytelen az egynap elem elhelyezése!"

    assert children.name == "div", "Nem div az egynap elem első eleme!"
    assert children.find_next_sibling().name == "img", "Nem img az egynap elem második eleme!"