# Git Alapok - Parancssoros Használat

Ez a dokumentáció bemutatja a Git alapvető használatát a parancssorban (cmd). Segít az első Git tároló létrehozásában, a változások követésében és a kód feltöltésében GitHubra.

---

## 1️⃣ Git telepítése és beállítása

### **Telepítés**
A Git letölthető innen: [https://git-scm.com/](https://git-scm.com/)

### **Név és e-mail beállítása**
A következő parancsokkal beállíthatod a neved és e-mail címed:

```cmd
git config --global user.name "Saját Neved"
git config --global user.email "email@example.com"
```

Ez kötelező beállítás a git használata előtt, hiszen tudni kell a repo-nak, hogy ki módosítja.

---

## 2️⃣ Új Git tároló létrehozása (repository)
Ha egy projektet Git-tel szeretnél kezelni, lépj be a megfelelő mappába, majd inicializáld a Git-et:

```cmd
cd projekt_mappa
git init
```

Ez létrehoz egy rejtett `.git` mappát a projektben.

---

## 3️⃣ Fájlok hozzáadása a követéshez



Ha egy fájlt követni szeretnél:

```cmd
git add fájl_neve.txt
```

Az összes fájl hozzáadásához:

```cmd
git add .
```

---

## 4️⃣ Változások mentése (commit)
A változtatásokat egy üzenettel együtt kell elmenteni:

```cmd
git commit -m "Első commit: fájlok hozzáadva"
```

---

## 5️⃣ Változások ellenőrzése

**Módosítások állapotának megtekintése:**
```cmd
git status
```

**Előzmények listázása:**
```cmd
git log --oneline
```

---

## 6️⃣ GitHub tároló beállítása és feltöltés

### **Távoli tároló hozzáadása**
```cmd
git remote add origin https://github.com/felhasznalonev/repository.git
```

### **Fő ág átnevezése `main`-re**
```cmd
git branch -M main
```

### **Feltöltés a GitHubra**
```cmd
git push -u origin main
```

Ezek után a további frissítésekhez már elég a következő parancs:
```cmd
git push
```

---

## 7️⃣ Frissítések letöltése GitHubról
Ha más is dolgozik a projekten, frissítheted a fájlokat:

```cmd
git pull origin main
```

---

## 8️⃣ Korábbi verzióra visszaállás
Ha hibáztál, egy korábbi commit állapotára visszaállhatsz:

```cmd
git reset --hard commit_azonosító
```

A commit azonosítóját a `git log` paranccsal találod meg.

---

## 9️⃣ Fájl eltávolítása a Gitből
Ha egy fájlt törölni szeretnél a Git követéséből:

```cmd
git rm fájl_neve.txt
git commit -m "Fájl törölve"
```

---

## 🔹 Összegzés

Ezek a Git alapvető parancsai, amelyeket a parancssorban használhatsz a verziókezeléshez és a GitHubra való feltöltéshez. Ha kérdésed van, nézd meg a Git hivatalos dokumentációját: [https://git-scm.com/doc](https://git-scm.com/doc)

🚀 **Jó kódolást!**
