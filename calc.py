import tkinter as tk
from tkinter import PhotoImage

menu_iniciar = tk.Tk()  # Criando uma janela
menu_iniciar.title("Calculadora")  # Nomenado título da janela

# Definindo a largura e a altura
largura = 400
altura = 300

# Extraindo a resolução do sistema
largura_screen = menu_iniciar.winfo_screenwidth()
altura_screen = menu_iniciar.winfo_screenheight()

# # Definindo posição da janela
posx = int(largura_screen / 2 - largura / 2)
posy = int(altura_screen / 2 - altura / 2)
# Calculo para sempre centralizar a tela

menu_iniciar.geometry(
    f"{largura}x{altura}+{posx}+{posy}"
)  # Definindo tamanho e posicionamento ("WxH+X+Y")

menu_iniciar.resizable(False, False)  # Definindo se é redimensionável ou não
# menu_iniciar.minsize(300, 300)  # Definindo a dimensão mínima
# menu_iniciar.maxsize(300, 300)  # Deinindo a dimensão máxima
# menu_iniciar.state(
#     "iconic"
# )  # Definindo como a janela deve iniciar, se é em tela cheia ou modo normal
"""
Com withdrawn o app não abriu
e com zoomed deu erro
"""
# menu_iniciar.iconbitmap("icon.png")
# Estava dando erro em definir a o icóne desse jeito
menu_iniciar.iconphoto(True, PhotoImage(file="icon.png"))  # Definindo o ícone
"""
Teve que ser assim, pois foi o jeito que deu certo e não funcionou com o
arquivo .ico
"""

tela = ""
num2 = None
num1 = None
aux = None


def apresenta_painel(painel):
    tk.Label(menu_iniciar,
             text=painel,
             font="Arial 20",
             justify=tk.CENTER
             ).place(x=0,
                     y=0,
                     width=400,
                     height=100)


def digitos(n):
    global tela, num1, aux
    operadores = " x - / + "

    if n.isnumeric():
        if aux is None:
            if num1 is None:
                aux = n
                apresenta_painel(aux)
            else:
                aux = n
                apresenta_painel("%s%s" % (tela, aux))
        elif num1 is None:
            aux = "%s%s" % (aux, n)
            apresenta_painel(aux)
        else:
            aux = "%s%s" % (aux, n)
            apresenta_painel("%s%s" % (tela, aux))
    elif n in operadores:
        if tela == "" and aux is None:
            apresenta_painel("inválido")
        elif n == " x ":
            if num1 is None:
                tela = "%s%s" % (aux, n)
                num1 = aux
                aux = None
                apresenta_painel(tela)
            else:
                tela = "%s%s" % (int(num1) * int(aux), n)
                apresenta_painel(tela)
                num1 = int(num1) * int(aux)
                aux = None
        elif n == " / ":
            if num1 is None:
                tela = "%s%s" % (aux, n)
                num1 = aux
                aux = None
                apresenta_painel(tela)
            else:
                tela = "%s%s" % (float(num1) / float(aux), n)
                apresenta_painel(tela)
                num1 = float(num1) / float(aux)
                aux = None
        elif n == " + ":
            if num1 is None:
                tela = "%s%s" % (aux, n)
                num1 = aux
                aux = None
                apresenta_painel(tela)
            else:
                tela = "%s%s" % (float(num1) + float(aux), n)
                apresenta_painel(tela)
                num1 = float(num1) + float(aux)
                aux = None
        elif n == " - ":
            if num1 is None:
                tela = "%s%s" % (aux, n)
                num1 = aux
                aux = None
                apresenta_painel(tela)
            else:
                tela = "%s%s" % (float(num1) - float(aux), n)
                apresenta_painel(tela)
                num1 = float(num1) - float(aux)
                aux = None
    elif n == "C":
        tela = ""
        num1 = None
        aux = None
        apresenta_painel("")


# Teclas numéricas
btn1 = tk.Button(
    menu_iniciar,
    text="1",
    command=lambda: digitos("1")
).place(x=0,
        y=100,
        width=100,
        height=50)

btn2 = tk.Button(
    menu_iniciar,
    text="2",
    command=lambda: digitos("2")
).place(x=100,
        y=100,
        width=100,
        height=50)

btn3 = tk.Button(
    menu_iniciar,
    text="3",
    command=lambda: digitos("3")
).place(x=200,
        y=100,
        width=100,
        height=50)

btn4 = tk.Button(
    menu_iniciar,
    text="4",
    command=lambda: digitos("4")
).place(x=0,
        y=150,
        width=100,
        height=50)

btn5 = tk.Button(
    menu_iniciar,
    text="5",
    command=lambda: digitos("5")
).place(x=100,
        y=150,
        width=100,
        height=50)

btn6 = tk.Button(
    menu_iniciar,
    text="6",
    command=lambda: digitos("6")
).place(x=200,
        y=150,
        width=100,
        height=50)

btn7 = tk.Button(
    menu_iniciar,
    text="7",
    command=lambda: digitos("7")
).place(x=0,
        y=200,
        width=100,
        height=50)

btn8 = tk.Button(
    menu_iniciar,
    text="8",
    command=lambda: digitos("8")
).place(x=100,
        y=200,
        width=100,
        height=50)

btn9 = tk.Button(
    menu_iniciar,
    text="9",
    command=lambda: digitos("9")
).place(x=200,
        y=200,
        width=100,
        height=50)

btn0 = tk.Button(
    menu_iniciar,
    text="0",
    command=lambda: digitos("0")
).place(x=100,
        y=250,
        width=100,
        height=50)

# Funções
btn_c = tk.Button(
    menu_iniciar,
    text="C",
    command=lambda: digitos("C")
).place(x=000,
        y=250,
        width=100,
        height=50)

# Operadores e funções
btn_igual = tk.Button(
    menu_iniciar,
    text="=",
    command=lambda: print("")
).place(x=200,
        y=250,
        width=100,
        height=50)

btn_multiplicar = tk.Button(
    menu_iniciar,
    text="*",
    command=lambda: digitos(" x ")
).place(x=300,
        y=100,
        width=100,
        height=50)

btn_divisao = tk.Button(
    menu_iniciar,
    text="/",
    command=lambda: digitos(" / ")
).place(x=300,
        y=150,
        width=100,
        height=50)

btn_adicao = tk.Button(
    menu_iniciar,
    text="+",
    command=lambda: digitos(" + ")
).place(x=300,
        y=200,
        width=100,
        height=50)

btn_subtracao = tk.Button(
    menu_iniciar,
    text="-",
    command=lambda: digitos(" - ")
).place(x=300,
        y=250,
        width=100,
        height=50)

menu_iniciar.mainloop()  # Executar a janela em loop
