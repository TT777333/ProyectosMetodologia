# Agregar elementos a una lista

motorcycles = ['honda', 'mortalica', 'yamaha']
print(motorcycles)

motorcycles.append('kawazaki') # Agrega el elemento al final de la lista
print(motorcycles)

"""
    El metodo append ayuda a crear lista facilmente de manera dinamica.
"""

motorcycles_2 = [] #Lista vacia
print(motorcycles_2)

motorcycles_2.append(motorcycles[0])
motorcycles_2.append(motorcycles[2])
motorcycles_2.append('susuki')

# Metodo insert .insert()

"""
    Agrega un elemento a una lista donde se especifique.
    Pide dos argumentos, donde y que.
"""

# Metodo .pop() Elimina el ultimo elemento de la lista

"""
    Elimina un elemento de la lista por indice,
    si los parentesis se dejan sin nada elimina el ultimo, si pones un int, eliminaras el elemento en aquel indice.
    pero tambien nos permite utilizar el elemento despues de eliminarlo.
    list.pop()
"""

motorcycles_4 = ['honda', 'suzuki', 'hd', 'mortalica']
deleted_motorcycle = motorcycles_4.pop() # honda, suzuki, hd
print(f'Tu motocicleta borrada es: {deleted_motorcycle}') # guarda el elemento borrado en deleted_motorcycle
print(motorcycles_4)

# Tambien puede elminar un elemento especifico
print('eliminar con pop indice')
motorcycles_5 = ['honda', 'suzuki', 'hd', 'mortalica']
print(motorcycles_5)
motorcycles_5.pop(3) # Borra mortalica, si pones un numero mayor a la cantidad de elementos causa un INDEX ERROR.
print(motorcycles_5)

# Metodo .remove(), permite eliminar elementos por su valor
print('metodo remove')
motorcycles_6 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles_6)
motorcycles_6.remove('yamaha')
print(motorcycles_6)



