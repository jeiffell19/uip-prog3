import os, Lector, Autor, Copia, Libro

lista_lector=[]
lista_autor=[]
lista_libro=[]

contador=0

opc=0


while opc !=6:
    
    print("         ")
    print("\n\t\t°°°°°BIENVENIDO°°°°°")
    print("\n\t-1: Ingresar un lector")
    print("\n\t-2: Ingresar un autor")
    print("\n\t-3: Ingresar un libro")
    print("\n\t-4: Hacer peticion")
    print("\n\t-5: Hacer devolucion")
    print("\n\t-6: Salir")

    opc = input("\n\tIntroduzca la opcion que desea elegir:  \n")

    if opc == "1":
        print("\n\tHa seleccionado: Ingresar un lector")
        
        idn = input("\n\tIntroduzca el id del lector:  ")
        nom = input("\n\tIntroduzca nombre del lector:  ")
        l = Lector.Lector(idn, nom)
        lista_lector.append(l)

    elif opc == "2":
        print("\n\tHa seleccionado: Ingresar un autor")

        nom1 = input("\n\tIntroduzca nombre del autor:  ")
        nac = input("\n\tIntroduzca nacionalidad del autor:  ")
        a = Autor.Autor(nom1,nac)
        lista_autor.append(a)

    elif opc == "3":
        print("\n\tHa seleccionado: Ingresar un libro")

        tit = input("\n\tIntroduzca titulo del libro:  ")
        tip = input("\n\tIntroduzca tipo del libro:  ")
        edit = input("\n\tIntroduzca editorial del libro:  ")
        li = Libro.Libro(tit,tip,edit)
        lista_libro.append(li)
        contador=10
        
    elif opc == "4":        
        print("\n\tHa seleccionado: Hacer peticion")

        contador-=1
	
        if contador < 0 :
            print("\n\tNo quedan mas libros:  ")
                    
        else:
            print("\n\tSe ha entregado un libro:  ")
                    
    elif opc == "5":
        print("\n\tHa seleccionado: Hacer devolucion")
        
        contador+=1
        if contador > 10:
            print("\n\tNo hay libros por devolver:  ")
            contador -= 1
        else:
            print("\n\tSe ha regresado el libro:  ")

    elif opc == "6" :

        print("\n\tSALIENDO....")

        break

    
os.system("cls")

        
        
    
