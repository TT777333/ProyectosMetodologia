# Ejercicio

"""
    Realizar un programa que determine el costo de un boleto a partir de las siguientes condiciones:

    - Costo para una persona menor o igual a 4 anos: gratis
    - Costo para una persona mayor a 4 pero menor a 18: 200
    - Costo para una persona mayor a 18: 500
"""

# METODO INPUT

"""
    input('mensaje que se mostrara') -> Los datos ingresados a un input regresan en string
"""

# METODO INT

"""
    int(variable) -> Convierte los numeros en string a numeros en int.

    El programa trona si no recibe un string de numeros, o si recibe un numero que no sea entero.
"""

# Costo de un boleto

age = input('Dime tu edad: ')
age = int(age)
# bloque if-elif-else
if age <= 4:
    ticketcost = 0
elif age > 4 and age < 18:
    ticketcost = 200
elif age > 18 and age < 65:
    ticketcost = 500
elif age >= 65:
    ticketcost = 0
# Usualmente se agrega un else al final, pero como el else es un caso que nunca ocurrira, se puede omitir.

print(ticketcost)

