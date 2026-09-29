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