#! /usr/bin/env python
 
# Importamos el conector de MySQL
import mysql.connector
 
# Variable con la configuracion de la conexion
config_mysql = {
    'user': 'usuario',
    'password': 'pass',
    'host': 'localhost',
    'database': 'prueba',
}
 
# conectamos al servidor MySql
conector = mysql.connector.connect(**config_mysql)
 
# cursor, clase para el manejo del SQL ???
cursor = conector.cursor()
 
# Creamos la consulta SQL
query = ("SELECT Nombre, Telefono FROM prueba")
 
# Ejecutamos la consula SQL
cursor.execute(query)
 
# Mostramos todos los datos de la consulta
for (Nombre, Telefono) in cursor:
    print("Nombre: " + Nombre + ", Telefono: " + Telefono)
 
# Cerramos cursor
cursor.close()
 
# Cerramos la conexion
conector.close()
