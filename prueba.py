import psycopg2;
import os;
print("hello roma")
conexion = psycopg2.connect(host="adesahurtoterminalesdb.postgres.database.azure.com", database="hurtoterminales", user="hurto_usr@adesahurtoterminalesdb", password="Temporal01*1")
# Creamos el cursor con el objeto conexion
cur = conexion.cursor()
esquema = 'hurto'
# Ejecutamos una consulta
cur.execute( "SELECT proname, pg_get_functiondef(f.oid) definicion FROM pg_catalog.pg_proc f INNER JOIN pg_catalog.pg_namespace n ON (f.pronamespace = n.oid) WHERE n.nspname = '" + esquema + "' " )

# Recorremos los resultados y los mostramos
for proname, definicion in cur.fetchall():
	#print(proname)
    file = open("C:/Users/EGSIERRAPO/Documents/GitHub/HurtoTerminalesBD/deploy/Struct/procedures/" + esquema + "_" + proname + ".sql","w")
    file.write(definicion)
    file.close()
    file = open("C:/Users/EGSIERRAPO/Documents/GitHub/HurtoTerminalesBD/deploy/Struct/procedures/rollback_" + esquema + "_" + proname + ".sql","w")
    file.write("process.borrar_funcion('" + esquema + "','" + proname + "');")
    file.close()

# Cerramos la conexión
conexion.close()




