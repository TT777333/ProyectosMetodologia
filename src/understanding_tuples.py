# Las tuplas no se pueden modificar, no tienen metodos como append ya que son listas como si fueran constantes.

"""

    TUPLAS

    Las tuplas son listas de elementos que no cambian de tamano.
    Las tuplas son listas inmutables.

    Se utilizan los parentesis () para definir una tupla.

   Ejemplo:

        Si tenemos un rectangulo (largo, ancho) que siempre va
        a tener cierto tamano, podemos asegurar que sus dimensiones
        no van a cambiar si colocamos sus valores en una tupla.

    Las tuplas se usan porque cuando uno define una lista, python reserva espacio en la memoria ram ya que asume que su
    tamano aumentara. Las tuplas no tienen este problema, no reservan espacio extra.

"""

dimensions = (200,50) # 200 de largo x 50 de largo
print("tupla original:", dimensions)

# Imprimir elementos de una tupla, es de la misma manera que con una lista
print(dimensions[0])
print(dimensions[1])

# metodo built in dir(arg)

"""
    Muestra los atributos y metodos del argumento.
    Los metodos son aquellos sin _ _
"""

print(dir(dimensions))

# dir de lista
dimensions_2 = [200, 50]
print('Metodos y atributos de las listas\n', dir(dimensions_2))

# dir de string
name = 'charly'
print('Metodos y atributos de los strings\n', dir(name))

# dir de numeros
age = 34
print('Metodos y atributos de los integers\n', dir(age))

# Vamos a modificar el valor de una lista

names = ['carlos', 'charly', 'juan', 'wendy']
print(names)

names[0] = 'mercury'
names[1] = 'mercury'
names[2] = 'mercury'

print(names)

#dimensions[0] = 500 # Type error porque no se pueden cambiar los valores de una tupla.

# looping en tuplas

for dimension in dimensions:
    print(dimension)

# Examen: que puede hacer el slice?
# Las tuplas no se pueden modificar, pero si se puede redefinir la variable

dimensions = (500, 1000, '20')
print('tupla re-definida:', dimensions)

# booleanos en electronica: 0V es false, 5V es true. En logica: 0 es false, 1 es true.

# Tipos de datos booleanos

answer = True
print(answer)
print(dir(answer))



