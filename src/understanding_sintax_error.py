# Eliminacion de espacios en blanco
programming_language = '    python      '

print(programming_language)
print("Efecto del lstrip")
print(programming_language.lstrip())
print("Efecto del rstrip")
print(programming_language.rstrip())
print("Efecto del strip")
print(programming_language.strip())
print("Variable original")
print(programming_language)

# Error de sintaxis

"""message = 'Una fortaleza de python es su comunidad'
print(message)
message = 'Una fortaleza de 'python' es su comunidad'
print(message)"""

# La unica manera que python vera los errores antes de la ejecucion es si son errores de sintaxis
