"""
    Erick Emmanuel Gomez Elizalde   2630260 IM 1-1
"""

# Resumen ejecutivo

"""
    Un string es un tipo de dato que describe una serie de caracteres, en python son todo lo que este entre '' o "". Se
    pueden relizar operaciones para concatenar(+,f,strings,join), obtener longitud(len()), extraer sub-cadenas(split(), slicing),
    buscar patrones(starts/endswith, find()) y reemplazar texto.
    Es importanto validar y normalizar el texto para mantener una consistencia que facilite la procesacion de datos.
    Este archivo cubrira 6 problemas, formatear nombres de manera que no tengan espacios extra ni capitalizacion rara, validar
    correos para asegurar que tengan un formato correcto, determinar si una frase en un palindromo ignorando espacios y
    capitalizacion, para una oracion encontrar el numero total de palabras, la primera, la ultima, la mas corta y la mas larga,
    clasificar contrasenas por fuerza segun reglas predefinidas y generar etiquetas para un producto. Se otorgaran salidas y
    entradas en string, se utilizaran validaciones de acuerdo a lo que pide el problema y se usaran diversos metodos string
    ademas de sus aplicaciones. Todo el codigo tambien esta aqui.
"""

# BUENAS PRACTICAS DE PYTHON

'''
    Normaliza la entrada con strip() y lower() antes de hacer comparaciones
    Documenta lo que extraen los slice, no utilizes "numeros magicos"
    Usa metodos string en lugar de reescribir logica basica
    Haz validaciones claras, primero que no este vacia la entrada, y luego la formateas.
    Escribe codigo legible, nombres de variables descriptivos y mensajes de error comprensibles.
'''

# Problema 1: Full name formatter
"""
    Normaliza el texto de entrada y muestra el nombre formateado en title case ademas de sus iniciales. Tambien borra espacios
    extra entre los nombres y niega nombres de puros espacios ademas de requerir estrictamente primer nombre y apellido.

    Entradas: 
        full_name (list)

    Salidas: 
        formatted_name[0] 
        initials

    Validaciones:
        full_name no debe de estar vacio
        full_name ha de contener almenos dos palabras
        El programa no debe aceptar cadenas que solo sean espacios

    Casos de prueba:
        Normal: 
            Primer Nombre: Er ic      k
            Segundo Nombre: Emma NUEl
            Primer Apellido: G O M Ez
            Segundo Apellido: elizA          lde

        Borde: 
            Primer Nombre: Eric k
            Segundo Nombre: 
            Primer Apellido: Gom EZ
            Segundo Apellido: 
"""

letters_first_name = ''
letters_second_name = ''

full_name = [input('First name: '), input('Second name: '), input('First surname: '), input('Second surname: ')] 

for letter in full_name[0]:
    if letter != ' ':
        letters_first_name = letters_first_name + letter
for letter in full_name[2]:
    if letter != ' ':
        letters_second_name = letters_second_name + letter

if letters_first_name == '' or letters_second_name == '':
    print('Please input your name and first surname.')
else:
    formatted_name = []
    initials = ''
    names = ''

    for name in full_name:
        if name != '' and name != ' ':
            names = names + name.replace(' ', '')
            names = names.title() + ' '
    formatted_name.append(names.strip())

    print('Formatted name:',str(formatted_name[0]))

    for letter in str(formatted_name[0]):
        if letter == letter.upper() and letter != letter.lower():
            initials = f'{initials.strip()}{letter.strip()}.' # Se podria hacer con un replace pero no voy a tocar esto

    print(f'Initials: {str(initials).strip()}')

# Problema 2: Simple email validator

"""
    Valida si una direccion de correo tiene un formato basico correcto, que contenga exactamente un @, que despues de este
    tenga minimo un . y que no tenga espacios en blanco. Si cumple este formato, muestra el dominio.

    Entradas: 
        email_text (string)

    Salidas: 
        valid_email
        domain

    Validaciones:
        email_text debe no estar vacio
        El programa debe contar cuantas veces aparece @
        El programa verifica que no se encuentren espacios en email_text

    Casos de prueba:
        Normal: 2630260@upv.edu.mx
        Borde: 2630260@upvedumx
"""

