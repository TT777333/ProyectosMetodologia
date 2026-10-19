"""
    Erick Emmanuel Gomez Elizalde   2630260 IM 1-1
"""

# Resumen ejecutivo

"""
    Los int representan numeros enteros, los float representan numeros decimales, la diferencia entre ambos es que uno solo
    admite valores enteros mientras que el otro permite los decimales. Un booleano es un tipo de dato que sirve para indicar si
    una condicion es verdadera o falsa, para obtener uno a partir de una comparacion solo tienes que ligarla a una condicion.
    Es importante validar rangos para asegurar que el programa sea capaz de procesar listas, tuplas o strings slices de manera
    correcta.
    El documento cubrira 6 problemas, convertidor de temperatura de celsius a farenheit y kelvin, horas de trabajo y sobretiempo
    para calcular pago semanal de un trabajador, determinar si un cliente es elegible a descuento siendo estudiante o anciano,
    estadisticas basicas de enteros: suma, promedio, maxima y minima, y si son pares, eligibilidad de prestamo con base en
    ganancias y deudas, calulador de indice de masa corporal. Las entradas y salidas se hacen para los requisitos del problema
    y se aplican las validaciones especificadas, ademas de que se usan enteros, flotantes y booleanos en las condicionales.
"""

# Principios y buenas practicas

"""
    Usa integers para contadores y float exclusivamente para cantidades con decimales
    Evita duplicar expresiones complejas, guarda resultados intermedios en variables.
    Valida los datos antes de operar
    Usa nombres de variables descriptivos y mensajes claros para el usuario.
    Documenta como se interpretan los booleanos
"""

# Problema 1: Temperature converter and range flag

"""
    Convierte la temperatura en grados celsius introducida a farenheit y kelvin, ademas verifica que los datos introducidos
    sean compatibles y que la temperatura no sea imposible.

    Entradas:
        temp_c (string -> float)

    Salidas:
        temp_f
        temp_k
        is_high_temperature

    Validaciones:
        temp_c debe poder convertirse a float
        No se deben permitir temperaturas fisicamente imposibles

    Casos de prueba:
        Normal: 22
        Borde: 29
"""

temp_c = input('Input a temperature in celsius: ').strip()

if temp_c.isspace() == True or temp_c == '': # Verifica que el valor introducido no sean puros espacios o nada.
    print('Please input a temperature in celsius.')
elif temp_c.replace('.','').replace('-','').isalnum() == False: # Verifica que no hayan caracteres especiales no admisibles.
    print('Please input a numerical value for the temperature measurement.')
elif temp_c.isalpha() == True: # Verifica que el input no sean letras.
    print('Please input a numerical value for the temperature measurement.')
elif str(int(abs(float(temp_c)))).isdigit() == True: # Verifica que el valor sea un numero sin discriminar valores flotantes.

    celsius = float(temp_c)

    if celsius < -273.15:
        print('Under absolute zero!')
    else:
        temp_f = celsius * (9/5) + 32 
        temp_k = celsius + 273.15

        is_high_temperature = False

        if celsius >= 30.0:
            is_high_temperature = True

        print(f'Fahrenheit: {temp_f}')
        print(f'Kelvin: {temp_k}')
        print(f'High temperature: {is_high_temperature}')

else:
    print('Please input a temperature with numbers in celsius.')

# Problema 2: Work hours and overtime payment

"""
    Toma las horas trabajadas y el pago por hora, determina si los valoresson caracteres especiales o alfabeticos, y si no lo son,
    Transforma el string a un float y a partir de este calcula si trabajo sobretiempo ademas de un pago por sobretiempo. Luego
    Otorga el pago regular, por sobretiempo, total y si trabajo sobretiempo.

    Entradas:
        hours_worked (string -> float)
        hourly_rate (string -> float)
        
    Salidas:
        regular_pay
        overtime_pay
        total_pay
        has_overtime

    Validaciones:
        Asegura que hourly_rate sea mayor a 0
        Asegura que hours_worked sea mayor o igual a 0
        Si uno de estos dos no cumple, muestra "Error: invalid input"

    Casos de prueba:
        Normal:
            Input the hours worked: 50 
            Input the hourly rate: 100
        
        Borde:
            Input the hours worked: 39
            Input the hourly rate: 1
"""

hours_worked = input('Input the hours worked: ').strip()
hourly_rate = input('Input the hourly rate: ').strip()

# Verifico que hours_worked y hourly_rate no esten vacios o sean puros espacios.

