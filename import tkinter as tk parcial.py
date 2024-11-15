# autor: Nelson Alves
# data: 13.11.2024
# código: calculadora de IMC (parcial)


import tkinter as tk
from tkinter import messagebox


def calcular_imc():
    try:
        # Pegando os dados de peso e altura de cada pessoa
        peso1 = float(entry_peso1.get())
        altura1 = float(entry_altura1.get())
        peso2 = float(entry_peso2.get())
        altura2 = float(entry_altura2.get())
        peso3 = float(entry_peso3.get())
        altura3 = float(entry_altura3.get())

        # Calculando os IMCs
        imc1 = peso1 / (altura1 ** 2)
        imc2 = peso2 / (altura2 ** 2)
        imc3 = peso3 / (altura3 ** 2)

        # Classificando os IMCs
        categoria1 = classificar_imc(imc1)
        categoria2 = classificar_imc(imc2)
        categoria3 = classificar_imc(imc3)

        # Atualizando os resultados na interface
        resultado_label.config(text=f"Pessoa 1: IMC = {imc1:.2f} ({categoria1})\n"
                               f"Pessoa 2: IMC = {imc2:.2f} ({categoria2})\n"
                               f"Pessoa 3: IMC = {imc3:.2f} ({categoria3})")
    except ValueError:
        messagebox.showerror("Entrada inválida",
                             "Por favor, insira valores numéricos válidos.")


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora de IMC para Múltiplas Pessoas")
janela.configure(bg='#f0f8ff')  # Fundo azul claro

# Labels e entradas para peso e altura das 3 pessoas
tk.Label(janela, text="Peso Pessoa 1 (kg):", bg='#f0f8ff', fg='#000080',
         font=('Arial', 12)).grid(row=0, column=0, padx=10, pady=10)
entry_peso1 = tk.Entry(janela)
entry_peso1.grid(row=0, column=1, padx=10, pady=10)

tk.Label(janela, text="Altura Pessoa 1 (m):", bg='#f0f8ff', fg='#000080',
         font=('Arial', 12)).grid(row=1, column=0, padx=10, pady=10)
entry_altura1 = tk.Entry(janela)
entry_altura1.grid(row=1, column=1, padx=10, pady=10)

tk.Label(janela, text="Peso Pessoa 2 (kg):", bg='#f0f8ff', fg='#000080',
         font=('Arial', 12)).grid(row=2, column=0, padx=10, pady=10)
entry_peso2 = tk.Entry(janela)
entry_peso2.grid(row=2, column=1, padx=10, pady=10)

tk.Label(janela, text="Altura Pessoa 2 (m):", bg='#f0f8ff', fg='#000080',
         font=('Arial', 12)).grid(row=3, column=0, padx=10, pady=10)
entry_altura2 = tk.Entry(janela)
entry_altura2.grid(row=3, column=1, padx=10, pady=10)

tk.Label(janela, text="Peso Pessoa 3 (kg):", bg='#f0f8ff', fg='#000080',
         font=('Arial', 12)).grid(row=4, column=0, padx=10, pady=10)
entry_peso3 = tk.Entry(janela)
entry_peso3.grid(row=4, column=1, padx=10, pady=10)

tk.Label(janela, text="Altura Pessoa 3 (m):", bg='#f0f8ff', fg='#000080',
         font=('Arial', 12)).grid(row=5, column=0, padx=10, pady=10)
entry_altura3 = tk.Entry(janela)
entry_altura3.grid(row=5, column=1, padx=10, pady=10)

# Botão para calcular os IMCs
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc,
                           bg='#4682b4', fg='#ffffff', font=('Arial', 12, 'bold'))
botao_calcular.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Label para exibir os resultados
resultado_label = tk.Label(
    janela, text="", bg='#f0f8ff', fg='#000080', font=('Arial', 12, 'italic'))
resultado_label.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

# Iniciar o loop principal da janela
janela.mainloop()
