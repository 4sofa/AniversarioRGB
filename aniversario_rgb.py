import tkinter as tk
from tkinter import messagebox
from datetime import date
from PIL import Image, ImageTk
import math


# Função para calcular a diferença de tempo até o próximo aniversário
def calcular_diferenca(hoje, aniversario):
    if aniversario < hoje:
        aniversario = aniversario.replace(year=hoje.year + 1)
    diferenca = aniversario - hoje
    return diferenca.days


# Função que verifica se hoje é o aniversário
def acertar_data():
    try:
        dia = entry_dia.get()
        mes = entry_mes.get()

        if len(dia) > 2 or len(mes) > 2:
            messagebox.showerror("ERRO", "Dia ou mês não podem ter mais de dois dígitos.")
            return

        dia = int(dia)
        mes = int(mes)

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            messagebox.showerror("ERRO", "Por favor insira um dia ou mês válido.")
            return

        hoje = date.today()
        aniversario = date(hoje.year, mes, dia)
        dias = calcular_diferenca(hoje, aniversario)

        if dia == hoje.day and mes == hoje.month:
            message = "Feliz aniversário!!!! Você está de aniversário hoje."
            messagebox.showinfo("Resultado", message)
        else:
            meses = dias // 30
            dias_restantes = dias % 30

            if meses == 0:
                message = ('Hoje não é seu aniversário.\nFaltam {} dias para seu aniversário.'
                           .format(dias_restantes))
                messagebox.showinfo("Resultado", message)
            else:
                message = ('Hoje não é seu aniversário.\nFaltam {} meses e {} dias para seu aniversário.'
                           .format(meses, dias_restantes))
                messagebox.showinfo("Resultado", message)
    except ValueError:
        messagebox.showerror("ERRO", "Por favor insira valores válidos.")


def mudar_cor_fundo():
    global fase

    # Atualiza os valores RGB com base na fase
    r = int((1 + math.sin(fase)) * 127.5)
    g = int((1 + math.sin(fase + 2 * math.pi / 3)) * 127.5)
    b = int((1 + math.sin(fase + 4 * math.pi / 3)) * 127.5)

    # Cria a imagem de fundo com a nova cor
    imagem_fundo = Image.new("RGB", (largura_janela, altura_janela), (r, g, b))
    imagem_fundo_tk = ImageTk.PhotoImage(imagem_fundo)

    # Atualiza a imagem de fundo no Canvas
    canvas.create_image(0, 0, image=imagem_fundo_tk, anchor="nw")
    canvas.image = imagem_fundo_tk  # Necessário para evitar coleta de lixo

    # Incrementa a fase para a próxima cor
    fase += 0.05

    # Chama a função novamente após um intervalo de 100 ms
    root.after(100, mudar_cor_fundo)


# Criação da Janela Principal
root = tk.Tk()
root.title("Você está de aniversário?")

# Define as dimensões da janela
largura_janela = 800
altura_janela = 600

# Inicializa a fase para o ciclo de cores
fase = 0

# Cria um Canvas para exibir a imagem de fundo
canvas = tk.Canvas(root, width=largura_janela, height=altura_janela)
canvas.pack(fill="both", expand=True)

# Criação dos widgets
label_dia = tk.Label(root, text="Insira o dia de nascimento: ", bg="white")
label_dia_window = canvas.create_window(largura_janela//2, altura_janela//3 - 40, window=label_dia)

entry_dia = tk.Entry(root)
entry_dia_window = canvas.create_window(largura_janela//2, altura_janela//3, window=entry_dia)

label_mes = tk.Label(root, text="Insira o mês de nascimento: ", bg="white")
label_mes_window = canvas.create_window(largura_janela//2, altura_janela//3 + 40, window=label_mes)

entry_mes = tk.Entry(root)
entry_mes_window = canvas.create_window(largura_janela//2, altura_janela//3 + 80, window=entry_mes)

button_verificar = tk.Button(root, text='Verificar', command=acertar_data)
button_verificar_window = canvas.create_window(largura_janela//2, altura_janela//3 + 120, window=button_verificar)

# Inicia a função para mudar a cor de fundo dinamicamente
mudar_cor_fundo()

# Define as dimensões da janela principal
root.geometry(f"{largura_janela}x{altura_janela}")

# Inicia o loop principal da interface gráfica
root.mainloop()