if hours_worked.isspace() == True or hours_worked == '' or hourly_rate.isspace() == True or hourly_rate == '':
    print('Please input both hours worked and hourly rate.')
else:
    h_w_allowed_chars = hours_worked.replace('.','').replace('-','')
    h_r_allowed_chars = hourly_rate.replace('.','').replace('-','')

    if h_w_allowed_chars.isalnum() == False or h_r_allowed_chars.isalnum() == False: # Verifico que no sean caracteres especiales
        print('Please input numerical values.')
    elif h_w_allowed_chars.isalpha() == True or h_r_allowed_chars.isalpha() == True:
        print('Please input numerical values.')
    else:
        hours_worked = float(hours_worked)
        hourly_rate = float(hourly_rate)

        if hours_worked < 0 or hourly_rate < 0: # Verifico que hours_worked y hourly_rate no sean menores a 0
            print('Error: invalid input')
        else:
            has_overtime = False
            overtime_hours = 0

            if hours_worked > 40: # Veo si ha trabajado mas de 40
                has_overtime = True
                overtime_hours = hours_worked - 40
                regular_pay = 40 * hourly_rate
            else:
                regular_pay = hours_worked * hourly_rate

            overtime_pay = overtime_hours * hourly_rate * 1.5
            total_pay = regular_pay + overtime_pay

            print(f'Regular pay: {regular_pay}')
            print(f'Overtime pay: {overtime_pay}')
            print(f'Total pay: {total_pay}')
            print(f'Has overtime: {has_overtime}')

# Problema 3: Discount eligibility with booleans

"""
    Determina si un cliente tiene descuento en su compra, donde el criterio es: si es estudiante, si es mayor de edad, o si el
    total de la compra es mayor o igual a 1000.

    Entradas:
        purchase_total (string -> float)
        is_student (string)
        is_senior (string)

    Salidas:
        purchase_total

    Validaciones:
        purchase_total debe ser mayor o igual a 0
        Normaliza is_student y is_senior a mayusculas y conviertelos a booleanos
        Si el texto normalizado no es 'YES' o 'NO', mostrar "Error: invalid input"

    Casos de prueba:
        Normal:
            Insert total purchase cost: 1000
            Are you a student? [YES/NO]: Yes
            Are you a senior? [YES/NO]: no
        
        Borde:
            Insert total purchase cost: 999
            Are you a student? [YES/NO]: no
            Are you a senior? [YES/NO]: NO
"""

purchase_total = input('Insert total purchase cost: ').strip()
p_t_allowed_characters = purchase_total.replace('.','').replace('-','')

if purchase_total.isspace() == True or purchase_total == '': # Verifico que purchase_total no sea espacios o nada.
    print('Please input a total purchase cost.')
elif p_t_allowed_characters.isalnum() == False: # Verifico que purchase_total no sean caracteres especiales.
    print('Please input a numeric value.')
elif p_t_allowed_characters.isalpha() == True: # Verifico que purchase_total no sean caracteres alfanumericos.
    print('Please input a numeric value.') 
else:
    purchase_total = float(purchase_total)

    is_student = input('Are you a student? [YES/NO]: ')

    if is_student.upper() != 'YES' and is_student.upper() != 'NO': # Verifico que is_student sea "YES" o "NO"
        print('Error: invalid input')
    else:
        if is_student.upper() == 'YES': # Checo si es estudiante
            is_student = True
        else:
            is_student = False
    
        is_senior = input('Are you a senior? [YES/NO]: ')

        if is_senior.upper() != 'YES' and is_senior.upper() != 'NO': # Verifico que is_senior sea "YES" o "NO"
            print('Error: invalid input')
        else:
            if is_senior.upper() == 'YES': # Checo si es mayor de edad
                is_senior = True
            else:
                is_senior = False

            if is_student == True or is_senior == True or purchase_total >= 1000: # Veo si es elegible para descuento.
                print('Discount eligible: True')
                print(f'Final total: {purchase_total * 0.9}')
            else:
                print('Discount eligible: False')
                print(f'Final total: {purchase_total}')

# Problem 4: Basic satistic of three integers

"""
    Para tres numeros enteros, calcula la suma, el promedio en float, el valor maximo, el valor minimo y un booleano de nombre
    all_even que indica si todos los numeros son pares.

    Entradas:
        n1 (string -> int)
        n2 (string -> int)
        n3 (string -> int)

    Salidas:
        sum_value
        average_value
        max_value
        min_value
        all_even

    Validaciones:
        Los tres valores deben poder convertirse a int
        Se deben permitir negativos
    
    Casos de prueba:
        Normal:     
            Input a number: 4
            Input another number: -2
            Input one last third number: 6
        
        Borde:
            Input a number: 4
            Input another number: 2
            Input one last third number: 5
"""

