import tkinter as tk
from tkinter import ttk, messagebox
import os
import threading
import time

# Função para iniciar o desligamento do PC após um tempo especificado
def iniciar_desligamento():
    try:
        tempo_minutos = int(tempo_entry.get())
        tempo_segundos = tempo_minutos * 60
        if tempo_segundos < 0:
            messagebox.showerror('Erro', 'Digite um número positivo')
            return
        else:
            threading.Thread(target=desligar_pc, args=(tempo_segundos,)).start()
            messagebox.showinfo('Sucesso', 'Timer de desligamento iniciado com sucesso!')
    except ValueError:
        messagebox.showerror('Erro', 'Digite um número válido')
        return

# Função para desligar o PC
def desligar_pc(tempo):
    try:
        time.sleep(tempo)
        os.system('shutdown /s /t 1')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao desligar o PC: {e}')

# Criação da janela do aplicativo
app_window = tk.Tk()
app_window.title('Desligar PC')
app_window.geometry('250x150')

# Criação dos widgets
tempo_label = ttk.Label(app_window, text='Tempo para desligar (em minutos):')
tempo_label.pack(pady=10)

tempo_entry = ttk.Entry(app_window, width=15, font=('Arial', 12), justify='center')
tempo_entry.pack()

desligar_button = ttk.Button(app_window, text='Desligar', command=iniciar_desligamento)
desligar_button.pack(pady=10)

# Iniciar a aplicação
app_window.mainloop()