# Úkoly - funkce


## 1. Pozdrav
Napiš funkci `pozdrav`, tak aby:
```python
pozdrav("Jakub")
```
vypsalo:
```
ahoj Jakub
```


## 2. Součet
Napiš funkci `secti`, která bere jako parametry čísla `a` a `b` a vrátí jejich součet
\
Pokud zavoláme například:
```python
soucet = secti(5,8)
print(soucet)
```
program by měl vypsat:
```
13
```


## 3. Funkce, která řekne, zda je číslo sudé
Napiš funkci `je_sude(cislo)`, která vrátí `True`, pokud je číslo sudé, jinak `False`.

program:
```python
print(je_sude(10))
print(je_sude(3))
print(je_sude(0))
```
by vypsal:
```
True
False
True
```


## 4. Podíl
Napiš funkci `vydel`, která bere jako parametry čísla `a` a `b` a vypíše jejich podíl. (`a / b`)

V případě, že je `b` 0, vypište místo podílu `Nulou nelze delit!`

program:
```python
vydel(6, 3)
vydel(8, 0)
```
by vypsal:
```
2
Nulou nelze delit!
```


## 5. Funkce, která vrátí první prvek seznamu
Napiš funkci `prvni_prvek(seznam)`, která zadanému seznamu vrátí jeho první prvek.  
Pokud je seznam prázdný, ať funkce vrátí `None`.
> tip: zjistěte délku seznamu pomocí `len(seznam)`

progam:
```python
print(prvni_prvek([8,3,4,5]))
print(prvni_prvek([]))
```
by vypsal:
```
8
None
```

