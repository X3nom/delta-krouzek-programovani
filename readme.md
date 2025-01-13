# Krouzek programovani
Nahoře jsou ve složkách materiály z hodin, stačí se do nich prokliknout



## Proměnné

### Operátory

= - ulož do

### Definice
```python
nazev_podminky = hodnota
```



hodnota bude např číslo(1) nebo text("Ahoj")

## Podmínka

### Operátory

== - hodnoty se rovnají <br>
\> - větší než <br>
< - Menší než <br>
\>= - větší rovno <br>
<= - menší rovno <br>

### Definice
```python
if(podminka):
    # to co se má udělat pokud je podmínka pravda
else():
    # to co se má udělat pokud podmínka není pravda

```

např:
```python
vstup = int(input())

if(vstup==1):
    print("pravda")
else:
    print("nepravda")
```
## Cykly

### While
Opakuje se dokud je podmínka pravda

```python
while(prodminka):
    # Tenhle kus kódu se bude dělat dokud je podmínka pravda
```


### For
Projde každy prvek v seznamu for i in seznam: ==> pro každý v seznamu

```python
seznam = [1,5,6,7]

for i in seznam:
    if(i>5):
        print("číslo " + i + " je větší než 5")
    else:
        print("číslo" + i + " není větší než 5")
```

Můžeme je použít jako jednoduché počítání
```python
# vypíše čísla od 0 do 9
for i in range(10):s
    print(i)
```


## Seznam (list)
Představte si je jako více poměnných v jedné.

```python
muj_list = [3,1,4]
# muj list je list o délce 3, který obsahuje čísla 3, 1 a 4
```

K hodnotě v listu přistupujeme pomocí "indexu" - pozice, na které se nachází.

Indexy začínají od 0 => první prvek v seznamu je na indexu 0, druhý je na indexu 1, ...


```python
muj_list = [3,1,4]

print(muj_list[0]) # vypise 3 (prvek listu na 2. pozici)
print(muj_list[1]) # vypise 1 (prvek listu na 2. pozici)
```
Kromě výpisu lze samozřejmě na index i *zapisovat*. To provedeme jako kdyby to byla kterákoli jiná proměnná.
```python
muj_list = [3,1,4]

print(muj_list) # [3, 1, 4]

muj_list[1] = 999

print(muj_list) # [3, 999, 4]
```

Do listu můžeme přidávat nové hodnoty pomocí `.append(<co chci přidat>)` a odebírat pomocí `.pop(<index, který chci odstranit>)`

```python
muj_list = [3, 2, 4]

print(muj_list) # [3, 2, 4]

muj_list.append(6)

print(muj_list) # [3, 2, 4, 6]

odebrana_hodnota = muj_list.pop(1)

print(odebrana_hodnota) # 2

print(muj_list) # [3, 4, 6]

```