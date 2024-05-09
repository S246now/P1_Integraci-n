import sqlite3

def crear_conexion(db_file):
    """ Crea una conexión a la base de datos SQLite especificada por db_file """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexión exitosa. SQLite DB version:", sqlite3.version)
    except sqlite3.Error as e:
        print(e)
    return conn

def crear_tabla(conn):
    """ Crea una tabla en la base de datos SQLite conectada por 'conn' """
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ventas_consolidadas (
                IdTransaccion INTEGER PRIMARY KEY,
                IdLocal INTEGER NOT NULL,
                Fecha TEXT NOT NULL,
                IdCategoria INTEGER NOT NULL,
                IdProducto INTEGER NOT NULL,
                Cantidad INTEGER NOT NULL,
                PrecioUnitario REAL NOT NULL,
                TotalVenta REAL NOT NULL
            );
        """)
        print("Tabla creada exitosamente.")
    except sqlite3.Error as e:
        print(e)

def main():
    database = "ventas.db"

    # Crear una conexión a la base de datos
    conn = crear_conexion(database)

    # Crear tabla
    if conn is not None:
        crear_tabla(conn)
        # Cerrar conexión a la base de datos
        conn.close()
    else:
        print("No se pudo establecer conexión con la base de datos.")

if __name__ == '__main__':
    main()