email_text = input('Input an email: ').strip()

has_spaces = None
is_empty = True
has_atdot = False
valid_email = False
ats = 0

for char in email_text:
    if char != ' ' and char != '':
        is_empty = False

if is_empty == False:

    if email_text.find(' ') != -1:
        has_spaces = True
    else:
        has_spaces = False

    for char in email_text:
        if char == '@':
            ats = ats+1 # El programa cuenta los @ mediante la variable ats, pero no se indico que se mostrara la cuenta.

    slice_start = email_text.find('@')

    if email_text[slice_start:].find('.') != -1:
        has_atdot = True

    domain = email_text[slice_start + 1:]

    if is_empty == False and has_spaces == False and has_atdot == True:
        valid_email = True
        print(f'Valid email: {valid_email}')
        print(f'Domain: {domain}')
    else:
        print(f'Valid email: {valid_email}')

else:
    print('Valid email: False')
    print('email must contain characters other than space.')

# Problema 3: Palindrome checker

"""
    Determina si una frase es un palindromo (se lee igual de izquierda a derecha), ignorando espacios y capitalizacion. Ademas
    comprueba que tenga una longitud minima de 2 caracteres.

    Entradas: 
        phrase (string)

    Salidas: 
        is_palindrome

    Validaciones:
        phrase debe no estar vacia
        la longitud minima debe ser de 3 caracteres, sin contar espacios.

    Casos de prueba:
        Normal: Anita lava la tina 
        Borde: Hi
"""

letters = ''
is_palindrome = None
is_empty = True

phrase = input('Input a phrase: ')

for char in phrase:
    if char != ' ' and char != '':
        is_empty = False

if is_empty == False:
    if len(phrase.strip()) >= 2:
        letters = phrase.replace(' ', '')
        reversed_letters = letters[::-1].lower()

        if letters.lower() == reversed_letters:
            is_palindrome = True
        else:
            is_palindrome = False

        print(f'Is palindrome: {is_palindrome}')
        print(f'Normalized version: {letters.lower()}')
    else:
        print('Phrase must have atleast 2 letters!')
else:
    print('Input atleast two characters that differ from space.')

# Problema 4: Sentence word stats

'''
    Normaliza espacios, separa las palabras, y muestra el numero total de palabras, la primera palabra, la ultima, y la palabra
    mas corta y larga.

    Entradas:
        sentence (string)
    
    Salidas:
        sentence_words
        shortest_word
        longest_word

    Validaciones:
        La oracion no puede estar vacia
        La oracion debe contener al menos una palabra

    Casos de prueba:
        Normal:
            Anita lava la tina
        Borde:
            a                 
'''

sentence = input('Input a sentence: ') # De este problema en adelante comienzo a investigar

if sentence.isspace() == True or sentence == '':    # Como pide referencias asumo que investigar metodos no vistos esta permitido
    print('Please input atleast one word.')
else:
    words = ''
    sentence_words = sentence.strip().split() # Acabo de descubrir que split ignora espacios
    shortest_word = sentence_words[0]
    longest_word = sentence_words[0]

    for word in sentence_words:
        words = words + str(word) + ' '
        words = words.strip().lower()

    for word in sentence_words:
        if len(word) < len(shortest_word):
            shortest_word = word

    for word in sentence_words:
        if len(word) > len(longest_word):
            longest_word = word

    print('Word count:', len(sentence_words))
    print('Fist word:', sentence_words[0])
    print('Last word:', sentence_words[-1])
    print('Shortest word:', shortest_word)
    print('Longest word:', longest_word)

# Problema 5: Password strenght classifier

"""
    Clasifica una clave en 'weak', 'medium' o 'strong' segun la longitud, capitalizacion y mezcla de caracteres alfabeticos con
    numericos y no alfanumericos.

    Entradas:
        password_input (string)

    Salidas:
        password_strenght

    Validaciones:
        No acepta clave vacia
        Se verifica la longitud mediante el metodo len()

    Casos de prueba:
        Normal:
            CharlyRocks123
        Borde:
            charlyrocks123              
"""

