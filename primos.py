def run() :
    numero = int(input("ingrese un numero: "))
    if esprimo(numero):
        print("el numero es primo")
    else :
        print("el numero no es primo")


def esprimo(numero) :
    if numero % 2 != 0 and numero % 3 != 0 and  numero % 5 != 0 and numero % 7 != 0 and numero % 11 != 0 :
        return True
    else :
        return False


if __name__ == "__main__" :
    run()