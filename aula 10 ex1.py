def comparar_numeros():
    # Solicitar a entrada do usuário
    num1 = int(input("Digite um número: "))
    num2 = int(input("Digite outro número: "))

    # Verificar se o primeiro número é par ou ímpar
    if num1 % 2 == 0:
        resultado1 = f"{num1} é par"
    else:
        resultado1 = f"{num1} é ímpar"

    # Verificar se o segundo número é par ou ímpar
    if num2 % 2 == 0:
        resultado2 = f"{num2} é par"
    else:
        resultado2 = f"{num2} é ímpar"
        
    # Retornar os resultados
    return resultado1, resultado2

# Chamar a função e armazenar os resultados
resultado1, resultado2 = comparar_numeros()
print(resultado1)
print(resultado2)
