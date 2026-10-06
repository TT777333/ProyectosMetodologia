# Listas de numeros

"""
    Las listas tambien pueden almacenar numeros. Python ofrece varias
    herramientas que ayudan a trabajar eficientemente con listas de numeros.
"""

# Metodo built-in range()

"""
    El metodo range() nos ayuda a crear facilmente
    series de numeros.
"""

for value in range(1,5): # Cerrado por la izquierda, abierto por la derecha. Empieza en 1, pero no llega al 5
    print(value)

# range solo genera numeros.

"""
Algunos metodos built-in

print() - Imprime sus argumentos
sorted()
type() - Retorna el tipo de dato del argumento
len()
str() - Convierte los argumentos a string??
list() - Crea una lista con los argumentos especificados

"""

numbers0to9 = list(range(0,10))
print(numbers0to9)

print('==========')

numbers0to10pair = list(range(0,11,2)) # El tercer argumento de range define el paso del incremento, en este caso 2 en 2.
print(numbers0to10pair) # + 'hola' genera un error de tipo

print(type(numbers0to10pair))
print(str(numbers0to10pair) + 'hola') # no genera un error de tipo porque ambos son string

tabla_del_cinco = list(range(5,51,5)) 
print(tabla_del_cinco)

print('==========')

table_of_squares = []
for value in range(1,11):
    table_of_squares.append(value**2) # Solo has una variable que tenga el valor por iteracion si la vas a usar
    print(table_of_squares)
print('end')



