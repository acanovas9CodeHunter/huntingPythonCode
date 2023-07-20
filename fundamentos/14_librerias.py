"""
EN PYTHON, UNA LIBRERÍA ES UN CONJUNTO DE MÓDULOS Y FUNCIONES PREDEFINIDAS QUE SE PUEDEN IMPORTAR Y UTILIZAR EN TUS PROGRAMAS PARA REALIZAR TAREAS ESPECIFICAS.
LAS LIBRERÍAS SON UNA PARTE ESENCIAL DEL ECOSISTEMA DE PYTHON, YA QUE PERMITEN A LOS DESARROLLADORES APROVECHAR FUNCIONALIDADES YA IMPLEMENTADAS EN LUGAR DE TENER
QUE ESCRIBIR TODO EL CÓDIGO DESDE CERO.
1. LIBRERÍAS ESTÁNDARD: PTHON VIENE CON UNA AMPLIA GAMA DE MÓDULOS Y LIBRERÍAS INTEGRADOS EN SU INSTALACIÓN ESTÁNDARD.
2. LIBRERÍAS DE TERCEROS. ESTAS LIBRERÍAS SE ENCUENTRAN EN EL PYTHON PACKAGE INDEX(PYPPI) Y SE PUEDEN INSTALAR FACILMENTE CON EL GESTOR DE PAQUETES PIP.
pip install nombre_libreria
DESPUÉS DE SU INSTALACIÓN DEBES HACER 
import nombre_libreria 
A PODER SER ARRIBA DE LA CLASE
"""

import my_libreria#IMPORTO UNA LIBRERÍA AUXILIAR QUE ME HE CREADO QUE TIENE UNA FUNCIÓN QUE DEVUELVE LA SUMA DE DOS NUMEROS ENTEROS

print(str(my_libreria.sumar(2,3)))#ACCEDO A LA LIBRERIA CON EL NOMBRE DE LA LIBRERÍA.METODO QUE QUEREMOS USAR, EN ESTE CASO EL SUMAR

#EN PYTHON HAY INFINIDAD DE LIBRERÍAS, UNA DE LAS MÁS TÍPICAS PARA CÁLCULOS MATEMÁTICOS ES

import math

print(math.inf)#MOSTRAMOS EL VALOR INFINITO QUE LA LIBRERÍA MATH