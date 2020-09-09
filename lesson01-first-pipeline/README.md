# Lekcja pierwsza — pierwszy pipeline

## Zadanie 1 — powłoka, CMD, terminal

1. Opis co to jest powłoka
2. Wyjaśnienie stosunku terminalu do powłoki
3. Uruchomienie CMD.exe
4. Polecenia cd i ls
5. Uruchomienie Terminala w VS Code
6. Polecenie mkdir

## Zadanie 2 — klonowanie repozytorium

1. Otworzyć VS code
2. Zainstalować plugin "Python"
3. Klonowanie repo
   1. Otworzyć ikonę kontroli wersji po lewej
   2. Kliknąć Clone Repository
   3. Wkleić link
   4. Otworzyć folder wklejony

## Zadanie 3 — hello world

1. Utworzyć plik hello-world.py
2. Otworzyć terminal
3. Uruchomić `python hello-world.py`
4. Wyjaśnienie — co to jest język interpretowany



## Zadanie 4 — zmienne

```python
a = 1
```

```python
a = 1
print a
```

```python
a = 1
print "Wartosc a wynosi: " + a
```

```python
a = 1
print "Wartosc a wynosi: " + str(a)
```

```python
b = 1.1
print "Wartosc b wynosi: " + str(b)
```

test kaczki = duck test:

> *If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck.*



```python
c = "tekst"
d = 5
print c
print c + str(d)
```



## Zadanie 5 — operacje

```python
c = a + b
```

```python
a = 1
b = 2
c = a + b + 5
print "Wartosc c wynosi: " + str(c)
```

```python
a = 1 * 10
print "Wartosc a wynosi: " + str(a)
```

```python
z = 10 / 50
print "Wartosc z wynosi: " + str(z)
```





## Zadanie 6 — funkcje

```python
def printHelloWorld():
  print "Hello world"

printHelloWorld()
printHelloWorld()
printHelloWorld()
```

```python
def printValue(name, value):
  print "Wartosc " + name + " wynosi: " + str(value)


pressure = 5
printValue("cisnienia", pressure)

printValue("temperatury", 36.6)

printValue("2 do potegi 3", 2 ** 3)
```

```python
def printBMI(weight, height):
  bmi = weight / (height ** 2)
  print "BMI wynosi " + str(bmi)

printBMI(75, 1.75)
```

```python
def calculateBMI(weight, height):
  return weight / (height ** 2)

bmi1 = calculateBMI(75, 1.75)
bmi2 = calculateBMI(70, 1.75)
spadekBMI = bmi1 - bmi2
print "BMI spadlo o " + str(spadekBMI)
```



## Zadanie 7 — listy

```python
lista = []
print lista

lista2 = [1, 2, 10000]
print lista2

lista3 = []
lista3.append(1)
lista3.append(2)
lista3.append(3)
print lista3

print "Drugi element listy trzeciej: " + str(lista3[1])
print "Trzeci element listy trzeciej: " + str(lista3[2])
```

```python
macierz = [
  [1, 2, 3],
  [0, 1, 0],
  [3, 3, 2]
]
print macierz

print "Srodkowy element macierzy: " + str(macierz[1][1])
```



## Zadanie 8 — pętle

```python
listA = [1, 2, 3, 100]

for value in listA:
  print 'Wartosc ' + str(value)

listA = [1, 2, 3, 100]

for index, value in enumerate(listA):
  print 'Wartosc w miejscu ' + str(index) + ' wynosi ' + str(value)

```



## Zadanie 9 — tworzenie pliku CSV w excelu

1. https://www.meteoblue.com/en/weather/archive/export/poland_united-states-of-america_4975603?daterange=2020-09-02%20to%202020-09-09&min=2020-09-02&max=2020-09-09&domain=NEMSGLOBAL&params=&params%5B%5D=temp2m&params%5B%5D=precip&params%5B%5D=wind%2Bdir10m&utc_offset=-4&timeResolution=hourly&temperatureunit=CELSIUS&velocityunit=KILOMETER_PER_HOUR&energyunit=watts&lengthunit=metric
2. Sanityzacja danych
3. Eksport do pliku CSV

## Zadanie 10 — otwieranie pliku CSV

```python
import csv
import sys

csvFile = open('temperature-data.csv', 'r')
dataIterator = csv.reader(csvFile, delimiter=';')
dataList = list(dataIterator)

print dataList
print 'Pierwszy wpis czas: ' + str(dataList[0][0])
print 'Pierwszy wpis temperatura: ' + str(dataList[0][1])
```



## Zadanie 12 — instalowanie biblioteki matplotlib

```
python -m pip install -U matplotlib
```

```
python3 -m pip install -U matplotlib
```



## Zadanie 12 — rysowanie wykresu z pliku

```python
import matplotlib.pyplot as plt
from dateutil.parser import parse
import csv
import sys

csvFile = open('temperature-data.csv', 'r')
dataIterator = csv.reader(csvFile, delimiter=';')
dataList = list(dataIterator)

plt.subplot(2, 1, 1)

x = []
y = []
for index, row in enumerate(dataList):
  x.append(index)
  y.append(float(row[1].replace(',','.')))

plt.plot(x,y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
```

