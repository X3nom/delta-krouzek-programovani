
# Práce s Listy v Pythonu

Tento úkol je zaměřen na procvičení práce s **listy** (seznamy) v Pythonu. Naučíš se, jak přidávat, odebírat a manipulovat s prvky v seznamu.

---

## Zadání

1. **Vytvoř seznam:**
   - Vytvoř prázdný seznam s názvem `moje_seznam`.

2. **Přidávání prvků do seznamu:**
   - Přidej do seznamu postupně následující položky:
     - `"jablko"`
     - `"banán"`
     - `"hruška"`

   Použij metodu `append()`.

3. **Vložení prvku na konkrétní místo:**
   - Přidej `"pomeranč"` na druhou pozici (index 1). Použij metodu `insert()`.

4. **Odebrání prvku:**
   - Odstraň `"banán"` ze seznamu. Použij metodu `remove()`.

5. **Odebrání posledního prvku:**
   - Odstraň poslední prvek seznamu a ulož ho do proměnné `posledni_prvek`. Použij metodu `pop()`.

6. **Změna hodnoty:**
   - Změň hodnotu na prvním místě seznamu (index 0) na `"ananas"`.

7. **Vypsání seznamu:**
   - Vypiš celý seznam pomocí funkce `print()`.

8. **Zjištění délky seznamu:**
   - Zjisti a vypiš počet prvků v seznamu pomocí funkce `len()`.

---

## Očekávaný výstup

Po splnění všech kroků by měl program vytvořit a upravit seznam podle následujícího procesu:

1. **Po přidání prvků:**  
   `["jablko", "banán", "hruška"]`

2. **Po vložení "pomeranče" na druhou pozici:**  
   `["jablko", "pomeranč", "banán", "hruška"]`

3. **Po odebrání "banánu":**  
   `["jablko", "pomeranč", "hruška"]`

4. **Po odstranění posledního prvku (uloženého v `posledni_prvek`):**  
   `["jablko", "pomeranč"]`

5. **Po změně prvního prvku na "ananas":**  
   `["ananas", "pomeranč"]`

6. **Výpis počtu prvků:**  
   `Počet prvků v seznamu: 2`

---

## Bonus

1. **Vyprázdnění seznamu:**
   - Vymaž celý seznam pomocí metody `clear()`.

2. **Kontrola prázdného seznamu:**
   - Zjisti, zda je seznam prázdný, a vypiš odpovídající zprávu (`"Seznam je prázdný."` nebo `"Seznam obsahuje prvky."`).
