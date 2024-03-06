# Andreas Johannesson - SRP
## Neurale Netværk

Dette bibliotek er en samling af de filer benyttet i min SRP i den praktiske anvendelse af matematikken bag neurale netværk.

Funktionerne som tager sig af matrix matematikken findes i filen: matrix_math.py
Opbygningen af det neurale netværk findes i filen: NeuraltNetværk_simple.py

## Praktiske informationer 

### Nødvendige Python biblioteker
Selvom pointen med dette projekt er at bygge et neuralt netværk op fra bunden kræves der alligevel
et par eksterne biblioteker. Disse kan ses i filen requirements.txt og de kan installers således:

`pip install -r requirements.txt`

### Erfaringer

* Learning_rate skal være negativ da dette resultere i den negative gradient
* Vægtenes tilfældige startværdier kan ikke afrundes til 2 decimaler.
* Labels og startværdier skal initialiseres korrekt. Se seneste comit

## Log

### 6 Marts 2024
Efter utalige mislykkedes træninger er det lykkedes at træne et netværk med en succes rate på 86%