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
