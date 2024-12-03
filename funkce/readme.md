# Funkce

- můžeme si kus kódu zabalit pod jméno a potom ho "volat"
- POZOR, kód v funkci je odříznutý od zbytku programu (můžu mít např. proměnnou `a` v funkci i v programu ale budou to různé proměnné)

## Jak je psát
- využijeme `def` *= definujeme funkci*
- po `def` následuje námi vybraný název funkce
- po názvu funkce je `():`. 
\
Do závorky můžeme dát "parametry" = proměnné, skrz které můžeme dostat dovnitř funcke data

příklad funkce:
```python
def moje_funkce():
    print("hello world")
    print("toto je moje funkce")
```
V příkladu jsme "nadefinovali" funkci `moje_funkce` a "zabalili" do ní kód, který nám vypíše `"hello world"` a `"toto je moje funkce"`


Pokud cheme funkci "zavolat" (provést kód, který je v ní), musíme napsat jméno funkce se závorkami.
```python
moje_funkce() # provede funkci
```

## parametry
Parametry jsou proměnné, které funkci můžeme předat

Parametr nemusí být žádný (jako v příkladu pro `moje_funkce` nahoře), nebo jich může být kolik jen chcete

například:
```python
def pozdrav(jmeno, prijmeni):
    print("ahoj ", jmeno, " ", prijmeni)
```
pokud potom zavoláme
```
pozdrav("John", "Smith")
```
výstup bude
```
ahoj John Smith
```

## return
Funkce nám také může "vracet" hodnotu

Aby jsme výslednou hodnotu funkce vrátili použijeme `return`

příklad:
```python
def secti_dve_cisla(cislo_1, cislo_2):
    vysledek = cislo_1 + cislo_2
    return vysledek
```
pokud zavoláme:
```python
print(secti_dve_cisla(1,2))
```
program nám vypíše:
```
3
```

## odříznutí

```python
a = 10

def vypis_promennou(a):
    print(a)


b = 5

vypis_promennou(b)
```
výpis programu:
```
5
```
Vypsalo se 5 i když nahoře v programu bylo `a = 10` a ve funkci je `print(a), proč?

- `a = 10` je **mimo** funkci, zatímco `a`, které vypisujeme pomocí `print(a)` je **uvnitř** funkce, jedná se tudíž o jinou proměnnou.