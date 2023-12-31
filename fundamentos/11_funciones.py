"""
EN PYTHON, LAS FUNCIONES SON BLOQUES DE CÓDIGO REUTILIZABLES QUE RALIZAN TAREAS ESPECÍFICAS. PERMITEN ESTRUCTURAR Y ORGANIZAR EL CÓDIGO, 
EVITANDO LA REPETICIÓN Y MEJORANDO LA LEGIBILIDAD Y MANTENIBILIDAD. AL DEFINIR UNA FUNCIÓN, SE LE ASIGNA UN NOMBRE Y SE ESPECIFICA QUE ACCIONES
DEBE REALIZAR CUANDO SE LLAMA
LA SINTAXIS GENERAL PARA DECLARAR UNA FUNCIÓN EN PYTHON ES LA SIGUIENTE:
DEF NOMBRE_DE_LA_FUNCION(ARGUMENTO1, ARGUMENTO2, ...):
    #CODIGO EJECUTABLE
    RETURN RESULTADO

-DEF ES UNA PALABRA RESERVADA QUE INDICA EL COMIENZO DE UNA DECLARACIÓN
-NOMBRE DE LA FUNCIÓN ES COMO NOSOTROS QUEREMOS QUE SE LLAME
-ARGUMENTOS1 Y 2 SON PARÁMETROS QUE LE PASAMOS PARA REALIZAR UNA DETERMINADA ACCIÓN
- : INDICAN QUE EMPIEZA EL CÓDIGO EJECUTABLE
- RETURN DEVUELVE UN TIPO DE DATO(ESTO ES OPCIONAL) SI NO HAY RETURN DEVUELVE NONE DE FORMA IMPLICITA

EL NOMBRE DE LAS FUNCIONES DEBE SER REPRESENTATIVO, YA QUE NO TIENE SENTIDO Y PUEDE SER CONFUSO QUE SI UNA FUNCIÓN HACE LA OPERACIÓN DE CONTAR ELEMENTOS DE UN DICCIONARIO
LE PONGAMOS DE NOMBRE my_funcion_1 YA QUE ESTO ES MUY GENÉRICO, UN NOMBRE CORRECTO SERÍA POR EJEMPLO: tam_dicc, tamanyo_diccionario... ALGO QUE NOS DIGA QUE HACE ESA FUNCIÓN
"""
#DEFINIMOS UNA FUNCIÓN SUMAR, QUE DEVUELVE EL RESULTADO DE LA SUMA DE DOS NUMEROS NATURALES
def sumar(a,b):
    resultado = a + b
    return resultado

#LLAMAMOS A LA FUNCIÓN SUMAR, COMO LA FUNCIÓN SUMAR TIENE 2 PARÁMETROS SIEMPRE HABRÁ QUE LLAMARLA SUMAR(X,Y) SI NO DARÁ ERROR Y TE DIRÁ QUE NECESITA MÁS ARGUMENTOS
print(sumar(2,2))

#EN LAS FUNCIONES PODEMOS USAR TODOS LOS CONOCIMIENTOS APRENDIDOS ANTERIORMENTE, PUEDEN SER FUNCIONES MUY CORTAS COMO LA DE SUMAR O FUNCIONES MUY LARGAS Y COMPLEJAS
#CON EL FIN DE OPTIMIZAR CÓDIGO, DUPLICAR, LEGIBILIDAD...

#DEFINIMOS UNA FUNCIÓN FIBONACCI, QUE DEVUELVA UNA LISTA CON LA SERIE DE FIBONACCI HASTA CIERTO NÚMERO PASADO COMO PARÁMTRO.

def fibonacci(n):
    a, b = 0,1
    my_list = list()#DECLARACIÓN DE UNA LISTA SIN UN TAMAÑO FIJO, YA QUE EL PARÁMETRO N PUEDE VARIAR
    indice = 0
    while a < n:#USAMOS UN BUCLE PARA ITERAR UN CÓDIGO EJECUTABLE TANTAS VECES COMO QUERAMOS, ESTA VEZ DESDE 1 MIENTRAS QUE SEA MENOR QUE N
        my_list.insert(indice,a)#USAMOS PARA METER ELEMENTOS EN UNA LISTA LA FUNCION INSERT VISTA EN LA LECCIÓN 5, (INDICE, VALOR)
        indice += 1#ACTUALIZAMOS LA POSICIÓN DE NUESTRA LISTA, SI NO SIEMPRE METERÍA EN 1
        a, b = b, a+b#VAMOS ACTUALIZANDO NUESTROS VALORES DE FIBONACCI Y LA CONDICIÓN DE BUCLE SI NO, SERÍA BUCLE INFINITO YA QUE A NUNCA SERÁ >= N
    
    return my_list

print(fibonacci(10))

#PODRÍAMOS INVOCAR UNA FUNCIÓN DENTRO DE UNA FUNCIÓN? VAMOS A INTENTAR LLAMAR A UNA FUNCIÓN QUE INSERTE EN LA LISTA EN VEZ DE HACERLO AHÍ

