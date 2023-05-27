import mysql.connector
# Establecer los parámetros de conexión
config = {
  'user': 'ia',
  'password': 'proyectoia.23',
  'host': '20.121.53.224',
  'database': 'ASISTENCIAUNIVERSIDAD',
  'raise_on_warnings': True
}

# Crear una conexión
try:
    conn = mysql.connector.connect(**config)
    print("Conexión exitosa a la base de datos")
    
    # Realizar operaciones en la base de datos

    cursor = conn.cursor()

    # Ejecutar una consulta SQL
    query = "SELECT * FROM IMAGENES"
    cursor.execute(query)

    resultados = cursor.fetchall()

    # Mostrar los datos de la tabla
    for row in resultados:
        print(row)
    
    # Cerrar el cursor
    cursor.close()

    # Cerrar la conexión
    conn.close()
    print("Conexión cerrada")

    # Cerrar la conexión
    conn.close()
    print("Conexión cerrada")
    
except mysql.connector.Error as err:
    print("Error de conexión a la base de datos: {}".format(err))

