"""
    Las listas nos permiten almacenar informacion en un lugar y
    cantidad que se desee: ya sean pocos elementos o millones de elementos.

    Una lista es una coleccion de items (elementos) que tienen un orden particular.
    Se pueden crear listas que incluyan strings, enteros, floats, podemos almacenar los
    tipos de datos que queramos en una lista.

    Son elementos Mutables: lo que indica que puede modificarse el tamano de la lista
    en tiempo de ejecucion.
    
!!! Se recomienda nombrar una variable de tipo lista en plural.

    En Python, los corchetes [] indican una lista, sus elementos se separan por comas.

"""

spec = 'specialized'

bicycles = ['trek', 'cannondale', 'redline'.title(), spec, "apache"]
print(bicycles)

# Como podemos acceder a los elementos de una lista?

"""
    Las listas son colecciones ordenadas. Se puede acceder
    a un elemento de una lista diciendole a Python la posicion o
    indice del elemento deseado.

    Para obtener el valor deseado, se escribe el nombre de la lista,
    seguido del indice del elemento entre corchetes.
"""

print(bicycles[0], bicycles[1], bicycles[2])
print(bicycles[0].upper())

# Los indices comienzan en 0, no en 1

# Que otra manera existe sin saber el tamano de la lista?

print(f"My first bicycles was a {bicycles[-2].upper()}")




