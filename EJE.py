import random
import matplotlib.pyplot as plt
import numpy as np

#Funcion que simula el lanzamiento del dado 
def dado():
    r = random.random()
    if r < 1/6:
      resu=1
    elif r< 2/6:
      resu=2
    elif r<3/6:
      resu=3
    elif r<4/6:
      resu=4
    elif r<5/6:
      resu=5
    else:
      resu=6
    return resu

#Acumulador de victorias
acumulador=0

#Ingreso de las iteracciones N 
N=int(input("Ingrese numero de repeticiones: "))

for i in range(N):

  #ATACANTE
  patacante=[]  #Lista de atacante
  for i in range(3):
    numero=dado()
    patacante.append(numero)

  #DEFENSOR
  pdefensor=[]  #Lista de defensor
  for i in range(2):
    numero=dado()
    pdefensor.append(numero)

  patacante.sort(reverse=True)  #Ordenamiento de mayor a menor de las listas
  pdefensor.sort(reverse=True)

  aatacante=0  #Acumuladores de victorias de atacante y defensor
  adefensor=0
  
  for i in range(2):
    if patacante[i]>pdefensor[i]:
      aatacante+=1

    elif patacante[i]<pdefensor[i]:
      adefensor+=1

    elif patacante[i]==pdefensor[i]:
      adefensor+=1

  if  aatacante>adefensor:   #Condificional para conocer el ganador
    acumulador+=1
  else:
    continue

print("PROBABILIDAD QUE GANE EL ATACANTE", acumulador/N)



