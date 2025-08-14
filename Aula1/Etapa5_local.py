import tkinter as tk
import math
import re

# Funções e constantes disponíveis para eval
funcoes = {
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
    'sqrt': math.sqrt,
    'log': math.log,      # log natural
    'log10': math.log10,
    'exp': math.exp,
    'pi': math.pi,
    'e': math.e,
    'abs': abs,
    'pow': pow
}

# Função para corrigir e preparar expressão
def preparar_expressao(expr):
    expr = expr.replace('×', '*').replace('÷', '/')
    expr = expr.replace('–', '-').replace('—', '-')
    expr = re.sub(r'\s+', '', expr)  # remove espaços extras
    return expr

# Função para calcular
def calcular():
    expressao = preparar_expressao(entrada.get())
    try:
        resultado = eval(expressao, {"__builtins__": None}, funcoes)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, f"Erro: {e}")

# Função para limpar
def limpar():
    entrada.delete(0, tk.END)

# Função para inserir texto no campo
def inserir(valor):
    entrada.insert(tk.END, valor)

# Criar janela principal
janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("400x500")
janela.resizable(False, False)

# Campo de entrada
entrada = tk.Entry(janela, font=("Arial", 18), justify="right", bd=10, relief="sunken")
entrada.pack(fill="both", padx=10, pady=10)

# Frame para botões
frame_botoes = tk.Frame(janela)
frame_botoes.pack()

# Lista de botões
botoes = [
    ('7', '8', '9', '/', 'sqrt'),
    ('4', '5', '6', '*', 'log'),
    ('1', '2', '3', '-', 'log10'),
    ('0', '.', '(', ')', '+'),
    ('pi', 'e', 'sin', 'cos', 'tan'),
    ('exp', '**', 'C', '=', 'Sair')
]

# Criar botões
for linha in botoes:
    linha_frame = tk.Frame(frame_botoes)
    linha_frame.pack(side="top", expand=True, fill="both")
    for texto in linha:
        if texto == "C":
            btn = tk.Button(linha_frame, text=texto, font=("Arial", 14), width=6, height=2, 
                            command=limpar)
        elif texto == "=":
            btn = tk.Button(linha_frame, text=texto, font=("Arial", 14), width=6, height=2, 
                            command=calcular, bg="lightgreen")
        elif texto == "Sair":
            btn = tk.Button(linha_frame, text=texto, font=("Arial", 14), width=6, height=2, 
                            command=janela.destroy, bg="tomato")
        else:
            btn = tk.Button(linha_frame, text=texto, font=("Arial", 14), width=6, height=2, 
                            command=lambda val=texto: inserir(val))
        btn.pack(side="left", expand=True, fill="both", padx=1, pady=1)

# Rodar a interface
janela.mainloop()
