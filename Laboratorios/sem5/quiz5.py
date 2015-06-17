import os
lista = []
opc = 0


do:

print("Este programa le permite elegir entre las siguientes opciones para su lista de supermercado")
print("   ")
print("-1: Agregar elemtos a la lista")
print("-2: Eliminar elemtos de la lista")
print("-3: Ver los elemtos que contiene la lista")
print("-4: Salir del programa")

opc = input("Introduzca la opcion que desea elegir")

if opc == "1": elemento = input("Digite lo que desea agregar a la lista")
lista.append(elemento)

if opc == "2": print("Estos son los elementos presentes en la lista")
print(lista)
eliminar = input ("Digite el elemento que desea eliminar de la lista")
del lista = [eliminar]

if opcion == "3": print(lista)

while opc !=4

os.system("cls")