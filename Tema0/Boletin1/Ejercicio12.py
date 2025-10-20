
# Función que hace de calculadora, num1 y num2 son los numeros recibidos, mientras que operacion indica
# la operación a hacer
def calculadora(num1, num2, operacion):

    # Variable que guardará el resultado de la operación
    resultado = 0

    #Si es 1 --> Suma
    if operacion == 1:

        resultado = num1 + num2 

    # 2 --> Resta
    elif operacion == 2:

        resultado = num1 - num2

    # 3 --> Multiplicacion
    elif operacion == 3:

        resultado = num1 * num2

    # 4 --> Division
    elif operacion == 4:

        resultado = num1 / num2

    # Otro --> No existe
    else:

        resultado = "La operación no existe."

    # Devolvemos el resultado
    return resultado

# Probamos

print(str(calculadora(2, 2, 1)))

print(str(calculadora(2, 2, 2)))

print(str(calculadora(2, 2, 3)))

print(str(calculadora(2, 2, 4)))

print(str(calculadora(2, 2, 47)))