n1 = input('Input a number: ').strip()

# Veo si n1 esta vacio o tiene caracteres especiales.
if n1.isspace() == True or n1 == '' or n1.replace('.','').replace('-','').isalnum() == False: 
    print('Please input a number')
elif n1.isalpha() == True: # Veo si tiene caracteres alfabeticos
    print('Please input a number')
else:

    n2 = input('Input another number: ')

# Veo si n2 esta vacio o tiene caracteres especiales.
    if n2.isspace() == True or n2 == '' or n2.replace('.','').replace('-','').isalnum() == False:
        print('Please input a number')
    elif n2.isalpha() == True: # Veo si tiene caracteres alfabeticos
        print('Please input a number')
    else:

        n3 = input('Input one last third number: ')

# Veo si n3 esta vacio o tiene caracteres especiales.
        if n3.isspace() == True or n3 == '' or n3.replace('.','').replace('-','').isalnum() == False:
            print('Please input a number')
        elif n3.isalpha() == True: # Veo si tiene caracteres alfabeticos
            print('Please input a number')
        else:
            n1 = int(round(float(n1)))
            n2 = int(round(float(n2)))
            n3 = int(round(float(n3)))

            sum_value = n1 + n2 + n3
            average_value = sum_value / 3
            max_value = max(n1, n2, n3)
            min_value = min(n1, n2, n3)
            all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

            print(f'Sum: {sum_value}')
            print(f'Average: {average_value}')
            print(f'Max: {max_value}')
            print(f'Min: {min_value}')
            print(f'All even: {all_even}')

# Problem 5: Loan eligibility

"""
    Determina si una persona es elegible para un prestamo con base en sus ingresos mensuales, deudas mensuales y puntaje de
    credito

    Entradas:
        monthly_income (string -> float)
        monthly_debt (string -> float)
        credit_score (string -> int)

    Salidas:
        debt_ratio

    Validaciones:
        monthly_income debe ser mayor a 0
        monthly_debt debe no ser negativo
        credit_score debe no ser negativo
        Si no cumple uno de estos criterios, debe mostar "Error: invalid input"

    Casos de prueba:
        Normal:
            Input your monthly income: 9750
            Input your monthly debt: 200
            Input your credit score: 700
        
        Borde:
            Input your monthly income: 7999
            Input your monthly debt: 3,199.5
            Input your credit score: 649
"""

monthly_income = input('Input your monthly income: ').strip()
m_i_allowed_chars = monthly_income.replace('.','').replace('-','')

if monthly_income.isspace() == True or monthly_income == '': # Veo si esta vacio o son puros espacios
    print('Please input a number.')
elif m_i_allowed_chars.isalnum() == False: # Veo si son caracteres especiales
    print('Please input a number.')
elif m_i_allowed_chars.isalpha() == True: # Veo si son caracteres alfanumericos
    print('Please input a number.')
else:

    monthly_debt = input('Input your monthly debt: ')
    m_d_allowed_chars = monthly_debt.replace('.','').replace('-','')

    if monthly_debt.isspace() == True or monthly_debt == '': # Veo si esta vacio o son puros espacios
        print('Please input a number.')
    elif m_d_allowed_chars.isalnum() == False: # Veo si son caracteres especiales
        print('Please input a number.')
    elif m_d_allowed_chars.isalpha() == True: # Veo si son caracteres alfanumericos
        print('Please input a number.')
    else:

        credit_score = input('Input your credit score: ')
        c_s_allowed_chars = credit_score.replace('.','').replace('-','')

        if credit_score.isspace() == True or credit_score == '': # Veo si esta vacio o son puros espacios
            print('Please input a number.')
        elif c_s_allowed_chars.isalnum() == False: # Veo si son caracteres especiales
            print('Please input a number.')
        elif c_s_allowed_chars.isalpha() == True: # Veo si son caracteres alfanumericos
            print('Please input a number.')
        else:
            monthly_income = float(monthly_income)

            if monthly_income > 0: # Me aseguro que sea mayor a cero para evitar la division entre cero
                monthly_debt = float(monthly_debt)
                if monthly_debt >= 0: # Me aseguro que monthly debt no sea negativo
                    credit_score = int(credit_score)
                    if credit_score >= 0: # Me aseguro que credit score no sea negativo
                        debt_ratio = monthly_debt / monthly_income
                        if monthly_income >= 8000 and debt_ratio <= 0.4 and credit_score >= 650: # Veo si cumple eligibilidad
                            print(f'Debt ratio: {debt_ratio}')
                            print('Eligible: true')
                        else:
                            print(f'Debt ratio: {debt_ratio}')
                            print('Eligible: false')
                    else:
                        print('Error: invalid input')
                else:
                    print('Error: invalid input')
            else:
                print('Error: invalid input')

