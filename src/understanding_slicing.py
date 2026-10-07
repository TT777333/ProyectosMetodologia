players = ['peter', 'mercado', 'aron', 'fatima', 'renata']
print('Lista original: ', players)

# Slicing
print(players[3:5]) # fatima y renata

"""

El slicing me permite trabajar con un grupo especifico de una lista: el resultado se conoce como un slice

"""

# Recuerda que empieza de cero!

print('1:4', players[1:4]) # mercado, aron, fatima
print(':3', players[:3]) # Si dejas vacio es como si pusieras cero. peter, mercado, aron
print('2:', players[2:]) # aron, fatima, renata
print('-3', players[-3:]) # Siempre va de menor a mayor, aron, fatima renata

# Casos especiales del slicing
print(players[-10:10]) # Cuando los indices son mayores que los disponibles, se va hasta el ultimo del lado que sea.
                     # Porque ? porque asi esta programado.


print(players[6:1]) # Si el indice es mayor al final, da lista vacia porque no hay nada.
print(players[:0]) # Tambien retorna una lista vacia.

# Loopings

for player in players[3:5]:
    print(f'El estudiante {player}, va a pasar la materia.')

# Como copiar una lista
my_food = ['pizza', 'tacos', 'flautas']
my_friend_food = my_food # Manera erronea de copiar una lista, si modificas my_friend_food, modificara my_food tambien.

# Maneras para copiar

my_friend_food_2 = my_food[:] # Copia todo lo de la lista
my_friend_food_3 = my_food.copy()
my_friend_food_4 = list(my_food)
