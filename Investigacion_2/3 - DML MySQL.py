USE base_datos;
CREATE TABLE persona (
    dni VARCHAR(9) PRIMARY KEY NOT NULL,
    nombre VARCHAR(15) NOT NULL,
    apellido1 VARCHAR(15) NOT NULL,
    apellido2 VARCHAR(15) NOT NULL
);
 
CREATE TABLE coche (
    matricula VARCHAR(8) PRIMARY KEY NOT NULL,
    marca VARCHAR(15) NOT NULL,
    modelo VARCHAR(15) NOT NULL,
    persona_dni VARCHAR(9) NOT NULL,
    FOREIGN KEY (persona_dni) REFERENCES persona(dni)
);
