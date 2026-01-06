from pyscript import Element

def calcular(operacao):
    # Use .value diretamente, é mais seguro nesta versão
    n1_val = Element("n1").value
    n2_val = Element("n2").value
    
    if not n1_val or not n2_val:
        Element("resultado").element.innerText = "Digite os números!"
        return

    num1 = float(n1_val)
    num2 = float(n2_val)
    
    # ... resto do seu código de soma, subtração, etc ...
    
    Element("resultado").element.innerText = f"Resultado: {res}"