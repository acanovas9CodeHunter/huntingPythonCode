"""
SECCION DEDICADA A LA ESTRUCTURA DE DATOS LISTS
UNA LISTA ES UNA ESTRUCTURA DE DATOS QUE PUEDE CONTENER VARIOS ELEMENTOS, COMO NÚMROS, CADENAS DE TEXTO, OBJETOS U OTRAS LISTAS. PUEDES PENSAR
EN UNA LISTA COMO UNA SECUENCIA ORDENADA DE ELEMENTOS, DONDE CADA ELEMENTO TIENE UN INDICE ASOCIADO QUE INDICA SU POSICION EN LA LISTA
"""

#PARA CREAR UNA LISTA
my_list = [1,2,3,4]
my_list2 = ["h","o","l","a"]
my_list3 = list()

#PARA ACCEDER A CADA POSICION DE UNA LISTA USAMOS EL OPERADOR [POS] QUE EMPIEZA EN 0 Y ACABA EN LEN -1
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
#SI INTENTAMOS ACCEDER A UNA POSICION DE LA LISTA QUE NO CONTIENE ELEMENTOS POR EJEMPLO LA 12 PROVOCAREMOS UN ERROR INDEXERROR
#print(my_list[12])

#PODEMOS MODIFICAR EL VALOR DE UN ELEMENTO DE LA LISTA ACCEDIENDO A SU VALOR POR POSICION

print(my_list[3])
my_list[3] = 7
print(my_list[3])

#FUNCIONES MÁS IMPORTANTES EN LISTAS
print(len(my_list)) #LA FUNCION LEN DEVUELVE EL TAMAÑO DE LA LISTA
my_list.append(9)#FUNCION QUE AÑADE UN ELEMENTO MÁS EN LA LISTA, EN LA SIGUIENTE POSICION
print(my_list)

my_list.insert(2, 33)#FUNCION INSERT QUE RECIBE UN INDICE Y UN VALOR Y LO INSERTA EN LA LISTA, DESPLAZA LOS DEMÁS ELEMENTOS UNA POS A LA DERECHA
print(my_list)

my_list.remove(3)#FUNCION QUE ELIMINA TODOS LOS ELEMENTOS QUE SEAN 3 DE LA LISTA
print(my_list)
my_list.pop(3)#FUNCION QUE ELIMINA UNA POSICION CONCRETA Y ADEMÁS DEVUELVE ESE VALOR
print(my_list)

del my_list[0]#FUNCION QUE ELIMINA EL PRIMER ELEMENTO SITUADO EN LA POSICION 0 DE LA LISTA
print(my_list)

print(my_list.count(2))#FUNCION COUNT QUE DEVUELVE EL NUMERO DE OCURRENCIAS DE ESE ELEMENTO EN LA LISTA, ¿CUANTOS 2 HAY EN MY_LIST?


#PODEMOS CONCATENAR LISTAS CON EL OPERADOR +
print(my_list + my_list2)

my_list.clear()#FUNCION QUE ELIMINA TODOS LOS ELEMENTOS DE UNA LISTA Y LA DEJA VACIA
print(my_list)