def insertar(my_list, indice, valor):
    my_list.insert(indice,valor)
    return my_list

def fibonacci2(n):
    a, b = 0,1
    my_list = list()#DECLARACIÓN DE UNA LISTA SIN UN TAMAÑO FIJO, YA QUE EL PARÁMETRO N PUEDE VARIAR
    indice = 0
    while a < n:#USAMOS UN BUCLE PARA ITERAR UN CÓDIGO EJECUTABLE TANTAS VECES COMO QUERAMOS, ESTA VEZ DESDE 1 MIENTRAS QUE SEA MENOR QUE N
        insertar(my_list, indice, a)#USAMOS PARA METER ELEMENTOS EN UNA LISTA LA FUNCION INSERT VISTA EN LA LECCIÓN 5, (INDICE, VALOR)
        indice += 1#ACTUALIZAMOS LA POSICIÓN DE NUESTRA LISTA, SI NO SIEMPRE METERÍA EN 1
        a, b = b, a+b#VAMOS ACTUALIZANDO NUESTROS VALORES DE FIBONACCI Y LA CONDICIÓN DE BUCLE SI NO, SERÍA BUCLE INFINITO YA QUE A NUNCA SERÁ >= N
    
    return my_list

print(fibonacci2(10))#COMO VEMOS DEVUELVE EL MISMO RESULTADO, AHORA HACIENDO LA OPERACIÓN DE INSERCIÓN EN UNA FUNCIÓN AUXILIAR

#¿Y QUE PASA SI A UNA FUNCIÓN QUE SUMA DOS NUMEROS LE PASO DOS STRINGS, O DOS LISTAS, O DOS DICCIONARIOS?
#LA RESPUESTA ES QUE CON EL TIPADO DINAMICO DE PYTHON NO PODEMOS DECLARAR QUE SÓLO LE PASEMOS UN TIPO DE DATO
#POR LO QUE NO DARÁ ERROR HASTA EL MOMENTO DE LA OPERACIÓN EN CONCRETO
#EJEMPLO

def f_error(val1, val2):
    res = val1/val2
    return res

print(f_error(8,2))#LLAMAMOS A LA FUNCION F_ERROR QUE HACE LA DIVISIÓN DE DOS NUMEROS Y ES CORRECTA
#PERO Y SI YO LE PASO DOS STRINGS?
#print(f_error("hola", "adios"))#EVIDENTEMENTE DA ERROR, PERO EL ERROR OCURRE CUANDO INTENTA HACER / YA QUE NO SE PUEDEN DIVIDIR CADENAS DE TEXTO, PERO LOS ARGUMENTOS NO SE QUEJAN
#POR LO QUE HAY QUE LLEVAR CUIDADO CON EL PASO DE PARÁMETROS

#PODEMOS USAR ANOTACIONES PARA INDICAR AL USUARIO QUE LEA LA FUNCIÓN EL TIPO ESPERADO Y EL TIPO DEVUELTO, PERO ESTO NO ES UNA OBLIGACIÓN 
#TAN SOLO PROPORCIONA INFORMACIÓN REFERENTE AL COMPORTAMIENTO DE LA MISMA, PERO NUNCA SERÁ UNA OBLIGACIÓN

def f_error2(val1: int, val2: int)-> int:
    res = val1/val2
    return res

#ESTO INDICA QUE QUEREMOS QUE NUESTROS PARAMETROS SEAN DE TIPO INT Y DEVUELVA UN INT, PERO VAMOS A INVOCARLA CON FLOATS

print(f_error2(8.5, 4.3)) #DEVUELVE COMO RESULTADO UN FLOAT, CUANDO NOSOTROS HEMOS ANOTADO INT, VEMOS QUE NO SIRVEN POR EL TIPADO DINAMICO Y QUE SÓLO APORTAN INFORMACIÓN

#¿PODEMOS TENER UNA FUNCIÓN CON PARÁTROS POR DEFECTO QUE SIEMPRE TENGA ALGO FIJO?
#EJEMPLO

def nombre_apellidos_edad (nombre, apellidos, edad = "Desconocida"):
    print("Mi nombre es: " + nombre + " y mi apellido es: " + apellidos + "y tengo " + edad + " anyos")

nombre_apellidos_edad("Alberto", "Canovas", "22")
#Y SI YO NO LE PONGO VALOR A EDAD¿?
nombre_apellidos_edad("Alberto", "Canovas")#VEMOS QUE COGE EL VALOR POR DEFECTO EN CASO DE QUE NO SE LE PASE NINGÚN PARÁMETRO INDICANDO LA EDAD
#MUESTRA DESCONCIDA QUE ES EL VALOR DEL ARGUMENTO POR DEFECTO EN CASO DE QUE NO TENGA VALOR EN LA LLAMADA DEL USUARIO
