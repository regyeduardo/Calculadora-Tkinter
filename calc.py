from estilo import Estilo, janela as wi
from teclas import Botoes

janela = Estilo()
janela.define_dimensoes(400, 300)
janela.define_icon("icon.png")
janela.define_titulo("Calculadora")

aux = None
num = None
ope = None


def recebe_teclas(tecla):

    global aux, num, ope

    if tecla.isnumeric():
        if aux is None:
            if num is None:
                aux = tecla
                apresenta_painel(aux)
            else:
                aux = tecla
                apresenta_painel("%s %s %s" % (num, ope, aux))
        else:
            if num is not None:
                aux = "%s%s" % (aux, tecla)
                apresenta_painel("%s %s %s" % (num, ope, aux))
            else:
                aux = "%s%s" % (aux, tecla)
                apresenta_painel("%s" % (aux))
    elif tecla == "*":
        ope = "*"
        if num is None:
            apresenta_painel("%s %s" % (aux, ope))
            num = aux
            aux = None
        elif num is not None and aux is not None:
            num = float(float(num) * float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel("%s %s" % (num, ope))
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        else:
            apresenta_painel("%s %s" % (num, ope))
    elif tecla == "/":
        ope = "/"
        if num is None:
            apresenta_painel("%s %s" % (aux, ope))
            num = aux
            aux = None
        elif num is not None and aux is not None:
            num = float(float(num) / float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel("%s %s" % (num, ope))
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        else:
            apresenta_painel("%s %s" % (num, ope))
    elif tecla == "+":
        ope = "+"
        if num is None:
            apresenta_painel("%s %s" % (aux, ope))
            num = aux
            aux = None
        elif num is not None and aux is not None:
            num = float(float(num) + float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel("%s %s" % (num, ope))
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        else:
            apresenta_painel("%s %s" % (num, ope))
    elif tecla == "-":
        ope = "-"
        if num is None:
            apresenta_painel("%s %s" % (aux, ope))
            num = aux
            aux = None
        elif num is not None and aux is not None:
            num = float(float(num) - float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel("%s %s" % (num, ope))
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        else:
            apresenta_painel("%s %s" % (num, ope))
    elif tecla == "=":
        if num is None or aux is None:
            pass
        elif ope == "*":
            num = float(float(num) * float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel(num)
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        elif ope == "/":
            num = float(float(num) / float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel(num)
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        elif ope == "+":
            num = float(float(num) + float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel(num)
                aux = None
            else:
                apresenta_painel(num)
                aux = None
        elif ope == "-":
            num = float(float(num) - float(aux))
            if num.is_integer():
                num = int(num)
                apresenta_painel(num)
                aux = None
            else:
                apresenta_painel(num)
                aux = None


def apresenta_painel(painel):
    Botoes().cria_label(wi, painel)


# Teclas Numéricas
Botoes().cria_botao(wi, "1", 100, 50, 0, 100, lambda: recebe_teclas("1"))

Botoes().cria_botao(wi, "2", 100, 50, 100, 100, lambda: recebe_teclas("2"))

Botoes().cria_botao(wi, "3", 100, 50, 200, 100, lambda: recebe_teclas("3"))

Botoes().cria_botao(wi, "4", 100, 50, 0, 150, lambda: recebe_teclas("4"))

Botoes().cria_botao(wi, "5", 100, 50, 100, 150, lambda: recebe_teclas("5"))

Botoes().cria_botao(wi, "6", 100, 50, 200, 150, lambda: recebe_teclas("6"))

Botoes().cria_botao(wi, "7", 100, 50, 0, 200, lambda: recebe_teclas("7"))

Botoes().cria_botao(wi, "8", 100, 50, 100, 200, lambda: recebe_teclas("8"))

Botoes().cria_botao(wi, "9", 100, 50, 200, 200, lambda: recebe_teclas("9"))

Botoes().cria_botao(wi, "0", 100, 50, 100, 250, lambda: recebe_teclas("10"))

# Operadores
Botoes().cria_botao(wi, "*", 100, 50, 300, 100, lambda: recebe_teclas("*"))

Botoes().cria_botao(wi, "/", 100, 50, 300, 150, lambda: recebe_teclas("/"))

Botoes().cria_botao(wi, "+", 100, 50, 300, 200, lambda: recebe_teclas("+"))

Botoes().cria_botao(wi, "-", 100, 50, 300, 250, lambda: recebe_teclas("-"))

Botoes().cria_botao(wi, "=", 100, 50, 200, 250, lambda: recebe_teclas("="))

# Funções
Botoes().cria_botao(wi, "C", 100, 50, 0, 250, lambda: recebe_teclas("C"))


# Executando Programa
janela.executa_janela()
