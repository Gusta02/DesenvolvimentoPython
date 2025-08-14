import ipywidgets as widgets
from IPython.display import display, clear_output
import math
import re

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

# Campo de entrada
entrada = widgets.Text(
    value='',
    placeholder='Digite a expressão (ex: 2 + (3*5) - 67 + 33/3*(34-7))',
    description='Entrada:',
    layout=widgets.Layout(width='500px')
)

# Área para exibir resultados
resultado_label = widgets.Label(value="Resultado: ")
resultado_tela = widgets.HTML(value="<b>Aguardando cálculo...</b>")

# Botões principais
botao_calc = widgets.Button(description="Calcular", button_style='success')
botao_limpar = widgets.Button(description="Limpar", button_style='warning')
botao_sair = widgets.Button(description="Sair", button_style='danger')

# Funções
def preparar_expressao(expr):
    # Substitui símbolos comuns para evitar erros
    expr = expr.replace('×', '*').replace('÷', '/')
    expr = expr.replace('–', '-').replace('—', '-')
    expr = re.sub(r'\s+', '', expr)  # remove espaços extras
    return expr

def calcular(b):
    expressao = preparar_expressao(entrada.value)
    try:
        resultado = eval(expressao, {"__builtins__": None}, funcoes)
        resultado_tela.value = f"<b>{entrada.value} = {resultado}</b>"
    except Exception as e:
        resultado_tela.value = f"<b style='color:red;'>Erro: {e}</b>"

def limpar(b):
    entrada.value = ''
    resultado_tela.value = "<b>Aguardando cálculo...</b>"

def sair(b):
    clear_output()
    print("Calculadora encerrada.")

botao_calc.on_click(calcular)
botao_limpar.on_click(limpar)
botao_sair.on_click(sair)

# Botões de funções rápidas
# funcoes_rapidas = [
#     '(', ')', '+', '-', '*', '/', '**', 
#     'sin', 'cos', 'tan', 'sqrt', 'log', 'log10', 'exp', 'pi', 'e'
# ]
# botoes_funcoes = []
# for f in funcoes_rapidas:
#     btn = widgets.Button(description=f, layout=widgets.Layout(width='50px'))
#     btn.on_click(lambda b, val=f: entrada.value.__iadd__(val))
#     botoes_funcoes.append(btn)

# linha_funcoes = widgets.HBox(botoes_funcoes)
linha_botoes = widgets.HBox([botao_calc, botao_limpar, botao_sair])

# Exibir interface
display(entrada)
# display(linha_funcoes)
display(linha_botoes)
display(resultado_label)
display(resultado_tela)
