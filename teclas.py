import tkinter as tk

# Teclas numéricas


class Botoes():

    def cria_botao(self, janela, texto,
                   largura, altura, x, y, comando):
        tk.Button(
            janela,
            text=texto,
            command=comando
        ).place(x=x,
                y=y,
                width=largura,
                height=altura)

    def cria_label(self, janela, texto):
        tk.Label(janela,
                 text=texto,
                 font="Arial 20",
                 justify=tk.CENTER
                 ).place(x=0,
                         y=0,
                         width=400,
                         height=100)
