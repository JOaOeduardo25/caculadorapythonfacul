import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def adicao():
    num1_str = num1.get()
    num2_str = num2.get()

    if not num1_str or not num2_str:
        messagebox.showerror("Erro", "Por favor, insira ambos os números.")
        return

    try:
        num1_value = float(num1_str)
        num2_value = float(num2_str)
        resultado.set(num1_value + num2_value)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def subtracao():
    num1_str = num1.get()
    num2_str = num2.get()

    if not num1_str or not num2_str:
        messagebox.showerror("Erro", "Por favor, insira ambos os números.")
        return

    try:
        num1_value = float(num1_str)
        num2_value = float(num2_str)
        resultado.set(num1_value - num2_value)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def multiplicacao():
    num1_str = num1.get()
    num2_str = num2.get()

    if not num1_str or not num2_str:
        messagebox.showerror("Erro", "Por favor, insira ambos os números.")
        return

    try:
        num1_value = float(num1_str)
        num2_value = float(num2_str)
        resultado.set(num1_value * num2_value)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def divisao():
    num1_str = num1.get()
    num2_str = num2.get()

    if not num1_str or not num2_str:
        messagebox.showerror("Erro", "Por favor, insira ambos os números.")
        return

    try:
        num1_value = float(num1_str)
        num2_value = float(num2_str)
        if num2_value == 0:
            messagebox.showerror("Erro", "Divisão por zero não permitida.")
            return
        resultado.set(num1_value / num2_value)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def resize(event):
    # Ajustar o layout e o dimensionamento dos widgets em resposta às alterações no tamanho da janela
    # Aqui, você pode adicionar lógica para reorganizar os widgets de acordo com o novo tamanho da janela
    pass

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora")
root.geometry("400x300")  # Definir tamanho inicial da janela
root.resizable(True, True)  # Permitir redimensionamento em largura e altura
root.bind("<Configure>", resize)  # Lidar com o evento de redimensionamento da janela

# Variáveis de controle para os campos de entrada e resultado
num1 = tk.StringVar()
num2 = tk.StringVar()
resultado = tk.StringVar()

# Frames para organizar os widgets
frame_num1 = tk.Frame(root)
frame_num1.grid(row=0, column=0, padx=10, pady=10, sticky="w")
frame_num2 = tk.Frame(root)
frame_num2.grid(row=1, column=0, padx=10, pady=10, sticky="w")
frame_botoes = tk.Frame(root)
frame_botoes.grid(row=2, column=0, padx=10, pady=10, sticky="w")
frame_resultado = tk.Frame(root)
frame_resultado.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Entradas de texto para os números
tk.Label(frame_num1, text="Número 1:").pack(side=tk.LEFT)
tk.Entry(frame_num1, textvariable=num1).pack(side=tk.LEFT)

tk.Label(frame_num2, text="Número 2:").pack(side=tk.LEFT)
tk.Entry(frame_num2, textvariable=num2).pack(side=tk.LEFT)

# Botões para as operações
ttk.Button(frame_botoes, text="+", command=adicao).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_botoes, text="-", command=subtracao).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_botoes, text="*", command=multiplicacao).pack(side=tk.LEFT, padx=5)
ttk.Button(frame_botoes, text="/", command=divisao).pack(side=tk.LEFT, padx=5)

# Exibir o resultado
tk.Label(frame_resultado, text="Resultado:").pack(side=tk.LEFT)
tk.Entry(frame_resultado, textvariable=resultado, state="readonly").pack(side=tk.LEFT)

# Iniciar o loop principal da interface gráfica
root.mainloop()
