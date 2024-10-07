# 7.10

## co je to program
Set příkazů které se postupně po sobě provádějí a říkají tak počítači co dělat.
\
Program postupuje po řádcích od zhora dolů a instrukce na nich provádí.


## základní funkce pro vstup a výstup
- `print()` - vypíše obsah v závorkách
    - př.1: `print("hello world")` -> `hello world`
    - př.1: `print(10)` -> `10`

- `input()` - dá nám text, který uživatel do programu zadá
    - př.1: `vstup = input("zadej tvoje jmeno: ")` -> napíše `zadej tvoje jmeno: `, po zadání jména (například `Jakub`) a enteru bude v proměnné uloženo toto jméno. 
    - př.2: `vstup = input()` *do input() žádnou zprávu zadávat nemusíme a bude i přes to fungovat*

## proměnná
Místo v programu, kam si můžu uložit nějakou hodnotu (například číslo 10 nebo text "Ahoj") se jmenuje proměnná.
\
V pythonu proměnnou deklarujeme tímto způsobem: `jméno_proměnné = hodnota_proměnné`
\
*příklad v pythonu:*
```
moje_promenna = 10

moje_promenna_2 = "Ahoj"

moje_promenna_3 = 1.5
```
pod jménem moje_promenna je nyní uloženo číslo 10, to samé platí pro druhou proměnnou s textem "Ahoj" a třetí s 1.5

## typy
Proměnné *(a vlastně všechna data v počítači)* mají nějaký **typ**.
\
Typ nám udává zda se jedná o celé číslo, desetinné číslo, text, ...
- Základní typy:
    - **int** *(celé číslo)*
    - **float** *(číslo s desetinnou čárkou)*
    - **string** *(textový řetězec)*
    - ...

### zápis v pythonu
- string - text zapisujeme uvnitř uvozovek. Je možné použít jak uvozovky dvojité (" ") tak jednoduché (' ')
- int a float - zapisujeme jako normální číslo
\
**POZOR: používá se desetinná tečka, ne čárka**


## matematické operace
symboly:

- `+` - sčítání
- `-` - odčítání
- `*` - násobení
    - `**` - mocnina
- `/` - dělení
    - `//` - celočíselné dělení
    - `%` - zbytek po celočíselném dělení *(modulo)*