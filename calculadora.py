def calcular(operacao):
    n1 = float(elemento_n1.value)
    n2 = float(elemento_n2.value)
    
    if operacao == '+':
        resultado = n1 + n2
    elif operacao == '-':
        resultado = n1 - n2
    elif operacao == '*':
        resultado = n1 * n2
    elif operacao == '/':
        resultado = n1 / n2
    
    elemento_resultado.innerHTML = f"Resultado: {resultado}"