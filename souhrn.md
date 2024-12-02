
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