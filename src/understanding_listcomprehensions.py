# Append, operaciones, for e if en una sola linea de codigo

"""
    Una list comprehension combina el loop for y la creacion de nuevos elementos
    en una sola linea y automaticamente agrega cada nuevo elemento a la lista, es decir,
    sin utilizar el metodo append.
"""
squares = [value**2 for value in range(1,11)] # Es una lista con valor de value**2 por cada value en un rango de 1,11
                                              # Funciona como si tuviera un append.
print(squares)

names = ['erick', 'miriam', 'erika', 'alejandra']
names_gomez = [name.title() + ' gomez' for name in names]
print(names_gomez)

