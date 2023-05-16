from tkinter import *
import random

class JokenpoGUI:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Jokenpo")
        self.janela.geometry("300x200")

        self.lbl_jogador = Label(self.janela, text="Escolha sua jogada:")
        self.lbl_jogador.pack()

        self.btn_pedra = Button(self.janela, text="Pedra", command=self.jogada_pedra)
        self.btn_pedra.pack()

        self.btn_papel = Button(self.janela, text="Papel", command=self.jogada_papel)
        self.btn_papel.pack()

        self.btn_tesoura = Button(self.janela, text="Tesoura", command=self.jogada_tesoura)
        self.btn_tesoura.pack()

        self.lbl_computador = Label(self.janela, text="")
        self.lbl_computador.pack()

        self.lbl_resultado = Label(self.janela, text="")
        self.lbl_resultado.pack()

        self.janela.mainloop()

    def jogada_pedra(self):
        jogada_jogador = "pedra"
        jogada_computador = self.jogada_aleatoria()
        self.lbl_computador.config(text="Computador: " + jogada_computador)
        resultado = self.verificar_jogada(jogada_jogador, jogada_computador)
        self.lbl_resultado.config(text=resultado)

    def jogada_papel(self):
        jogada_jogador = "papel"
        jogada_computador = self.jogada_aleatoria()
        self.lbl_computador.config(text="Computador: " + jogada_computador)
        resultado = self.verificar_jogada(jogada_jogador, jogada_computador)
        self.lbl_resultado.config(text=resultado)

    def jogada_tesoura(self):
        jogada_jogador = "tesoura"
        jogada_computador = self.jogada_aleatoria()
        self.lbl_computador.config(text="Computador: " + jogada_computador)
        resultado = self.verificar_jogada(jogada_jogador, jogada_computador)
        self.lbl_resultado.config(text=resultado)

    def jogada_aleatoria(self):
        jogadas = ["pedra", "papel", "tesoura"]
        return random.choice(jogadas)

    def verificar_jogada(self, jogada_jogador, jogada_computador):
        if jogada_jogador == jogada_computador:
            return "Empate!"
        elif (jogada_jogador == "pedra" and jogada_computador == "tesoura") \
                or (jogada_jogador == "papel" and jogada_computador == "pedra") \
                or (jogada_jogador == "tesoura" and jogada_computador == "papel"):
            return "Jogador venceu!"
        else:
            return "Computador venceu!"

jokenpo = JokenpoGUI()
