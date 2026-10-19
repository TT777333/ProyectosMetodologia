"""
    Erick Emmanuel Gomez Elizalde   2630260 IM 1-1
"""

# Resumen ejecutivo

"""
    Una lista es un conjunto de objetos que pueden ser de distintos tipos de datos, son mutables, lo que significa que estas 
    pueden cambiar de tamano al agregar mas objetos. Una tupla es como una lista, solo que estas son inmutables, lo que significa
    que no pueden cambiar de tamano ni se les puede agregar nuevos objetos. Un diccionario es similar a ambos, solo que estos
    utilizan un sistema de llave : valor, estos son mutables. Los diccionarios crean una coleccion que asocia claves con valores,
    donde se puede llamar la clave para recibir el valor de esta misma. Este documento cubrira 6 problemas: Crear una lista de
    compras donde se puedan agregar productos, saber su tamano, y ver si un producto se encuentra en esta; uso de tuplas para
    representar dos puntos en un plano 2D; catalogo de productos donde se use un diccionario para relacionar los productos a un
    precio; administrar las calificaciones de un grupo utilizando un diccionario que relacione el alumnno a sus calificaciones; un
    contador de frecuencia de palabras en una oracion que use un diccionario, y un libro de contacto que use diccionarios. Se
    crearan entradas para lo pedido, e igualmente se seguiran las validaciones pedidas y se usaran listas, tuplas y diccionarios.
"""

# Principios y buenas practicas

"""
    Usa listas cuando necesites agregar o eliminar elementos con frecuencia
    Usa tuplas para datos que no deben cambiar
    Usa diccionarios para buscar informacion por claves
    Solo modifica una lista mendiante un for si sabes lo que estas haciendo
    Usa claves descriptivas en los diccionarios
    Escribe codigo legible y mensajes claros para el usuario.
"""

# Problema 1: Shopping list basics

"""
    Con una lista de productos y sus cantidades, se crea una lista inicial de productos, se permite agregar un nuevo producto
    al final, se muestra la cantidad total de elementos en la lista y se verifica si un producto en especifico se encuentra en
    la lista.

    Entradas:
        new_item (string)
        search_item (string)

    Salidas:
        items_list
        found_item
    
    Validaciones:
        inital_items debe no estar vacio
        La cadena debe ser separada por comas y se deben eliminar espacios extra en cada elemento
        new_item y serach_item deben no estar vacios
        Manejar el caso de lista inicial vacia si el estudiante lo decide (no)
    
    Casos de prueba:
        Normal:
            Input an item to add to the list: paint
            Input an item name to search in the list: paint
        Borde:
            Input an item to add to the list: cheese
            Input an item name to search in the list: chees
"""

items_list = ['cookies','potatochips','coke','toothbrush']
new_item = input('Input an item to add to the list: ').strip().lower().split()
new_item = str(new_item).replace('[','').replace(']','').replace("'","").replace(',',' ').strip()

if new_item.isspace() == True or new_item == '':
    print('Item must have a name with alphanumeric or special characters.')
else:
    items_list.append(new_item)
    found_item = False

    search_item = input('Input an item name to search in the list: ').strip().lower()
    
    if search_item.isspace() == True or search_item == '':
        print('Item to search must have a name with alphanumeric or special characters')
    else: 
        if search_item in items_list:
            found_item = True

        print('Items list:', items_list)
        print('Total items:', len(items_list))
        print('Found item:', found_item)
    
# Problema 2: Points and distances with tuples

"""
    Se usa una tupla para representar dos puntos en un plano 2D, el programa crea dos tuplas, calcula la distancia entre los
    puntos y crea una nueva tupla midpoint con el punto medio entre los puntos.

    Entradas:
        x1 (string -> float)
        y1 (string -> float)
        x2 (string -> float)
        y2 (string -> float)

    Salidas:
        point_a
        point_b
        distance
        mid_point

    Validaciones:
        Verificar que las 4 entradas se puedan convertir a float
        Permitir numeros negativos

    Casos de prueba:
        Normal:
            Input the x coordinate for point a: 2
            Input the y coordinate for point a: 2
            Input the x coordinate for point b: 4
            Input the y coordinate for point b: 4
        Borde:
            Input the x coordinate for point a: 2
            Input the y coordinate for point a: 3
            Input the x coordinate for point b: 4
            Input the y coordinate for point b: a
"""

x1 = input('Input the x coordinate for point a: ').strip()
y1 = input('Input the y coordinate for point a: ').strip()
x2 = input('Input the x coordinate for point b: ').strip()
y2 = input('Input the y coordinate for point b: ').strip()

