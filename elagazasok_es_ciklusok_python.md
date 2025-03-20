# Elágazások és ciklusok Pythonban

## 1. Elágazások (`if`-`elif`-`else`)
Az elágazások segítségével a program különböző utakon haladhat attól függően, hogy egy feltétel igaz vagy hamis.

### Példa: Egyszerű elágazás
```
python
szam = int(input("Adj meg egy számot: "))

if szam > 0:
    print("A szám pozitív.")
elif szam < 0:
    print("A szám negatív.")
else:
    print("A szám nulla.")
```

## 2. Ciklusok

### `for` ciklus
A `for` ciklus egy lista vagy egy számtartomány elemein végiglépked.

**Lista bejárása:**
```python
gyumolcsok = ["alma", "banán", "cseresznye"]

for gyumolcs in gyumolcsok:
    print(gyumolcs)
```

**Számláló ciklus (`range()`):**
```python
for i in range(5):  # 0-tól 4-ig fut
    print(i)
```

### `while` ciklus
A `while` ciklus addig ismétlődik, amíg a feltétel igaz marad.

```python
szam = 5

while szam > 0:
    print(szam)
    szam -= 1

print("Bumm!")
```

### Ciklusvezérlő utasítások
- `break` – kilép a ciklusból.
- `continue` – kihagyja az aktuális iterációt, de a ciklus folytatódik.

**Példa `break`-re:**
```python
for szam in range(10):
    if szam == 5:
        break
    print(szam)
```

**Példa `continue`-ra:**
```python
for szam in range(5):
    if szam == 2:
        continue
    print(szam)
```

## 3. Feltételek helyessége

### Logikai operátorok
Pythonban a feltételek mindig **igaz (`True`) vagy hamis (`False`)** értéket adnak vissza.

| Operátor | Leírás |
|----------|--------|
| `==` | Egyenlőség |
| `!=` | Nem egyenlő |
| `>` | Nagyobb mint |
| `<` | Kisebb mint |
| `>=` | Nagyobb vagy egyenlő |
| `<=` | Kisebb vagy egyenlő |

### Hibás és helyes feltételek
```python
szam = 10

if szam = 10:  # HIBÁS! (= értékadás, nem összehasonlítás)
    print("A szám 10.")

if szam == 10:  # HELYES!
    print("A szám 10.")
```

### Logikai műveletek (`and`, `or`, `not`)
```python
# AND művelet
if szam > 10 and szam < 20:
    print("A szám 10 és 20 között van.")

# OR művelet
szin = "piros"
if szin == "piros" or szin == "kék":
    print("A szín piros vagy kék.")

# NOT művelet
esik = False
if not esik:
    print("Nem esik az eső.")
```

### Feltételek tesztelése
Ha egy feltétel nem működik jól, írjuk ki az értékét:
```python
szam = 7
print(szam > 10)  # Kiírja: False

if szam > 10:
    print("Nagyobb mint 10.")
```

### Tippek a helyes feltételekhez
✅ Mindig használj **összehasonlító operátort** (`==`, `!=`, `>`, stb.).  
✅ Ha több feltételt kombinálsz, gondold végig a **logikai kapcsolatokat**.  
✅ Használj `print()`-et vagy `debugger`-t, ha nem azt kapod, amit vártál.
