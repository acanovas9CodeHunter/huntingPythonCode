"""
SECCIÓN DEDICADA A LOS OPERADORES ARITMÉTICOS, ASIGNACIÓN, LÓGICOS...


OPERADOR               EJEMPLO             LO MISMO QUE
ARITMÉTICOS
+=                     x += 5              x = x + 5
-=                     x -= 5              x = x - 5
*=                     x *= 5              x = x * 5
/=                     x /= 5              x = x / 5
%=                     x %= 5              x = x % 5 -> DEVUELVE EL RESTO DE UNA DIVISIÓN DE X / 5
//=                    x //= 5             x = x // 5 -> ES UNA DIVISIÓN QUE SIEMPRE VA A REDONDEAR A UN NUMERO ENTERO
**=                    x ** 5              x = x ** 5 -> DEVUELVE EL RESULTADO DE UN EXPONENTE, ES DECIR 2^5 

LÓGICOS
==                     x == 5              x == 5
!=                     x != 5              x != 5
>                      ¿x > 5?             ¿x > 5?            
<                      ¿x < 5?             ¿x < 5?
>=                     ¿x >= 5?            ¿x >= 5?
<=                     ¿x <= 5?            ¿x <= 5?
ESTOS MAYORMENTE SE UTILIZAN EN SENTENCIAS CONDICIONES QUE SE VERÁN EN CAPÍTULOS POSTERIORES
UN EJEMPLO SERÍA:
    if(x >= 5)//SI X ES MAYOR O IGUAL A 5 HARÁ EL CÓDIGO DE ABAJO
        ....
    else//SI ES CUALQUIER VALOR DESDE 4 PARA ABAJO HARÁ ESTE CÓDIGO DE ABAJO
        ....

AND Y OR ESTOS SE UTILIZAN PARA CONCATENAR SENTENCIAS CONDICIONALES, POR EJEMPLO:
    SI(X > 5 AND X < 10) SE TIENEN QUE CUMPLIR LAS DOS CONDICIONES, ES DECIR QUE X SEA 6,7,8,9
        ....
    
    SI(X > 5 OR Y > 5) SÓLO TIENE QUE CUMPLIRSE UNA CONDICIÓN DE LAS DOS, TAMBIÉN VALEN LAS DOS
        ES DECIR SI X ES 6,7,8,9... O SI Y ES 6,7,8,9...
"""

# EJEMPLOS ARITMÉTICOS

x = 5
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)
print("------------------------------")
#EJEMPLO LÓGICOS ESTOS DEVUELVE TRUE O FALSE, SI SE CUMPLE LA CONDICIÓN
print(x > y)
print(x < y)
print(x == y)
print(x >= y)
print(x <= y)
print(x != y)
print("------------------------------")
#EJEMPLO LÓGICOS ESTOS DEVUELVE TRUE O FALSE, SI SE CUMPLE LA CONDICIÓN
print(x<10 and y>2)
print(x<10 or y>2)
print(x<3 and y>2)
print(x<4 or y>2)