x1_allowed_chars = x1.replace('.','').replace('-','')
y1_allowed_chars = y1.replace('.','').replace('-','')
x2_allowed_chars = x2.replace('.','').replace('-','')
y2_allowed_chars = y2.replace('.','').replace('-','')

if x1.isspace() == True or x1 == '' or y1.isspace == True or y1 == '':
    print('Please input x and y coordinates for point a.')
elif x1_allowed_chars.isalnum() == False or y1_allowed_chars.isalnum() == False:
    print('Please input numerical values for x and y coordinates.')
elif x1_allowed_chars.isalpha() == True or y1_allowed_chars.isalpha() == True:
    print('Please input numerical values for x and y coordinates.')
else:

    if x2.isspace() == True or x2 == '' or y2.isspace == True or y2 == '':
        print('Please input x and y coordinates for point b.')
    elif x2_allowed_chars.isalnum() == False or y2_allowed_chars.isalnum() == False:
        print('Please input numerical values for x and y coordinates.')
    elif x2_allowed_chars.isalpha() == True or y2_allowed_chars.isalpha() == True:
        print('Please input numerical values for x and y coordinates.')
    else:
        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)

        point_a = (x1, y1)
        point_b = (x2, y2)

        distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
        mid_point = ((x1+x2)/2, (y1+y2)/2)

        print('Point A', point_a)
        print('Point B', point_b)
        print('Distance:', distance)
        print('Midpoint:', mid_point)

# Problema 3: Product catalog with dictionary

'''
    Se crea un catalogo de productos en forma de diccionario de 3 productos, se debe poder leer el nombre del producto y la
    cantidad a comprar, se debe poder sacar un total a pagar si el producto existe, y si no, sale un error. 

    Entradas:
        product_name (string)
        quantity (string -> int)
    
    Salidas:
        unit_price
        quantity
        total_price
    
    Validaciones:
        quantity debe ser mayor a 0
        product_name debe no estar vacio
        product_name debe estar en el diccionario como clave
    
'''
# OMITIDO POR INSTRUCCION

# Problema 4: Student grades with dict and list

'''
    Se crea una lista de calificaciones en forma de diccionario de 3 estudiantes, donde se puede leer el nombre de cada
    estudiante, calcular el promedio de sus calificaciones e indicar si esta aprobado.

    Entradas:
        student_name (string)

    Salidas:
        grades_list
        average
    
    Validaciones:
        student_name debe no estar vacio
        student_name debe ser una clave en el diccionario
        la lista de calificaciones debe no estar vacia antes de calcular el promedio
'''
# OMITIDO POR INSTRUCCION

# Problema 5: Word frequency counter

'''
    Cuenta la frecuencia de cada palabra en una oracion mediante una lista y un diccionario que guarda la palabra y su
    frequencia. Lee la oracion, convierte todo a minusculas y separa las palabras en la lista, por ultimo, muestra el
    diccionario completo y la palabra mas frecuente.

    Entradas:
        sentence (string)
    
    Salidas:
        words_list
        freq_dic
        word

    Validaciones:
        sentence debe no estar vacia
        Manejar signos de puntuacion (inconcluso)
        la lista de palabras debe no estar vacia   
'''
# OMITIDO POR INSTRUCCION

# Problema 6: Simple contact book

'''
    Se crea un "contact book" usando un diccionario, se crea un diccionario inicial con algunos contactos, y se lee una accion
    la cual segun la accion, agrega, busca o borra nombres ademas de que muestra un mensaje indicando el resultado de la
    operacion.

    Entradas:
        action_text (string)
        name (string)
        phone (string)
    
    Salidas:
        name
        phone

    Validaciones:
        action_text debe ser mayusculas
        action_text debe ser solo 'ADD' 'SEARCH' o 'DELETE'
        name debe no estar vacio
        Al agregar con 'ADD', phone debe no estar vacio
       
'''
# OMITIDO POR INSTRUCCION

# Conclusiones

'''
    Conviene usar listas cuando cambiaras datos constantes, tuplas cuando no cambiaras datos del conjunto y diccionarios cuando
    necesitas llamar a un valor mediante una clave. Las listas son mutables, por lo que se le pueden agregar y eliminar elementos
    de forma flexible. Las tuplas son utiles para datos que no deben cambiar porque no reservan espacio extra que puede ser
    utilizado para otra cosa. Los diccionarios facilitan busquedas rapidas al relacionar valores con claves especificas.
    [Inconcluso]
'''

# Referencias

'''
    1) Python documentation - Built-in Types: list, tuple, dict
    2) W3Schools - Python Dictionaries
    3) W3Schools - Python in keyword
    4) W3Schools - Python Dictionary Methods
    5) W3Schools - Python - List Methods
'''