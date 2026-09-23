# Combinacion o concatenacion de Strings

firstname = "erick"
lastname = "gomez"
fullname = firstname + ' ' + lastname # Concatenacion, combinacion o union, no suma de strings. El resultado es un string.
print(fullname.title())
# Los metodos se pueden usar tanto en valores como en variables
print('hola'.title(), fullname.title()) # Al usar coma en print, se agrega un espacio automaticamente.

# Whitespace

"""
    Cualquier caracter que no se imprime, como un espacio( ), tabulador(\t) o final de linea(\n).
    Utilizados para organizar las salidas de text de tal manera que sea mas facil de leer.
"""

print('python')
print('\tpython')
print('\t\tpython')
print('Lenguajes: \n\tPython\n\tC\n\tJavaScript')

# Concatenacion de strings utilizando f-strings (existen en la version 3.6 hacia adelante)

"""
    Permiten meter variables dentro de los strings
"""

famous_person = 'charly mercury'
message = f'{famous_person.title()} una vez dijo: Python is love' # la f cambia lo que esta entre llaves por la variable.
            # Metodos van dentro de las llave                     # la f y la comilla siempre van juntas f'
print(message)