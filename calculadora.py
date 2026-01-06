from pyscript import Element

def calcular(operacao):
    # Esta linha garante que 'res' sempre exista
    res = 0 
    
    try:
        # Pega os valores das caixas usando os IDs exatos
        n1_val = Element("n1").value
        n2_val = Element("n2").value
        
        if not n1_val or not n2_val:
            Element("resultado").element.innerText = "Resultado: Digite os números!"
            return

        num1 = float(n1_val)
        num2 = float(n2_val)
        
        # Realiza a operação
        if operacao == '+': 
            res = num1 + num2
        elif operacao == '-': 
            res = num1 - num2
        elif operacao == '*': 
            res = num1 * num2
        elif operacao == '/': 
            res = num1 / num2 if num2 != 0 else "Erro: Divisão por 0"
            
        # Mostra o resultado final
        Element("resultado").element.innerText = f"Resultado: {res}"
        
    except Exception as e:
        Element("resultado").element.innerText = "Erro: Use apenas números!"