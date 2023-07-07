import datetime
import time
import tkinter as tk


def mostrar_relogio():
    agora = datetime.datetime.now()
    hora_formatada = agora.strftime("%H:%M:%S")
    label.configure(text=hora_formatada)
    label.after(1000, mostrar_relogio)


# Cria uma janela
window = tk.Tk()
window.title("Relógio")

# Cria um rótulo para exibir o relógio
label = tk.Label(window, font=("Arial", 80), bg="black", fg="white")
label.pack(padx=20, pady=20)

# Chama a função para atualizar o relógio
mostrar_relogio()

# Inicia o loop principal da janela
window.mainloop()
