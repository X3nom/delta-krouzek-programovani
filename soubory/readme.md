# Soubory


zapisování do souboru:
```py

f = open("mujsoubor.txt", "w")

f.write("ahoj")

f.close()


```


čtení souboru:
```py

f = open("mujsoubor.txt", "r")

obsah = f.read()

print(obsah) # ahoj

```


# Cesty

## Absolutní cesta
Vede od začátku disku (`C:\Users\....`)

## Relativní
Vede od místa, kde je program spuštěn.

Pokud 