# For cyklus
Jak název říká jedná se o další typ cyklu tkz. `for` loop

- `for` = omezeně opakující se cyklus

sám o sobě `for` nedělá nic musíme mu udat proměnnou a tkz. iterátor 

- `for i in můj_list` správný tvar pro for cyklus --> `for + proměnná + in + iterátor(třeba list)`

do for loopu píšeme proměnnou a tím ji také zakládáme jako kdyby jsme vytvářely novou. Do této nové proměnné vytvořené pro `for loop` potom ukládáme hodnoty kterýmy tkz. iterujeme

př:
```python
for i in range(10):
    print(i)
```
vypíše čísla od 0 do 9:
```
0
1
...
8
9
```
př:
```python
for cislo in [1,4,3]:
    print(cislo)
```
vypíše pod sebe prvky listu:
```
1
4
3
```