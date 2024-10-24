

def validar_ean(codigo):
    
    comp=False
    
    #var para el calculo de la suma
    suma = 0
    
    
    
    #debemos comprobar si el numero tiene menos de 13 cifras, y si esta fuera de
    if len(codigo) <= 8:
        codigo = codigo.zfill(8)
        
        comp=True
        
    elif len(codigo) > 8 and len(codigo) <= 13:
        codigo = codigo.zfill(13)
        
        
        comp=True
        
    elif len(codigo) > 13:
        return False
    
    
    
    # Separar el código en los dígitos principales y el dígito de control
    digitos = [int(d) for d in codigo]
    codigo_sin_control = digitos[:-1]
    digito_control = digitos[-1]

    # Determinar si es EAN-8 o EAN-13
    longitud = len(codigo)

    
    
    # Realizar la suma ponderada
    for i in range(longitud - 1):
        # Si la posición es impar desde la derecha, multiplicamos por 3
        if (longitud - 2 - i) % 2 == 0:
            suma += codigo_sin_control[i] * 3
        else:
            suma += codigo_sin_control[i] * 1
    
    
    
    
    
    
    
    
    return comp