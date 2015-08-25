import sqlite3 
import os.path


def DbTranslator_esp(translation): 
    contenido =[]
    con = None  
    try:
 
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "Translator")
        con = sqlite3.connect(db_path)    
        cur = con.cursor()    
        
        consulta= ("SELECT * FROM translation WHERE SPANISH LIKE '{}'".format(translation))
        cur.execute(consulta)
        datos = cur.fetchone()
        if datos == None:
            print("-No disponible-")
        else:           
            print("-Disponible-")
            for i  in range(len(datos)):
                if i==0:
                    # print("  SPANISH - ESPANOL: ",datos[i])
                    contenido.append(datos[i])
                if i==1:
                    # print("  ENGLISH - INGLES: ",datos[i])
                    contenido.append(datos[i])                
               
    except Exception as e: 
        print("Error %s : "%(e.args[0]) )
    finally:
        if con:
            con.close()
    return contenido


def DbTranslator_ing(translation): 
    contenido =[]
    con = None  
    try:

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "Translator")
        con = sqlite3.connect(db_path)    
        cur = con.cursor()    
        
  
        consulta= ("SELECT * FROM translation WHERE ENGLISH LIKE '{}'".format(translation))
        cur.execute(consulta)
        datos = cur.fetchone()
        if datos == None:
            print("-No disponible-")
        else:           
            print("-Disponible-")
            for i  in range(len(datos)):
                if i==0:
                    # print("  SPANISH - ESPANOL: ",datos[i])
                    contenido.append(datos[i])
                if i==1:
                    # print("  ENGLISH - INGLES: ",datos[i])
                    contenido.append(datos[i])
                    
               
    except Exception as e: 
        print("Error %s : "%(e.args[0]) )
    finally:
        if con:
            con.close()
    return contenido
