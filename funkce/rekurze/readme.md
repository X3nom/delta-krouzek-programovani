# Rekurze
= Funkce, která volá sama sebe

například:
```python
def numbers_to_infinity(n):
    print(n)
    numbers_to_infinity(n+1)


numbers_to_infinity(0)
```
by začalo vypisovat čísla od 0 do "nekonečna":
```
0
1
2
3
...
```
V programu jsme zavolali funkci s `n=0`, ta nám vypíše `n` a zavolá sama sebe s `n=n+1`, ta opět zavolá sebe, ...

Úplně do neknečna ale tohle nejde, protože by nám velmi rychlo program spadl kvůli `RecursionError: maximum recursion depth exceeded` = funkce je zavolaná vícekrát, než to náš systém dovolí.

Proto je potřeba se vždy ujistit, že máme nějaký limit, při kterém se rekurze ukončí.