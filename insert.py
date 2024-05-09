def insertar_venta(conn, venta):
    """
    Inserta una nueva fila en la tabla ventas_consolidadas.
    venta debe ser una tupla que contenga (IdTransaccion, IdLocal, Fecha, IdCategoria, IdProducto, Cantidad, PrecioUnitario, TotalVenta).
    """
    sql = ''' INSERT INTO ventas_consolidadas(IdTransaccion, IdLocal, Fecha, IdCategoria, IdProducto, Cantidad, PrecioUnitario, TotalVenta)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, venta)
    conn.commit()
    return cur.lastrowid

# Ejemplo de uso
conn = crear_conexion('ventas.db')
nueva_venta = (1, 1, '2024-05-08', 101, 001, 5, 10.0, 50.0)
venta_id = insertar_venta(conn, nueva_venta)
print("Se ha insertado una nueva venta con id:", venta_id)
conn.close()
