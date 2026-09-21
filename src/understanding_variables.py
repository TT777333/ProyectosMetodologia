# Let's try to use variables
message = "This is my first program :), I am very happy"
another_message = "I am not used to english keyboard, holy crap"

print(message)
print(another_message)
print(message, ",", another_message)

message = "Hello everybody"
print(message)

"""
Comentario
en
Bloque

Reglas generales para nombrar variables en PYTHON

    Los nombres de variables deben nombrarse solo con:

    - Palabras en ingles
    - Letras, numeros y guion bajo
    - Deben comenzar con una letra o guion bajo, pero nunca con numeros
    - No deben tener espacios separando las palabras, se usa guion _
    - No utilizar palabras reservadas de python o el nombre del archivo como nombre de variable
    - Los nombres deben ser cortos pero descriptivos
    - Solo letras minusculas, por ahora.

    EX: 
        Correcto: message_1, _message_1
        Incorrecto: 1message_1

"""

message = "Hola amigo python"
print(message)

"""
Traceback:  Registro de donde el interprete tuvo problemas al intentar ejecutar codigo.
    NameError: Sucede al no establecer el nombre de una variable antes de utilizarla o al escribir el nombre de una variable mal
"""

# Strings

"""
    Un string es una serie de caracteres
    En Python, todo lo que se encuentre entre comillas simples ''
    o dentro de comillas dobles es considerado un String.

    Ejemplo:

        "Esto es un string"
        'Esto tambien es un string'
        Los strings puden usar dos tipos de comillas distintas.

        'El lenguaje Python lleva el nombre por "Monty Python", no la serpiente'

"""

name = "Erick Emmanuel Gomez Elizalde"
print(name)

