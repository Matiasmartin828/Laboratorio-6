# LABORATORIO 6
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-6

import tkinter as tk                                                #Librerías
from tkinter import messagebox
import math

def calcular_raiz():
    print("Calcular raíz")



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
ventana.geometry("650x700")
marco_principal = tk.Frame(ventana, padx=10, pady=20)                                       
marco_principal.pack()
titulo = tk.Label(marco_principal,text="Laboratorio VI.1", font=("Time new roman", 16, "bold"))
titulo.grid(row=0, column=0)
subtitulo = tk.Label(marco_principal,text="Cálculo de raíces, derivadas, sistema de ecuaciones e integrales", font=("Time new roman", 9))
subtitulo.grid(row=1, column=0)

marco_coeficientes = tk.Frame(marco_principal)
marco_coeficientes.grid(row=2, column=0, pady=10)
tk.Label(marco_coeficientes,text="Coeficientes\ndel polinomio", justify="left",font=("Time new roman", 9)).grid(row=0, column=0, rowspan=2, padx=(0, 10))
boton_borrar = tk.Button(marco_coeficientes, text="Borrar valores", command=borrar_coeficientes, font=("Time new roman", 9), width=15)
boton_borrar.grid(row=0, column=8, pady=(0, 5), padx=(8, 0))
boton_valores_prueba = tk.Button(marco_coeficientes, text="Valores de prueba", command=valores_prueba, font=("Time new roman", 9), width=15)
boton_valores_prueba.grid(row=1, column=8, pady=(5, 0), padx=(8, 0))
entradas = []
for i in range(7):
    entrada = tk.Entry(marco_coeficientes, width=8, justify="center")
    entrada.grid(row=0, column=i+1, padx=4)
    etiqueta = tk.Label(marco_coeficientes, text="a" + str(6-i), font=("Time new roman", 9))
    etiqueta.grid(row=1, column=i+1)
    entradas.append(entrada)

titulo_raiz = tk.LabelFrame(marco_principal,text="",padx=10,pady=5,width=650)
titulo_raiz.grid(row=3, column=0, sticky="we", pady=(3, 0))
titulo_raiz_nombre = tk.Label(titulo_raiz,text="Cálculo de una raíz", font=("Times New Roman", 12, "bold"))
titulo_raiz_nombre.pack(anchor="w")

marco_calculo_raiz = tk.Frame(marco_principal)
marco_calculo_raiz.grid(row=4, column=0, pady=(5, 10), sticky="we")
metodos = ["Bisección", "Newton-Raphson", "Secante"]
metodo_seleccionado = tk.StringVar(value=metodos[0]) 
titulo_metodo = tk.Label(marco_calculo_raiz, text="Método:", font=("Times New Roman", 9))
titulo_metodo.grid(row=0, column=0, padx=(0, 10))
for i in range(3):
    boton_metodo = tk.Radiobutton(marco_calculo_raiz, text=metodos[i], variable=metodo_seleccionado, value=metodos[i],font=("Times New Roman", 9))
    boton_metodo.grid(row=0, column=i+1, padx=(0, 2))

var_raiz = tk.StringVar()
var_iter = tk.StringVar()
var_ea = tk.StringVar()
var_f_raiz = tk.StringVar()
textos_resultados = ["Raíz:", "Iteraciones:", "εa (%):", "f(raíz):"]
variables_resultados = [var_raiz, var_iter, var_ea, var_f_raiz]
for i in range(4):
    titulo_resultado = tk.Label(marco_calculo_raiz, text=textos_resultados[i])
    titulo_resultado.grid(row=i, column=7, sticky="we", padx=(5, 5), pady=2)
    entry = tk.Entry(marco_calculo_raiz, textvariable=variables_resultados[i], state="readonly", width=15)
    entry.grid(row=i, column=8, sticky="we", pady=2)
boton_calcular_raiz = tk.Button(marco_calculo_raiz, text="Calcular", font=("Times New Roman", 9), width=12, command = calcular_raiz)
boton_calcular_raiz.grid(row=2, column=6, padx=5, pady=2)

marco_calculo_derivada_primera = tk.LabelFrame(marco_principal,text="",padx=10,pady=5,width=650)
marco_calculo_derivada_primera.grid(row=5, column=0, sticky="we", pady=(3, 0))
titulo_calculo_derivada_primera = tk.Label(marco_calculo_derivada_primera,text="Cálculo de la derivada primera (diferencia centrada)", font=("Times New Roman", 12, "bold"))
titulo_calculo_derivada_primera.pack(anchor="w")

ventana.mainloop()              