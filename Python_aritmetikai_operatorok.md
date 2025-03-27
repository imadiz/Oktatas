# **Python Tananyag: Aritmetikai Operátorok**  

## **Bevezetés**  
A Python programozási nyelv számos aritmetikai operátort támogat, amelyek segítségével matematikai műveleteket végezhetünk. Ezek az operátorok alapvetőek a számítások és az algoritmusok megírásában.  

---

## **1. Összeadás (`+`) és kivonás (`-`)**  
Az összeadás és kivonás az alapvető matematikai műveletek közé tartozik.  

### **Példa:**  
```python
a = 10
b = 5

osszeg = a + b  # 10 + 5 = 15
kulonbseg = a - b  # 10 - 5 = 5

print("Összeg:", osszeg)
print("Különbség:", kulonbseg)
```

### **Kimenet:**
```
Összeg: 15  
Különbség: 5  
```

---

## **2. Szorzás (`*`) és osztás (`/`)**  
A szorzás és osztás szintén gyakran használt műveletek.  

### **Példa:**  
```python
a = 6
b = 3

szorzat = a * b  # 6 * 3 = 18
osztas = a / b  # 6 / 3 = 2.0 (float eredmény)

print("Szorzat:", szorzat)
print("Osztás:", osztas)
```

### **Kimenet:**
```
Szorzat: 18  
Osztás: 2.0  
```

**Megjegyzés:** Az osztás (`/`) eredménye mindig **lebegőpontos szám** (float), még akkor is, ha a művelet egész számokkal történik.  

---

## **3. Hatványozás (`**`)**  
A hatványozás egy szám megemelését jelenti egy adott hatványra.  

### **Példa:**  
```python
alap = 2
kitevo = 3

eredmeny = alap ** kitevo  # 2^3 = 8

print("Hatvány eredménye:", eredmeny)
```

### **Kimenet:**
```
Hatvány eredménye: 8  
```

---

## **4. Egész osztás (`//`)**  
Az egész osztás során az eredmény csak az osztás **egész része**, a maradék elvész.  

### **Példa:**  
```python
a = 7
b = 3

egesz_osztas = a // b  # 7 // 3 = 2 (a maradék elvész)

print("Egész osztás eredménye:", egesz_osztas)
```

### **Kimenet:**
```
Egész osztás eredménye: 2  
```

**Megjegyzés:** Az eredmény mindig egész szám lesz (`int`), de ha lebegőpontos számokkal használjuk, akkor `float` lehet.  

---

## **5. Maradékos osztás (`%`)**  
A maradékos osztás az osztás után fennmaradó maradékot adja vissza.  

### **Példa:**  
```python
a = 7
b = 3

maradek = a % b  # 7 % 3 = 1 (mert 7 / 3 = 2 maradékkal 1)

print("Maradékos osztás eredménye:", maradek)
```

### **Kimenet:**
```
Maradékos osztás eredménye: 1  
```

---

## **Összegzés**  
| Operátor | Leírás | Példa | Eredmény |
|----------|--------|-------|----------|
| `+` | Összeadás | `5 + 3` | `8` |
| `-` | Kivonás | `5 - 3` | `2` |
| `*` | Szorzás | `5 * 3` | `15` |
| `/` | Osztás | `5 / 2` | `2.5` |
| `**` | Hatványozás | `2 ** 3` | `8` |
| `//` | Egész osztás | `5 // 2` | `2` |
| `%` | Maradékos osztás | `5 % 2` | `1` |

Ezek az operátorok alapvetőek a Python programozásban, és minden matematikai számításhoz használhatók.