password_input = input('Input a password: ')

if password_input.isspace() == True or password_input == '':
    print('Please input a password.')
else:
    password_strenght = 'weak'
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password_input:
        if char.isupper() == True:
            has_upper = True

        if char.islower() == True:
            has_lower = True

        if char.isdigit() == True:
            has_digit = True

        if char.isalnum() == False:
            has_special = True

    if len(password_input) >= 8 and has_special == True and has_digit == True and has_upper == True and has_lower == True:
        password_strenght = 'strong'
    elif len(password_input) >= 8 and has_digit == True and has_upper == True and has_lower == True:
        password_strenght = 'medium'
    elif len(password_input) < 8 or has_digit == False and has_special == False:
        password_strenght = 'weak'

    print('Password strenght:', password_strenght)

# Problema 6: Product label formatter

"""
    Dado el nombre de un producto, y considerando su precio , se genera una etiqueta de una sola linea con el formato:
    Product: <NAME> | Price: $<PRICE>, donde debe tener exactamente 30 caracteres.

    Entradas:
        product_name (string)
        product_price (string)

    Salidas:
        label

    Validaciones:
        Product name debe no estar vacio
        price_value debe poder convertirse a un numero positivo.

    Casos de prueba:
        Normal:
            Ingrese el nombre del producto: Cookie
            Ingrese el precio del producto: 20

        Borde:
            Ingrese el nombre del producto: Coche
            Ingrese el precio del producto: 99999 
"""

product_name = input('Input the product name: ').strip()

if product_name.isspace() == True or product_name == '':
    print('Please input a product name.')
else:
    price_value = input('Input a product price: ').strip()
    if price_value.isspace() == True or price_value == '':
        print('Please input a product price.')
    else:
        if str(abs(int(price_value))).isdigit() == True:

            product_words = product_name.split()
            normalized_name = ''
            shortend_name = ''
            shortend_number = ''

            for word in product_words:
                normalized_name = normalized_name + word + ' '

            normalized_name = normalized_name.rstrip()

            if len(normalized_name) > 4:
                shortend_name = normalized_name[:5]
            else:
                shortend_name = normalized_name

            if len(price_value) > 5:
                if abs(int(price_value)) >= 100000 and abs(int(price_value)) < 1000000:
                    shortend_number = f'{round(int(price_value) / 1000)}k'
                elif abs(int(price_value)) >= 1000000 and abs(int(price_value)) < 1000000000:
                    shortend_number = f'{round(int(price_value) / 1000000)}M'
                elif abs(int(price_value)) >= 1000000000:
                    shortend_number = 'pricy'
            else:
                shortend_number = price_value

            label = f'Product: {shortend_name} | Price: ${shortend_number}                              '
            
            if label[30] != ' ':
                print(f'Label: "{label[:31]}"')
            if label[30] == ' ':
                print(f'Label: "{label[:30]}"')

        else:
            print('Please input a whole value without separators.')

# Conclusiones

"""
    Manejar strings en la entrada y salida de datos es escencial para recibir informacion, interpretarla y procesarla de manera
    correcta para cumplir la funcion deseada. lower() conviene usarse al comparar strings donde la capitalizacion no importe,
    strip() es muy conveniente en casi todos los casos ya que se deshace de espacios extras que usualmente solo estan de estorbo,
    split es MUY conveniente para separar palabras y borrar espacios extra entre sentencias que strip() no puede alcanzar y
    la concatenacion siempre es util. El texto siempre debe ser normalizado antes de compararlo para que, cuando la capitalizacion
    no importe, se pueda realizar una comparacion correcta entre strings. Las validaciones evitan errores y datos basura al guiar
    el desarrollo del programa. Aprendi que los strings no cambian, solo se crean y destruyen, ademas de que slice() es la
    salvacion en contra de espacios que strip() no alcanza.
"""

# Referencias

"""
    1) W3Schools - Python round() Function
    2) W3Schools - Python abs() Function
    3) W3Schools - Python String isspace() Method
    4) pytutorial - Python: Find Shortest or Longest Word in String
    5) Python documentation - Built-in Types: Text Sequence Type - str
"""