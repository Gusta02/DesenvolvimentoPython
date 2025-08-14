import math

# Dicionário de funções matemáticas permitidas
funcoes = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,          # log(x, base) -> log(x) natural
    'log10': math.log10,
    'exp': math.exp,
    'pi': math.pi,
    'e': math.e,
    'abs': abs,
    'pow': pow
}

def calculadora_cientifica():
    print("=== Calculadora Científica ===")
    print("Digite expressões matemáticas usando operadores +, -, *, /, **, %, ()")
    print("Funções disponíveis: sin(x), cos(x), tan(x), sqrt(x), log(x), log10(x), exp(x), abs(x), pow(x,y)")
    print("Constantes: pi, e")
    print("Digite 'sair' para encerrar.\n")

    while True:
        expressao = input("Digite a expressão: ")
        if expressao.lower() in ['sair', 'exit', 'quit']:
            print("Saindo da calculadora...")
            break
        try:
            # Avalia a expressão usando apenas funções e constantes seguras
            resultado = eval(expressao, {"__builtins__": None}, funcoes)
            print(f"Resultado: {resultado}\n")
        except Exception as e:
            print(f"Erro: {e}\n")

if __name__ == "__main__":
    calculadora_cientifica()
