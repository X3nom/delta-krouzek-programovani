# Ukoly

## Pridej do listu
Uzivatel bude na vstup zadavat slova.

Pokazde se po zadani slovo prida do listu a cely list se vypise.

vstup:
```
ahoj
neco
```
vystup:
```
['ahoj']
['ahoj', 'neco']
```


## Odeber z listu
Uprav progam z ulohy `Pridej do listu` tak, aby se po zadani **3** slov misto dalsich slov zeptal na index prvku, ktery ma odstranit.

vstup:
```
ahoj
neco
treti
1
```
vystup:
```
['ahoj']
['ahoj', 'neco']
['ahoj', 'neco', 'treti']
['ahoj', 'treti']
```


## Najdi prvek v listu
Opet uprav program z 1. ulohy tak, aby po **3** zadanych slovech prestal slova pridavat.

Dalsi slova budou "hledani" - program vypise `nalezeno` nebo `nenalezeno` podle toho, zda slovo v seznamu je nebo neni.

vstup:
```
ahoj
neco
treti
ahoj
aohj
```
vystup:
```
['ahoj']
['ahoj', 'neco']
['ahoj', 'neco', 'treti']
nalezeno
nenalezeno
```



## Regisgtracni system

Napis system pro registraci jmen majitelu aut v servisu.

System se vzdy zepta na akci, kterou ma provest (uzivatel zada jedno pismeno)
- "P" - Pridej noveho majitele

- "N" - Najdi majitele