# HTML és CSS Alapjai

## Fájlkiterjesztések
- **`.html`** – A HTML dokumentumok kiterjesztése. Ebben a fájlban tároljuk a weboldal szerkezetét és tartalmát.
- **`.css`** – A CSS fájlok kiterjesztése. Ebben a fájlban definiáljuk a weboldal stílusát és megjelenését.

## HTML és CSS fájlok struktúrája
### HTML fájl szerkezete
A HTML egy jelölőnyelv, amely a weboldalak szerkezetét határozza meg. Az alábbi példa egy alap HTML dokumentumot mutat be:
```html
<!DOCTYPE html> <!-- Meghatározza a dokumentum típusát -->
<html lang="hu"> <!-- A teljes HTML dokumentum kezdete -->
<head> <!-- Fejléc, metaadatok és hivatkozások -->
    <meta charset="UTF-8"> <!-- A karakterkódolás beállítása -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> <!-- Reszponzív nézet beállítása -->
    <title>Dokumentum címe</title> <!-- A böngésző fülén megjelenő cím -->
    <link rel="stylesheet" href="styles.css"> <!-- Külső CSS fájl csatolása -->
</head>
<body> <!-- A weboldal látható tartalma -->
    <h1>Helló, világ!</h1> <!-- Főcím -->
    <p>Ez egy bekezdés.</p> <!-- Bekezdés -->
</body>
</html>
```

### CSS fájl szerkezete
A CSS (Cascading Style Sheets) a HTML dokumentumok formázására szolgál. Az alábbi példa egy egyszerű CSS fájlt mutat be:
```css
body {
    font-family: Arial, sans-serif; /* Betűtípus beállítása */
    background-color: #f4f4f4; /* Háttérszín */
    color: #333; /* Szöveg színe */
}

h1 {
    color: blue; /* A címsor színe */
}
```

## HTML tagek felépítése
Egy HTML elem három részből áll:
```html
<tag attribútum="érték">Tartalom</tag>
```
Példa egy hivatkozásra:
```html
<a href="https://example.com">Kattints ide</a>
```
- **`<a>`** – A HTML tag (hivatkozás elem)
- **`href`** – Attribútum, amely megadja a hivatkozás célját
- **`Kattints ide`** – Az elem tartalma, ami megjelenik a böngészőben

## CSS szelektorok felépítése
A CSS szelektorok meghatározzák, hogy mely HTML elemekre vonatkozik a stílus. Egy alap szelektor szerkezete:
```css
szelektor {
    tulajdonság: érték;
}
```
Példa:
```css
p {
    color: red; /* A bekezdés szövegszínének beállítása */
    font-size: 16px; /* Betűméret beállítása */
}
```

## Leggyakoribb HTML tagek
- `<h1>` – `<h6>` : Címsorok (h1 a legnagyobb, h6 a legkisebb)
- `<p>` : Bekezdés szövegekhez
- `<a>` : Hivatkozás más oldalakra vagy tartalmakra
- `<img>` : Képek beillesztése
- `<ul>`, `<ol>`, `<li>` : Rendezett és rendezetlen listák
- `<table>`, `<tr>`, `<td>` : Táblázatok létrehozása
- `<form>`, `<input>`, `<button>` : Űrlapelemek, például gombok és szövegmezők

## Leggyakoribb CSS tulajdonságok
- **Szövegstílusok**: 
  - `color` – Szöveg színe
  - `font-size` – Betűméret
  - `text-align` – Igazítás (balra, jobbra, középre stb.)
- **Háttér**: 
  - `background-color` – Háttérszín
  - `background-image` – Háttérkép
- **Elhelyezkedés és térközök**:
  - `margin` – Külső térköz (az elem és más elemek közötti távolság)
  - `padding` – Belső térköz (az elem tartalma és a széle közötti távolság)
  - `position` – Pozíció (pl. `absolute`, `relative`, `fixed`)
- **Méret**: 
  - `width` – Szélesség
  - `height` – Magasság
- **Szegélyek és árnyékok**:
  - `border` – Szegély beállítása
  - `box-shadow` – Árnyékhatás az elem körül

## CSS mértékegységek
A CSS-ben különböző egységekkel lehet méreteket megadni:
- **Abszolút egységek**: 
  - `px` – Pixel, egy képpontnyi méret
  - `pt` – Pont (nyomtatásban használatos)
  - `cm`, `mm` – Centiméter és milliméter
- **Relatív egységek**:
  - `em` – Az aktuális betűméret függvényében változik
  - `rem` – A gyökér elem (`html`) betűméretéhez viszonyított érték
  - `%` – Százalékos arány a szülő elem méretéhez képest
  - `vw`, `vh` – A nézetablak szélességéhez és magasságához viszonyított érték