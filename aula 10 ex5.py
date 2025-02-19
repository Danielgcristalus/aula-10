def calcular_idade(dia, mes, ano):
    # Obter a data atual
    ano_atual = 2025
    mes_atual = 2
    dia_atual = 19

    # Calcular a idade
    idade = ano_atual - ano
    
    # Ajustar a idade caso o aniversário ainda não tenha ocorrido no ano atual
    if (mes_atual, dia_atual) < (mes, dia):
        idade -= 1
    
    return idade

# Exemplo de uso
dia = 15
mes = 5
ano = 2000  # Exemplo: 15 de maio de 2000
idade = calcular_idade(dia, mes, ano)
print(f"A idade da pessoa é: {idade} anos")
