def printHelloWorld():
  print "Hello world"

printHelloWorld()
printHelloWorld()
printHelloWorld()


#########
def printValue(name, value):
  print "Wartosc " + name + " wynosi: " + str(value)


pressure = 5
printValue("cisnienia", pressure)

printValue("temperatury", 36.6)

printValue("2 do potegi 3", 2 ** 3)

#########
def printBMI(weight, height):
  bmi = weight / (height ** 2)
  print "BMI wynosi " + str(bmi)

printBMI(75, 1.75)


#########
def calculateBMI(weight, height):
  return weight / (height ** 2)

bmi1 = calculateBMI(75, 1.75)
bmi2 = calculateBMI(70, 1.75)
spadekBMI = bmi1 - bmi2
print "BMI spadlo o " + str(spadekBMI)
