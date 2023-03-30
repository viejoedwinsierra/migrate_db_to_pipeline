# importando el modulo de regex de python
from ast import Not, NotIn
import re  
import os


def run() :
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("**Analisis contenidos directorios Proyectyo migracion Hurto fecha: 2022-04-20**")
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("*******************************************************************************")
    print("\n\n")
    print("Ingresando directorios para analizar es una lista")
    #reed_plano(["C:\\xpbatch\\out_busqueda.txt";"C:\\xpserneg\\out_busqueda.txt"])
    #print(red_plano("C:\\xpbatch\\out_busqueda.txt"))
    list_plano = reed_plano("C:\\xpbatch\\out_busqueda.txt")
    print(substr_plano())


def reed_plano(local_url):
    print ("Inicia funcion de leer archivo plano")
    f = open(local_url, "r")
    arc_plano = f.read()
    #print(f.read())
    print("Convertimos el txt en una lista por lineas")
    plano_list = arc_plano.split("\n")
    #print(plano_list)
    print("devolvemos la lista del archivo plano")
    return plano_list


def substr_plano():
    string = 'abc 12\de 23 \n f45 6'
    pattern = '\s+'
    replace = ''
    new_string = re.sub(pattern, replace, string)
    return new_string


if __name__ == "__main__" :
    run()
    
    