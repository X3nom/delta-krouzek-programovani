# Jednoduché úlohy na procvičení funkcí v Pythonu

Níže najdeš pět jednoduchých úloh, které tě naučí vytvářet a používat funkce.  
Po splnění úlohy si můžeš výsledek zkontrolovat vytištěním (`print`) návratové hodnoty funkce.

## 1. Funkce pro pozdrav

**Zadání:**  
Napiš funkci `pozdrav()`, která nic nepřijímá, pouze vrací řetězec `"Ahoj!"`.  
Poté funkci zavolej a její návratovou hodnotu vytiskni.

**Nápověda:**  
- Použij `def pozdrav():`
- Funkce nepotřebuje žádný argument, jen vrátí řetězec: `return "Ahoj!"`

## 2. Funkce, která vrátí dvojnásobek čísla

**Zadání:**  
Napiš funkci `dvojnasobek(cislo)`, která přijme jedno číslo a vrátí jeho dvojnásobek.

**Nápověda:**  
- Např. `dvojnasobek(3)` by mělo vrátit `6`.

## 3. Funkce, která vrátí první prvek seznamu

**Zadání:**  
Napiš funkci `prvni_prvek(seznam)`, která zadanému seznamu vrátí jeho první prvek.  
Pokud je seznam prázdný, ať funkce vrátí `None`.

**Nápověda:**  
- Zkontroluj, zda je seznam prázdný pomocí `if not seznam:`
- Pokud ne, vrať `seznam[0]`.

## 4. Funkce, která sečte dvě čísla

**Zadání:**  
Napiš funkci `secti(a, b)`, která vrátí součet dvou čísel `a` a `b`.

**Nápověda:**  
- Např. `secti(10, 5)` by mělo vrátit `15`.

## 5. Funkce, která řekne, zda je číslo sudé

**Zadání:**  
Napiš funkci `je_sude(cislo)`, která vrátí `True`, pokud je číslo sudé, jinak `False`.

**Nápověda:**  
- Sudé číslo má zbytek po dělení 2 roven 0: `cislo % 2 == 0`.