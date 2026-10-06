# Trabajando con listas
print('\n\t metodo sort')

magicians = ['harry', 'ron', 'hermione', 'snape']
print(magicians[0], magicians[1], magicians[2], magicians[3])

# Si quiero agregar elementos a la lista, tengo que anadirlos manualmente al print para mostrarlos, esto es un problema
# FOR

"""
    for auxiliar in iter:
        actions

    auxiliar son como items en una lista, los nombras al momento de crear el for.
    iter es un iterable
    actions lleva un tab detras para decirle a for que ese es un elemento suyo.
"""

for magician in magicians:
    print(magician.title(), end=' ')

# imprimiendo un mesaje para cada mago
# esto se conoce como looping

print('\n')

for magician in magicians:
    if magician == 'harry':
        print(f'{magician.title()} eres un hechizero {magician.upper()}')
    else:   # elseif existe en python
        print(f'{magician.title()} vaya echizo bro')
        print(f'haz otro {magician.upper()}')
print('solo una vez')    # se imprime solo una vez porque esta no esta indentado

# Identacion - lo que haces al presionar tabulador
"""
    Python utiliza la identacion para determinar
    cuando una linea de codigo esta conectada a la linea de codigo anterior.

    basicamente, se utilizan 4 espacios para en blanco para 
    obligarnos a escribir codigo ordenado y estructurado.

    ayuda a diferenciar donde inicia una linea de codigo y otra termina.
"""

# Estudia tipos de error para reconocerlos!!!! Identacion, name, tipo, sintaxis y logica "identifica tipo de error"
# Estudia error de tipo !
# Recuerda que los errores de sintaxis son los que se muestran primero

# IdentationError - No olvides identar!
for magician in magicians:
    print(magician) # Si esto no se indenta, saldra error, ya que el for necesita al menos un elemento.

# Para que sirve un commit - PREGUNTA DE EXAMEN!!, que es NameError

# Error de logica - aquellos que no se muestran en el traceback
for magician in magicians:
    print(magician) # La variable permanece con el ultimo valor asignado por el for.
print(f'No puedo esperar a ver el siguiente truco, {magician}') # Esta linea no le pertenece al for, pero se ejecutara.
                                                                # Solo una vez...

# IndentationError - Indentaciones ineccesarias. Tambien ocurre con espacios regulares
#message = 'Hello python world!'
#   print(message)

# Para que sirve el ambiente virtual de python y porque se activa. EXAMEN

# metodo built in title (NO ES EL DE STRINGS...aparentemente)
















