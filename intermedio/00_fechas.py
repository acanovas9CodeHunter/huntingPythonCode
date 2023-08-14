"""
EN PYTHON, EL MANEJO DE FECHAS Y HORAS SE REALIZA PRINCIPALMENTE UTILIZANDO EL MÓDULO ESTÁNDAR LLAMADO 'DATETIME'. ESTE MÓDULO 
PROPORCIONA CLASES Y FUNCIONES PARA TRABAJAR CON FECHAS, HORAS, INTERVALOS DE TIEMPO Y REALIZAR OPERACIONES RELACIONADASA CON ELLAS. 
EN PYTHON PODEMOS DIFERENCIAR ENTRE EL TIPO DATE QUE MUESTRA UNA FECHA ESPECIFICA SIN INCLUIR INFORMACIÓN DE LA HORA Y EL TIPO TIME
QUE HACE REFERENCIA A UN MOMENTO ESPECIFICO DEL DÍA, REPRESENTADO EN HORAS, MINUTOS Y SEGUNDOS

POR LO QUE SEGÚN EL USO Y EL CASO PODRÍAMOS ELEGIR ENTRE EL TIPO DE DATO DATE, TIME O EL DATETIME QUE INCLUYE LOS DOS.

"""
from datetime import datetime, timedelta

hora_actual = datetime.now()
#CON TODOS ESTOS CAMPOS PODEMOS ACCEDER A LA FECHA ACTUAL DEL SISTEMA
print(hora_actual)
print(hora_actual.year)
print(hora_actual.month)
print(hora_actual.day)
print(hora_actual.hour)
print(hora_actual.minute)
print(hora_actual.second)

#CONVERSIÓN DE FECHAS EN FORMATOS
"""
PARÁMETROS DE LA FUNCIÓN d.strftime
%Y año completo 2023
%y últimos 2 dígitos 23
%m mes en número 07
%B mes en palabra Julio
%A día de la semana Viernes
%a día de la semena abreviado Vier
"""

fecha = datetime.now()
print(fecha.strftime('%A-%m-%Y'))
print(fecha.strftime('%a-%m-%Y'))
print(fecha.strftime('%A-%B-%Y'))
print(fecha.strftime('%A-%m-%y'))

#strptime DEVUELVE EL OBJETIO DE TIPO DATE, TIME O DATETIME QUE RESULTA DE CONVERTIR LA CADENA S DE ACUERDO AL FORMATO INDICADO 
#LOS PARÁMETROS SON IGUALES QUE EN CONVERSIÓN DE FECHAS

f_string = '21/07/2023'
print(fecha.strptime(f_string,'%d/%m/%Y'))

#ARITMÉTICA DE FECHAS
fecha1 = fecha.strptime(f_string,'%d/%m/%Y')
fecha2 = fecha.strptime('22/07/2023','%d/%m/%Y')

print(fecha2-fecha1)#CON EL OPERADOR - RESTA PODEMOS VER LA DIFERENCIA ENTRE DOS FECHAS

#CON LA FUNCIÓN timedelta PODEMOS REALIZAR OPERACIONES CON LAS FECHAS, SUMAR DÍAS A UNA FECHA CONCRETA, SUMAR MESES...

dias_sumar = 5 #LA FUNCION TIMEDELTA NOS PERMITE SUMAR DÍAS, HORAS, MINUTOS, SEGUNDOS ETC
print(fecha1 + timedelta(days=dias_sumar))#NUESTRA FECHA1 ES 21/07/2023 Y ESTAMOS SUMANDO 5 DÍAS, RESULTADO 26/07/2023


#revisar

