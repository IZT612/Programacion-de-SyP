def sumarNumeros(num1, num2):

    resultado = 0

    mayor = 0
    menor = 0

    if(num1 > num2):

        mayor = num1
        menor = num2
    
    else:

        mayor = num2
        menor = num1

    if (mayor == menor):

        resultado = mayor

    else:

        contador = 0
        contadorLimite = mayor - menor

        while(contador != contadorLimite + 1):

            resultado += menor + contador

            contador += 1

    print(resultado)