# Problema 6: Body Mass Index

"""
    Calcula el indice de masa corporal de una persona, ademas de que utiliza booleanos para indicar si su peso es bajo, normal o
    si tiene sobrepeso.

    Entradas:
        weight_kg (string -> float)
        height_m (string -> float)

    Salidas:
        bmi
        is_underweight
        is_normal
        is_overweight

    Validaciones:
        weight_kg debe ser mayor a 0
        height_m debe ser mayor a 0
        Si no se cumplen, mostrar "Error: invalid input"

    Casos de prueba:
        Normal:
            Input your weight in kilograms: 50kg
            Input your height in meeters: 1.62m
        
        Borde:
            Input your weight in kilograms: 144kg
            Input your height in meeters: 2.44
"""

weight_kg = input('Input your weight in kilograms: ').strip()

if weight_kg.isspace() == True or weight_kg == '': # Verifico que no este vacio o sean puros espacios
    print('Please input your weight.')
else:
    w_kg_valid_chars = weight_kg.replace('.','').replace('-','').replace('KG','').replace('kg','').strip()

    if w_kg_valid_chars.isalnum() == False: # Verifico que no sean caracteres especiales
        print('Input your weight with numerical values.')
    elif w_kg_valid_chars.isalpha() == True: # Verifico que no sean letras
        print('Input your weight with numerical values.')
    else:
        height_m = input('Input your height in meeters: ')

        if height_m.isspace() == True or height_m == '': # Verifico que no este vacio o sean puros espacios
            print('Please input your height.')
        else:
            h_m_valid_chars = height_m.replace('.','').replace('-','').replace('M','').replace('m','').strip()

            if h_m_valid_chars.isalnum() == False: # Verifico que no sean caracteres especiales
                print('Input your height with numerical values.')
            elif h_m_valid_chars.isalpha() == True: # Verifico que no sean letras
                print('Input your height with numerical values.')
            else:
                weight_kg = float(weight_kg.replace('KG','').replace('kg',''))
                height_m = float(height_m.replace('M','').replace('m',''))

                if weight_kg <= 0 or height_m <= 0: # Verifico que el peso o altura no sean cero.
                    print('Error: invalid input')
                else:
                    bmi = weight_kg / (height_m * height_m)

                    is_underweight = False
                    is_normal = False
                    is_overweight = False

                    if bmi < 18.5: # Checo si es bajo de peso
                        is_underweight = True
                    elif bmi >= 18.5 and bmi < 25: # Checo si tiene peso normal
                        is_normal = True
                    elif bmi >= 25: # Checho si tiene sobrepeso.
                        is_overweight = True

                    print(f'BMI: {round(bmi, 2)}')
                    print(f'Underweight: {is_underweight}')
                    print(f'Normal: {is_normal}')
                    print(f'Overweight: {is_overweight}')

# Conclusiones

"""
    Los enteros y flotantes se usan de forma conjunta para calculos reales donde hayan valores que solo pueden ser enteros y
    valores que pueden ser decimales, las comparaciones nos permiten generar booleanos para tomar decisiones a patir de
    que se cumpla o no una condicion, es importante validar rangos para evitar resultados imposibles y se deben evitar las
    divisiones entre cero ya que no son posibles. Aprendi que las condiciones combinadas son un inmenso dolor de cabeza pero que
    al final llegan a ser relativamente simples y comprensibles. Estos patrones de utilizar enteros, flotantes y condicionales
    se repiten en problemas de nomina, descuentos y prestamos ya que el ser elegible para uno de estos requiere que cumplas
    ciertas metricas las cuales pueden tener un valor entero o decimal.
"""

# Referencias

"""
    1) GeeksforGeeks - Python String isalpha() Method
    2) GeeksforGeeks - float() in Python
    3) W3Schools - Python min() Function
    4) W3Schools - Python max() Function
    5) W3Schools - Python round() Function
"""