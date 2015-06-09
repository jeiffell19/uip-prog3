nombre = str (input ("¿Cual es el nombre del Vendedor?:\n"))

venta1 = float (input("¿Cuanto fue el monto del primer mes?\n"))

venta2 = float (input("¿Cuanto fue el monto del segundo mes?\n"))

venta3 = float (input("¿Cuanto fue el monto del tercer mes?\n"))


totalv=(venta1+venta2+venta3)

totalc=(totalv*.125)


print("Vendedor\tVentas\t\tComision\n-----\t\t-----\t\t-----\n" + nombre + "\t" + str(totalv) + "\t\t" + str(totalc))


JEIFFELL VASQUEZ
8-879-2483