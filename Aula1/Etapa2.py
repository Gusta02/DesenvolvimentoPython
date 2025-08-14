import math

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro: divisão por zero!"
    return x / y

def exponenciacao(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        return "Erro: número negativo não tem raiz quadrada real!"
    return math.sqrt(x)

def logaritmo(x, base=10):
    if x <= 0:
        return "Erro: logaritmo indefinido para zero ou número negativo!"
    return math.log(x, base)

def calculadora():
    while True:
        print("\nCalculadora Melhorada")
        print("Selecione a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Exponenciação (x^y)")
        print("6 - Raiz Quadrada")
        print("7 - Logaritmo")
        print("0 - Sair")

        escolha = input("Digite o número da operação: ")

        if escolha == '0':
            print("Saindo...")
            break

        if escolha in ['1', '2', '3', '4', '5']:
            num1 = float(input("Digite o primeiro número: "))
            if escolha != '5':
                num2 = float(input("Digite o segundo número: "))
        elif escolha in ['6', '7']:
            num1 = float(input("Digite o número: "))
            if escolha == '7':
                base = input("Digite a base do logaritmo (pressione Enter para base 10): ")
                base = float(base) if base else 10
        else:
            print("Opção inválida!")
            continue

        if escolha == '1':
            print(f"{num1} + {num2} = {adicao(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
        elif escolha == '5':
            print(f"{num1} ^ {num2} = {exponenciacao(num1, num2)}")
        elif escolha == '6':
            print(f"√{num1} = {raiz_quadrada(num1)}")
        elif escolha == '7':
            print(f"log base {base} de {num1} = {logaritmo(num1, base)}")

if __name__ == "__main__":
    calculadora()
