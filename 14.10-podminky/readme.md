# Větvení
- `if` = podmínka pokud je něco pravda (*například* `x == 1`), proveď kód uvnitř if
  
- `else` = můžeme ho napsat po podmínce `if`, znamená to, že pokud se podmínka nesplní, tak se staně to co je zapsané zde
  
- `elif` = kombinace `if` a `else` v českém jazyce by se toto dalo nahradit slovy `a nebo`


## porovnávací operátory
+ porovnávací operátory používané při zapisovaní podmínek do -> `if`, `elif`  

|Porovnávací operátory|Vysvětlivky|
|---------------------|-----------| 
|`==`|Vrací `True` pokud se obě strany rovnají|
|`<`|Vrací `True` pokud je levá strana menší než druhá|
|`>`|Vrací `True` pokud je pravá strana menší než levá|
|`<=`|Vrací `True` pokud je levá strana menší nebo se rovná právé|
|`>=`|Vrací `True` pokud je pravá strana menší nebo se rovná levé|

## Logické operátory
+ Logické operátory se v psaní podmínek používají na spojení a propojení vícero podmínek najednou
+ zapisuje se do `if` -> `if příklad == True and příklad_2 == True`: pokud jsou tyto podmínky splněné vrací => `True`, ale pokud jedno není vrací => `False`
                                

|Logické operátory|Vysvětlivky|
|-----------------|-----------|
|`and`| propojí podmíky, tak že se musí splnit obě př.: přeložilo by se jako, `a`|
|`or`| Propojí podmínky, tak že se musí splnit jen jedna př.: přeložilo by se jako, `nebo` | 
|`not`| vrací negovaný tvar (opak) př.: `or not` přeložilo by se jako, `nebo ne`|