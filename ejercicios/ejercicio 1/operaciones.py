def error_num(a, b):
    '''
    Esta función nos ayuda a determinar si los datos introducidos son números o no.
    '''
    try:
        a, b = int(a), int(b)
        return True
    except ValueError:
        return 'Error: Tipo de dato no válido.'

def sumar(a, b):
    '''
    Esta función realiza la suma de dos números.
    '''
    if error_num(a, b) == True:
        return int(a)+int(b)
    else:
        return error_num(a, b)