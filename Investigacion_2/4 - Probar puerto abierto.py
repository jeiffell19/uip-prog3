import socket

host = input("Indica el host : ")

uno = input("Primer numero del rango : ")

dos = input("Segundo numero del rango : ")

socket = socket.socket()

for puerto in range(int(uno),int(dos)):
    try:
        socket.connect((host,puerto))
        print ("Puerto "+str(puerto)+" abierto")
        socket.close()
 
    except :
        print ("Puerto "+str(puerto)+" cerrado.")

