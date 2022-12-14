def error_num(a, b):
    '''
    Esta función nos ayuda a determinar si los datos introducidos son números o no.
    '''
    try:
        a, b = int(a), int(b)
        return True
    except ValueError:
        return 'Error: Tipo de dato no válido.'

def error_div(a, b):
    '''
    Esta función nos ayuda a determinar si la división introducida es entre 0.
    '''
    try:
       return int(a)/int(b)
    except ZeroDivisionError:
        return 'Error: No es posible dividir entre cero.'

def suma(a, b):
    '''
    Esta función realiza la suma de dos números.
    '''
    if error_num(a, b) == True:
        return int(a)+int(b)
    else:
        return error_num(a, b)

def resta(a, b):
    '''
    Esta función realiza la resta de dos números.
    '''
    if error_num(a, b) == True:
        return int(a)-int(b)
    else:
        return error_num(a, b)

def producto(a, b):
    '''
    Esta función realiza el producto de dos números. 
    '''
    if error_num(a, b) == True:
        return int(a)*int(b)
    else:
        return error_num(a, b)

def division(a, b):
    '''
    Esta función realiza la división de dos números.
    '''
    if error_num(a, b) == True:
        return error_div(a, b)
    else:
        return error_num(a, b)