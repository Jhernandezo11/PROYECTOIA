import pandas as pd
import mysql.connector

# Conectarse a la base de datos MySQL
conexion = mysql.connector.connect(
    host='20.121.53.224',
    user='ia',
    password='proyectoia.23',
    database='ASISTENCIAUNIVERSIDAD'
)

cursor = conexion.cursor()
# Llamada al procedimiento almacenado
fecha_inicio = '2023-05-27'
fecha_fin = '2023-05-30'

# Consulta SQL para obtener los datos
query = "CALL sp_asistencias(%s, %s)"
parametros = (fecha_inicio, fecha_fin)

# Ejecutar el procedimiento almacenado
cursor.execute(query, parametros)

# Obtener los resultados
resultados = cursor.fetchall()

# Crear un DataFrame de pandas con los resultados
#df = pd.DataFrame(resultados, columns=['CLASE', 'Estudiante','CARNET','FECHA','ATENCION'])

# Guardar el DataFrame en un archivo Excel
#ruta_archivo = './tests/dataset/asistencia.xlsx'
#df.to_excel(ruta_archivo, index=False)

for fila in resultados:
    print(fila) 

# Cerrar cursor y conexión
cursor.close()
conexion.close()