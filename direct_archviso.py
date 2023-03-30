import os
ejemplo_dir = 'C:\xpbatch'
for nombre_directorio, dirs, ficheros in os.walk(ejemplo_dir):
    print(nombre_directorio)
    for nombre_fichero in ficheros:
        print(nombre_fichero)