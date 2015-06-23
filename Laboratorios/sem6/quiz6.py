import os

directorio = {}


opc = 0

while opc != 5 :
    
    print("   ")
    print("DIRECTORIO TELEFONICO")
    print("   ")
    print("-1: Imprimir numeros de telefono")
    print("-2: Agregar numeros de telefono")
    print("-3: Quitar numeros de telefono")
    print("-4: Buscar numeros de telefono")
    print("-5: SALIR")
    print("   ")
    opc = input("Digite la opcion deseada: ")

    if opc == "1" :
        print("   ")
            
        print("Numero\t\tNombre\n\t\t\t\n" + str(directorio)+"\t\t"+nombre)
        
    elif opc == "2" :
        print("   ")
        nombre = input("Introduzca nombre que desea agregar: ")
        tel = (input("Introduzca numero que desea agregar: "))
        directorio [nombre]=tel

    elif opc == "3" :
        print("   ")
        nombre = input ("Introduzca nombre que desea eliminar: ")
        del directorio [nombre] 

    elif opc == "4" :
        print("   ")
        nombre = input("Introduzca el nombre que desea buscar: ")
        print("Numero\t\tNombre\n\t\t\t\n" + str(directorio [nombre])+"\t\t"+nombre)

    elif opc == "5" :
        
        break   

os.system("cls")
