"""
EN ESTA SECCION SE TRATARA EL USO DE VARIABLES
UNA VARIABLE ES UN NOMBRE MUTABLE QUE USAMOS PARA HACER REFERENCIA A UN VALOR O DATO ALMACENADO EN MEMORIA
COMO SE COMENTO EN LA SECCION INTRODUCCION00.PY PYTHON TIENE TIPADO DINAMICO, ESTO PRODUCE QUE NO SEA NECESARIO DECLARAR EL TIPO DE VARIABLE ANTES
    EJEMPLOS C++/JAVA
        String cadena  = "cadena"
        integer num = 20;
    EJEMPLOS PYTHON
        cadena = "cadena"
        num = 20;
*APENDICE CONSTANTES ABAJO
"""
#LO MAS CORRECTO ES TODO EN MINUSCULAS Y CON _ SEPARANDO (NOMENCLATURA,CONVENCION Y BUENAS PRACTICAS DE PYTHON)
my_first_variable = "esta varaible almacena un string"
myfirstvariable2 = 5

#EJEMPLO DE TIPADO DINAMICO(PODEMOS PARA UNA MISMA VARIABLE CAMBIAR TANTAS VECES QUERAMOS SU TIPO DE DATO)
var_aux = 10
print(type(var_aux)) #ESTO VA A MOSTRAR TIPO INT
var_aux = "ahora soy una cadena"
print(type(var_aux)) #ESTO VA A MOSTRAR TIPO STRING
var_aux = True
print(type(var_aux)) #ESTO VA A MOSTAR UN BOOL



#PODEMOS DECLARAR VARIAS VARIABLES EN LA MISMA LINEA (NO ES LO MEJOR DESDE LAS BUENAS PRACTICAS)
name, surname, age = "ALBERTO", "CANOVAS", 22  

#ESTO ES CORRECTO Y FUNCIONA, PERO ESTE ESTILO DE DECLARACION SE UTILIZA EN JAVA Y C/C++
myFirstVariable3 = 5

#ERRORES A LA HORA DE DECLARAR, AÑADIR CARACTERES ESPECIALES, NUMEROS AL INICIO...
"""
    first-name
    first@name
    first%name
    name-1
    1name
"""


"""
APENDICE CONSTANTES
UNA CONSTANTE ES UNA VARIABLE INMUTABLE CUYO VALOR NO PUEDE CAMBIAR A LO LARGO DE LA EJECUCION DE NUESTRO PROGRAMA
EN JAVA SE CONOCEN Y DECLARAN TAL QUE ASI:
    public static final int MY_CONSTANT = 10;
ESTO INDICA QUE MY_CONSTANT TIENE EL VALOR DE 10, SI LINEAS DESPUES INTENTAS HACER MY_CONSTANT = 11 DARA ERROR 
YA QUE AL USAR LA PALABRA RESERVA 'FINAL' NO ES POSIBLE DE MODIFICAR SU VALOR

EN PYTHON COMO TAL NO EXISTEN LAS CONSTANTE, NO TIENE TERMINOS DEFINIDOS CON ESE FIN, PERO POR CONVENCION Y NOMENCLATURA "TECNICAMENTE PODRIAMOS DECLARARLA ASI"
    MY_CONSTANT = 10
LOS PROGRAMADORES DE PYTHON SABEN QUE UNA VARIABLE ESCRITA EN MAYUSCULAS TIENE EL FIN DE QUE SU VALOR NO SE MODIFIQUE
SIN EMBARGO, COMO HEMOS DICHO NO EXISTEN LAS CONSTANTES COMO TAL POR LO QUE PODRIAMOS HACER:
    MY_CONSTANT = 11

"""






