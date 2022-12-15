from io import open

def existe(fichero):
    try:
        f = open(fichero, 'r')
        f.close()
    except FileNotFoundError:
        return False

def contador(*arg):
    if existe('ejercicios/ejercicio2/contador.txt') == False:
        fichero = open('ejercicios/ejercicio2/contador.txt', 'a+')
        fichero.write('0')
        fichero.seek(0)
        contenido = fichero.read()
    else:
        fichero = open('ejercicios/ejercicio2/contador.txt', 'r')
        contenido = fichero.read()
        fichero.close()
        if len(arg) != 0:
            fichero = open('ejercicios/ejercicio2/contador.txt', 'w')
            if 'inc' in arg:
                contenido = int(contenido) + 1
            elif 'dec' in arg:
                contenido = int(contenido) - 1
            fichero.write(str(contenido))
    fichero.close()
    return contenido