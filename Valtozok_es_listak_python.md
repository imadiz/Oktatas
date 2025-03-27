# Változók és listák Pythonban

## 1. Változótípusok Pythonban

Pythonban a változók típusát automatikusan kezeli az értékük alapján.

| Típus | Példa | Leírás |
|-------|-------|--------|
| `int` | `x = 10` | Egész szám |
| `float` | `y = 3.14` | Tört szám |
| `str` | `nev = "Python"` | Szöveg (karakterlánc) |
| `bool` | `igaz = True` | Logikai érték |
| `list` | `lista = [1, 2, 3]` | Lista (tömbszerű) |
| `set` | `halmaz = {1, 2, 3}` | Egyedi elemek halmaza |

### Példák a különböző változótípusokra
```
python
egesz = 42
tort = 3.14
szoveg = "Hello, világ!"
logikai = True
lista = [1, 2, 3, 4, 5]
halmaz = {1, 2, 3}

print(type(egesz))  # <class 'int'>
print(type(tort))   # <class 'float'>
print(type(szoveg)) # <class 'str'>
```

---

## 2. A változók tulajdonságai

### Változók elnevezése
- A változó neve **betűvel vagy aláhúzással (`_`)** kell kezdődjön.
- Nem tartalmazhat szóközt és speciális karaktereket (kivéve `_`).
- Python kis- és nagybetűérzékeny (`valtozo` és `Valtozo` különböző!).

**Példa helyes változónevekre:**
```python
nev = "Anna"
eletkor = 25
_auto_tipus = "Toyota"
```

**Helytelen változónevek:**
```python
2eletkor = 25  # Nem kezdődhet számmal!
auto-típus = "Ford"  # Nem használhat kötőjelet!
```

### Típuskonverzió
Pythonban a változók típusát megváltoztathatjuk:

```python
x = "123"
y = int(x)  # Szövegből egész szám lesz

a = 5
b = float(a)  # Egész számból tört szám lesz

print(type(y))  # <class 'int'>
print(type(b))  # <class 'float'>
```

---

## 3. Listák (`list`)

A listák **több értéket** tárolnak egy változóban. A lista elemei módosíthatók.

### Lista létrehozása és indexelése
```python
gyumolcsok = ["alma", "banán", "cseresznye"]

print(gyumolcsok[0])  # alma
print(gyumolcsok[-1])  # cseresznye (utolsó elem)
```

### Lista módosítása
```python
gyumolcsok[1] = "körte"  # banán helyett körte kerül a listába
```

### Lista műveletek
```python
gyumolcsok.append("szőlő")  # Új elem hozzáadása a végére
gyumolcsok.insert(1, "eper")  # Új elem beszúrása adott indexre
gyumolcsok.remove("alma")  # Elem eltávolítása
utolso = gyumolcsok.pop()  # Utolsó elem eltávolítása és visszaadása
```

### Lista bejárása
```python
for gyumolcs in gyumolcsok:
    print(gyumolcs)
```

### Listaműveletek
```python
szamok = [5, 2, 9, 1]

szamok.sort()  # [1, 2, 5, 9] – Növekvő sorrend
szamok.reverse()  # [9, 5, 2, 1] – Fordított sorrend

hossz = len(szamok)  # Lista hossza
```

---

## 4. Összefoglalás

- **Változók** lehetnek különböző típusúak (`int`, `float`, `str`, `bool`, stb.).  
- **A változók neve** nem kezdődhet számmal, nem tartalmazhat szóközt vagy speciális karaktert (kivéve `_`).  
- **A listák** több értéket tárolnak és módosíthatók.  
- A listák **indexeléssel** érhetők el, és különböző műveletek végezhetők rajtuk (`append()`, `remove()`, `sort()`, stb.).  
