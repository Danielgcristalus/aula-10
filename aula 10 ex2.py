def multiplicar_tres_numeros(num1, num2, num3):
    # Multiplicar os três números
    resultado = num1 * num2 * num3
    return resultado
num1 = int(input('digite um numero'))
num2 = int(input('digite segundo numero'))
num3 = int(input('digite terceiro numero'))
resultado = multiplicar_tres_numeros(num1, num2, num3)
print(resultado)
