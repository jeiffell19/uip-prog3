import os


opc = 0  #variable para escoger la opcion

while opc != 5:         #este while permite ejecutar el menu hasta que el usuario desee salir
    print("    ")
    print("\t\t°°°°°BIENVENIDO A CIPHER°°°°°")
    print("\tESTE PROGRAMA LE PERMITE REALIZAR LO SIGUIENTE")
    print("\n\t1.-- Introducir Texto")                          
    print("\n\t2.-- Cifrar Texto")                          #menu del programa en el cual se detalla las operaciones del mismo
    print("\n\t3.-- Descifrar Texto")
    print("\n\t4.-- Imprimir Texto")
    print("\n\t5.-- Salir del Programa")
    opc = input ("\n\tDigite el numero de la opcion que desee utilizar : ") #captura por teclado de la operacion a utilizar


    if opc == "1":                  #acceso a una de las opciones del menu en la cual se introducira el texto
        print("\n\tHa seleccionado Introducir Texto")
        texto = str(input("\n\tDigite Texto : "))   #captura valor de la variable por teclado

    elif opc == "2":    #segunda opcion del menu en la cual se cifrara el texto digitado
        print("\n\tHa seleccionado Cifrar Texto")
        print(str(ord(texto)+1)) #esta funcion ord permite retornar el valor entero del caracter introducido en la opcion 1
        
                  
    elif opc == "3":        #proceso de desifrado del texto
        print("\n\tHa seleccionado Descifrar Texto")
        print(str(chr((texto)-1)))  #esta opcion chr permite retorna el valor cadena de un caracter entero introducido, en este caso el cifrado en opcion 2
        
      
    elif opc == "4":        #impresion por pantalla del texto
        print("\n\tHa seleccionado Imprimir Texto")
        print(texto)    #visualisaremos el texto introducido

    elif opc == "5":    #ultima opcion para salir del programa
        print("\n\tSALIENDO....")

        break

os.system("cls")

        
    


