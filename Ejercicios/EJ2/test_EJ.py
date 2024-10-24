from EJ import *


def codigo_barra_test():
    assert validar_ean("65839522")==True



def codigo_barra_test():
    assert validar_ean("65839521")==False



def codigo_ean13_test():
    assert validar_ean("8414533043847")==True 


#tests con menos de 8 cifras

#true. uno de los 
def completa_ceros_ean8_test():
    assert validar_ean("5839522")==True

#false. uno de los numeros esta mal
def completa_ceros_ean8_falso_test():
    assert validar_ean("5839521")==False




