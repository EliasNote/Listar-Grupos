import random
groups = []
list = []

def printOut(groups):
  for x in range(len(groups)):
    print("Grupo",x+1)
    for y in range(len(groups[x])):
      print(groups[x][y])

def adicionar():
  option = 1
  while option == 1:
    list.append(input("Digite o nome: "))
    option = int(input("Digite 1 para continuar a adicionar, qualquer outra tecla para parar: "))
  random.shuffle(list)
  organize(list)

def organize(list):
  personAmount = int(input("Digite a quantidade desejada de integrantes em cada grupo: "))

  if len(list) % personAmount == 0:
    groupSize = int(len(list)/personAmount)
  else:
    groupSize = int(len(list)/personAmount)+1

  for x in range(groupSize):
    groups.append([])


  counter = 0
  while counter < len(list):
    for x in range(groupSize):
      if counter == len(list):
          break
      groups[x].append(list[counter])
      counter += 1


adicionar()
printOut(groups)