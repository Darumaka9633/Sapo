import sqlite3

# Creamos una conexión con la base de datos SQLite
conn = sqlite3.connect('ejemplo.db')

# Creamos una tabla para almacenar los datos de la entidad "Clientes"
conn.execute('''CREATE TABLE Clientes
                (ID INTEGER PRIMARY KEY,
                Nombre TEXT NOT NULL,
                Direccion TEXT NOT NULL,
                Email TEXT);''')

# Creamos una tabla para almacenar los datos de la entidad "Pedidos"
conn.execute('''CREATE TABLE Pedidos
                (ID INTEGER PRIMARY KEY,
                Fecha TEXT NOT NULL,
                ClienteID INTEGER,
                FOREIGN KEY(ClienteID) REFERENCES Clientes(ID));''')

# Cerramos la conexión con la base de datos
conn.close()