# LABORATORIO 6
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-6

import tkinter as tk                                                #Librerías
import math

def borrar_coeficientes():                                           
    for entrada in entradas:
        entrada.delete(0, tk.END)

def valores_prueba():
    valores = [0, 1, 0, -8, 0, 82, -25]
    for i in range(7):
        entradas[i].delete(0, tk.END)
        entradas[i].insert(0, str(valores[i]))

ventana = tk.Tk()                                                  
ventana.title("Laboratorio VI.1 - Cálculo numérico")   
ventana.geometry("700x700")
marco_principal = tk.Frame(ventana, padx=10, pady=20)                                       
marco_principal.pack()
titulo = tk.Label(marco_principal,text="Laboratorio VI.1", font=("Time new roman", 16, "bold"))
titulo.grid(row=0, column=0)
subtitulo = tk.Label(marco_principal,text="Cálculo de raíces, derivadas, sistema de ecuaciones e integrales", font=("Time new roman", 8))
subtitulo.grid(row=1, column=0)
marco_coeficientes = tk.Frame(marco_principal)
marco_coeficientes.grid(row=2, column=0, pady=10)
tk.Label(marco_coeficientes,text="Coeficientes\ndel polinomio", justify="left",font=("Time new roman", 8)).grid(row=0, column=0, rowspan=2, padx=(0, 10))
boton_borrar = tk.Button(marco_coeficientes, text="Borrar valores", command=borrar_coeficientes, font=("Time new roman", 8), width=15)
boton_borrar.grid(row=0, column=8, pady=(0, 5), padx=(8, 0))
boton_valores_prueba = tk.Button(marco_coeficientes, text="Valores de prueba", command=valores_prueba, font=("Time new roman", 8), width=15)
boton_valores_prueba.grid(row=1, column=8, pady=(5, 0), padx=(8, 0))
entradas = []
for i in range(7):
    entrada = tk.Entry(marco_coeficientes, width=8, justify="center")
    entrada.grid(row=0, column=i+1, padx=4)
    etiqueta = tk.Label(marco_coeficientes, text="a" + str(6-i), font=("Time new roman", 8))
    etiqueta.grid(row=1, column=i+1)
    entradas.append(entrada)


ventana.mainloop()              