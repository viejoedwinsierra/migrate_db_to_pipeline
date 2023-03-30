import psycopg2;
import xml.etree.ElementTree as ET
import os;
print("hello roma")
conexion = psycopg2.connect(host="adesahurtoterminalesdb.postgres.database.azure.com", database="hurtoterminales", user="hurto_usr@adesahurtoterminalesdb", password="Temporal01*1")
# Creamos el cursor con el objeto conexion
cur = conexion.cursor()
esquema = 'hurto'
# Ejecutamos una consulta
#cur.execute( "SELECT proname, pg_get_functiondef(f.oid) definicion FROM pg_catalog.pg_proc f INNER JOIN pg_catalog.pg_namespace n ON (f.pronamespace = n.oid) WHERE n.nspname = '" + esquema + "' " )

cur.execute( "SELECT n.nspname, proname, pg_get_functiondef(f.oid) definicion FROM pg_catalog.pg_proc f INNER JOIN pg_catalog.pg_namespace n ON (f.pronamespace = n.oid) WHERE n.nspname not in ('pg_catalog','information_schema','public')" )

# Recorremos los resultados y los mostramos
for nspname, proname, definicion in cur.fetchall():
	#print(proname)
    file = open("C:/Users/EGSIERRAPO/Documents/GitHub/HurtoTerminalesBD/deploy/Struct/procedures/" + nspname + "_" + proname + ".sql","w")
    file.write(definicion)
    file.close()
    file = open("C:/Users/EGSIERRAPO/Documents/GitHub/HurtoTerminalesBD/deploy/Struct/procedures/rollback_" + nspname + "_" + proname + ".sql","w")
    file.write("select * process.borrar_funcion('" + nspname + "','" + proname + "');")
    file.close()

# Cerramos la conexión
conexion.close()
tree = ET.parse("C:/Users/EGSIERRAPO/Documents/GitHub/HurtoTerminalesBD/deploy/Struct/tables/001_hurto_create_table.xml")




