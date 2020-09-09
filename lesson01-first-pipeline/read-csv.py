import csv
import sys

csvFile = open('temperature-data.csv', 'r')
dataIterator = csv.reader(csvFile, delimiter=';')
dataList = list(dataIterator)

print dataList
print 'Pierwszy wpis czas: ' + str(dataList[0][0])
print 'Pierwszy wpis temperatura: ' + str(dataList[0][1])
