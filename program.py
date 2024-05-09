import pandas as pd
import sqlite3
import time

def cargar_csv(ruta_archivo, id_local):
    df = pd.read_csv(ruta_archivo)
    df['IdLocal'] = id_local
    df.drop(columns=['Producto'], inplace=True)
    return df

def crear_conexion(db_file):
    """Crea y devuelve una conexión a la base de datos SQLite especificada por db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Conexión exitosa a SQLite.")
    except sqlite3.Error as e:
        print(e)
    return conn

def exportar_a_excel(conn):
    """ Exporta los datos de la tabla 'ventas_consolidadas' a un archivo Excel. """
    df = pd.read_sql_query("SELECT * FROM ventas_consolidadas", conn)
    # Cambia la ruta completa a una carpeta donde tengas permisos de escritura
    with pd.ExcelWriter(r'C:\Users\fernando.lopez\OneDrive - PichinchaCorp\Documentos\Programas\Integración\Reporte_Ventas.xlsx', engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Ventas Consolidadas')
    print("Datos exportados a Excel")


def proceso_principal():
    archivos_locales = {
        1: 'DBLocales/Local1.csv',
        2: 'DBLocales/Local2.csv',
        3: 'DBLocales/Local3.csv',
        4: 'DBLocales/Local4.csv'
    }
    
    dataframes = []
    for id_local, nombre_archivo in archivos_locales.items():
        ruta_completa = nombre_archivo
        df = cargar_csv(ruta_completa, id_local)
        dataframes.append(df)
    
    df_consolidado = pd.concat(dataframes, ignore_index=True)
    
    # Conectar a SQLite
    conn = crear_conexion('ventas.db')
    
    # Si no hay una tabla, crea una o reemplaza
    df_consolidado.to_sql('ventas_consolidadas', conn, if_exists='append', index=False)
    
    # Exportar a Excel
    exportar_a_excel(conn)
    
    # Cerrar la conexión a la base de datos
    conn.close()

def main():
    while True:
        try:
            print("Iniciando el proceso de consolidación de datos...")
            proceso_principal()
            print("Proceso completado. Esperando hasta la próxima ejecución.")
        except Exception as e:
            print(f"Error durante la ejecución: {e}")
        
        # 3600 segundos (1 hora) antes de la próxima ejecución
        time.sleep(6300)

if __name__ == "__main__":
    main()
