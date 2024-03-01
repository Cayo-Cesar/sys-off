import tkinter as tk
from tkinter import ttk, messagebox
import os
import threading
import time

def desligar():
    try:
        tempo = int(entry.get())
        tempo = tempo * 60
        if tempo < 0:
            messagebox.showerror('Erro', 'Digite um número positivo')
            return
        else:
            threading.Thread(target=desligar_pc, args=(tempo,)).start()
            messagebox.showinfo('Sucesso', 'Timer de desligamento iniciado com sucesso!')
    except ValueError:
        messagebox.showerror('Erro', 'Digite um número válido')
        return

def desligar_pc(tempo):
    try:
        time.sleep(tempo)
        os.system('shutdown /s /t 1')
    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao desligar o PC: {e}')

window = tk.Tk()
window.title('Desligar PC')
window.geometry('250x150')

label = ttk.Label(window, text='Tempo para desligar (em minutos):')
label.pack(pady=10)

entry = ttk.Entry(window, width=15, font=('Arial', 12), justify='center')
entry.pack()

button = ttk.Button(window, text='Desligar', command=desligar)
button.pack(pady=10)

window.mainloop()
