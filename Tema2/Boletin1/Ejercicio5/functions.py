def sumarNumeros(num1, num2):

    if num1 > num2:
        mayor = num1
        menor = num2
    else:
        mayor = num2
        menor = num1

    resultado = 0
    contador = menor

    while contador <= mayor:
        resultado += contador
        contador += 1

    print(resultado)