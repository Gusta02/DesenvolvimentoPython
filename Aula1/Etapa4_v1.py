# 🔹 Como usar

# Execute o código no Google Colab.

# Digite uma expressão no campo de entrada ou use os botões de funções rápidas.

# Clique em Calcular para ver o resultado.

# Para começar de novo, clique em Limpar.

# 🔹 Exemplo de uso:

# sin(pi/2) + sqrt(16) - log10(100)

# Resultado: 5.0

# Instale o ipywidgets

import ipywidgets as widgets
from IPython.display import display, clear_output
import math

# Funções e constantes disponíveis
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

# Output para exibir resultados
output = widgets.Output()

# Campo de entrada
entrada = widgets.Text(
    value='',
    placeholder='Digite a expressão',
    description='Entrada:',
    layout=widgets.Layout(width='500px')
)

# Botão de calcular
botao_calc = widgets.Button(description="Calcular", button_style='success')
botao_limpar = widgets.Button(description="Limpar", button_style='warning')

def calcular(b):
    with output:
        clear_output()
        expressao = entrada.value
        try:
            resultado = eval(expressao, {"__builtins__": None}, funcoes)
            print(f"{expressao} = {resultado}")
        except Exception as e:
            print(f"Erro: {e}")

def limpar(b):
    entrada.value = ''
    with output:
        clear_output()

botao_calc.on_click(calcular)
botao_limpar.on_click(limpar)

# Botões de funções rápidas
# funcoes_rapidas = ['sin', 'cos', 'tan', 'sqrt', 'log', 'log10', 'exp', 'pi', 'e', '+', '-', '*', '/', '**', '(', ')']
# botoes_funcoes = []
# for f in funcoes_rapidas:
#     btn = widgets.Button(description=f, layout=widgets.Layout(width='50px'))
#     def on_click_f(valor):
#         return lambda b: entrada.value.__iadd__(valor)
#     btn.on_click(on_click_f(f))
#     botoes_funcoes.append(btn)

# Organizando os widgets
# linha_funcoes = widgets.HBox(botoes_funcoes)
linha_botoes = widgets.HBox([botao_calc, botao_limpar])

display(entrada)
# display(linha_funcoes)
display(linha_botoes)
display(output)