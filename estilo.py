import tkinter as tk
from tkinter import PhotoImage

janela = tk.Tk()


class Estilo():

    global janela

    def define_dimensoes(self, largura, altura, redimencionavel=False):
        # Extraindo a resolução do sistema
        largura_screen = janela.winfo_screenwidth()
        altura_screen = janela.winfo_screenheight()

        # # Definindo posição da janela
        posx = int(largura_screen / 2 - largura / 2)
        posy = int(altura_screen / 2 - altura / 2)
        # Calculo para sempre centralizar a tela

        janela.geometry(
            f"{largura}x{altura}+{posx}+{posy}"
        )  # Definindo tamanho e posicionamento ("WxH+X+Y")

        # Definindo se é redimensionável ou não
        janela.resizable(redimencionavel, redimencionavel)
        # root.minsize(300, 300)  # Definindo a dimensão mínima
        # root.maxsize(300, 300)  # Deinindo a dimensão máxima
        # root.state(
        #     "iconic"
        # )  # Definindo como a janela deve iniciar, se é em tela cheia ou
        # modo normal
        """
        Com withdrawn o app não abriu
        e com zoomed deu erro
        """

    def define_titulo(self, titulo):
        janela.title(titulo)  # Nomenado título da janela

    def define_icon(self, arquivo):
        # root.iconbitmap("icon.png")
        # Estava dando erro em definir a o icóne desse jeito
        janela.iconphoto(True, PhotoImage(file=arquivo))  # Definindo o ícone
        """
        Teve que ser assim, pois foi o jeito que deu certo e não funcionou com
        o
        arquivo .ico
        """

    def executa_janela(self):
        janela.mainloop()
