
myFruitList = ["apple", "banana", "cherry"]



"""
print(myFruitList)
print(type(myFruitList))


print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)


myFinalAnswerTuple = ("apple", "banana", "pineapple", "sandia")

LargoLista = len(myFruitList)
LargoTupla = len(myFinalAnswerTuple)

print("Largo Lista: " + str(LargoLista))
print("Largo Tupla: " + str(LargoTupla))
 
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[1])
"""
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple",
  "Daniel" : myFruitList
}

value = myFavoriteFruitDictionary.get('Daniel', "no existe")
print(value)
print(type(value))

"""
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

print(myFavoriteFruitDictionary["Daniel"])
"""
