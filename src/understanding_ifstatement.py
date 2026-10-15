# Estructura de if statement

"""

if condition:           El corazon del if es la condicion.
    do something }      Acciones verdaderas
else:
    do something }      Acciones falsas

"""

# If statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car)

# Condicionales (importante)

# El condicional

"""
    Lo que va al ladito del if, es el corazon del if.
    Para determinar igualdad, utilizamos == , no es lo mismo que =, = asigna variables == es condicional de igualdad
"""

# Condicional True/Verdadero
print('Condicional Verdadero')
truck = 'ford'
print(truck == 'ford') # Imprime True porque esto es verdadero, ford == ford
print(truck == 'Ford'.lower()) # Metodos se ejecutan antes que la condicional
print('ford' == 'audi')

# Condicional False/Falso
print('Condicional Falso')
print(truck == 'cheyenne')  # Imprime False porque esto es falso, ford =/= cheyenne

# El == se llama conector o condicional de igualdad, compara lo de la izquierda a lo de la derecha, los tipos de dato importan.

print('Condicional de desigualdad')

# Condicional != para determinar desigualdad, compara para ver si lo de la izquiera es distinto a lo de la derecha

print(truck != 'tacoma') # Retorna true porque ford no es igual a tacoma.
print(truck != 'ford') # Retorna false porque ford es igual a ford

# Comparaciones numericas

print('\nComparaciones numericas')
age = 34 
print(age == 34) # True
print(age == 18) # False
print(age == '34') # False, porque los tipos de datos son distintos.

# !!! Python es un lenguaje de Tipado fuerte, lo que significa que 34 es distinto de '34'
# Tipado debil es donde 34 == '34'

# if

answer = 17
if answer != 42:
    print('Esa no es la respuesta correcta') # Else no es obligatorio.

# Condicional <

print('Simbolos de menor y mayor que')
age = 19
print(age < 21) # < pregunta si lo de la izquierda es menor a lo de la derecha
print(age <= 21) # <= pregunta si lo de la izquiera es menor o igual a lo de la derecha
age = 21
print(age < 21) # False
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # True

# Operaciones booleanas

"""
    AND, OR, NOT (XOR y otras derivan de estas)

    AND alojara verdadero solo cuando todas sus condiciones sean verdaderas. Retorna falso en cualquier otro caso.
    OR alojara verdadero si almenos una de sus condiciones es verdadera. Retorna falso solo si todas son falsas.
    NOT alojara el booleano opuesto de la condicion.

    las tablas de verdad son aquellas que muestran los resultados de operaciones booleanas, y tienen una cantidad de
    resultados calculable meidante la formula 2^n donde n es la cantidad de condicionales
    
"""

