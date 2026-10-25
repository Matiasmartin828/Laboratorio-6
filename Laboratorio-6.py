# LABORATORIO 6
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-6

import tkinter as tk                                                #Librerías
from tkinter import messagebox
import math

def calcular_integral_definida():
    print("Calcular integral definida")

def calcular_sistema():
    print("Calcular sistema de ecuaciones")

def borrar_valores_sistema():
    for entrada in entradas_sistema:
        entrada[0].delete(0, tk.END)
        entrada[1].delete(0, tk.END)

def valores_prueba_sistema():
    valores_matriz = [[2, 2, 1, -1, 5], [2, -2, 6, -4, 0], [2, 2, 1, 1, 13], [1, 5, -4, -2, -9]]
    for i in range(4):      
        for j in range(4): 
            indice_x = j * 4 + i
            entradas_sistema[indice_x][0].delete(0, tk.END)
            entradas_sistema[indice_x][0].insert(0, str(valores_matriz[i][j]))
        indice_b = 12 + i
        entradas_sistema[indice_b][1].delete(0, tk.END)
        entradas_sistema[indice_b][1].insert(0, str(valores_matriz[i][4]))

def calcular_derivada_primera():
    print("Calcular derivada primera")

def calcular_raiz():
    print("Calcular raíz")

def alternar_condicion_raiz():
    if parada_seleccionada.get() == "εs (%):":
        entrada_es.config(state="normal")
        entrada_cifras.delete(0, tk.END)
        entrada_cifras.config(state="readonly")
    else:
        entrada_es.delete(0, tk.END)
        entrada_es.config(state="readonly")
        entrada_cifras.config(state="normal")

def metodo_biseccion():
    print("Método de bisección")

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
ventana.geometry("750x700")
marco_principal = tk.Frame(ventana, padx=5, pady=5)                                       
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
titulo_raiz.grid(row=3, column=0, sticky="we", pady=(5, 0))
titulo_raiz_nombre = tk.Label(titulo_raiz,text="Cálculo de una raíz", font=("Times New Roman", 12, "bold"))
titulo_raiz_nombre.pack(anchor="w")

marco_calculo_raiz = tk.Frame(marco_principal)
marco_calculo_raiz.grid(row=4, column=0, pady=(5, 5), sticky="we")
metodos = ["Bisección", "Newton-Raphson", "Secante"]
metodo_seleccionado = tk.StringVar(value=metodos[0]) 
titulo_metodo = tk.Label(marco_calculo_raiz, text="Método:", font=("Times New Roman", 9))
titulo_metodo.grid(row=0, column=0, padx=(0, 5))
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

condiciones_parada = ["εs (%):", "Cifras signif.:"]
parada_seleccionada = tk.StringVar(value=condiciones_parada[0])
boton_error_aproximado_relativo = tk.Radiobutton(marco_calculo_raiz, text=condiciones_parada[0], variable=parada_seleccionada, value=condiciones_parada[0], font=("Times New Roman", 9), command=alternar_condicion_raiz)
boton_error_aproximado_relativo.grid(row=3, column=0, padx=(0, 2), sticky="e")
entrada_es = tk.Entry(marco_calculo_raiz, width=8, justify="center")
entrada_es.grid(row=3, column=1, padx=(0, 10))
boton_cifras_significativas = tk.Radiobutton(marco_calculo_raiz, text=condiciones_parada[1], variable=parada_seleccionada, value=condiciones_parada[1], font=("Times New Roman", 9), command=alternar_condicion_raiz)
boton_cifras_significativas.grid(row=3, column=2, padx=(0, 2), sticky="e")
entrada_cifras = tk.Entry(marco_calculo_raiz, width=8, justify="center")
entrada_cifras.config(state="readonly")
entrada_cifras.grid(row=3, column=3, padx=(0, 5))
titulo_max_iteraciones = tk.Label(marco_calculo_raiz, text="Máx. iter.:", font=("Times New Roman", 9))
titulo_max_iteraciones.grid(row=3, column=4, padx=(0, 2), sticky="e")
entrada_max_iter = tk.Entry(marco_calculo_raiz, width=8, justify="center")
entrada_max_iter.grid(row=3, column=5, padx=(0, 2))

titulo_derivada = tk.LabelFrame(marco_principal, text="", padx=10, pady=5, width=650)
titulo_derivada.grid(row=5, column=0, sticky="we", pady=(5, 0))
titulo_calculo_derivada_primera = tk.Label(titulo_derivada, text="Cálculo de la derivada primera (diferencia centrada)", font=("Times New Roman", 12, "bold"))
titulo_calculo_derivada_primera.pack(anchor="w")
marco_entradas_derivada = tk.Frame(marco_principal)
marco_entradas_derivada.grid(row=6, column=0, sticky="we", pady=(5, 5))
titulo_xcero = tk.Label(marco_entradas_derivada, text="x0:", font=("Times New Roman", 9))
titulo_xcero.grid(row=0, column=0, padx=(0, 2))
entrada_xcero = tk.Entry(marco_entradas_derivada, width=8, justify="center")
entrada_xcero.grid(row=0, column=1, padx=(0, 15))
titulo_dx = tk.Label(marco_entradas_derivada, text="dx:", font=("Times New Roman", 9))
titulo_dx.grid(row=0, column=2, padx=(0, 2))
entrada_dx = tk.Entry(marco_entradas_derivada, width=8, justify="center")
entrada_dx.grid(row=0, column=3, padx=(0, 15))
boton_calcular_derivada_primera = tk.Button(marco_entradas_derivada, text="Calcular", font=("Times New Roman", 9), width=10, command=calcular_derivada_primera)
boton_calcular_derivada_primera.grid(row=0, column=4, padx=(15, 15))
titulo_resultado_derivada_primera = tk.Label(marco_entradas_derivada, text="Derivada f'(x0):", font=("Times New Roman", 9))
titulo_resultado_derivada_primera.grid(row=0, column=5, padx=(5, 5))
resultado_derivada_primera = tk.Entry(marco_entradas_derivada, state="readonly", width=15)
resultado_derivada_primera.grid(row=0, column=6)

titulo_resolucion_sistema = tk.LabelFrame(marco_principal, text="", padx=10, pady=5, width=650)
titulo_resolucion_sistema.grid(row=7, column=0, sticky="we", pady=(5, 0))
titulo_calculo_resolucion_sistema = tk.Label(titulo_resolucion_sistema, text="Resolución de un sistema de 4 ecuaciones (eliminación gaussiana)", font=("Times New Roman", 12, "bold"))
titulo_calculo_resolucion_sistema.pack(anchor="w")
marco_entradas_sistema = tk.Frame(marco_principal)
marco_entradas_sistema.grid(row=8, column=0, sticky="we", pady=(5, 5))
titulos_sistema = ["x1", "x2", "x3", "x4"]
entradas_sistema = []
for i in range(4):
    titulo = tk.Label(marco_entradas_sistema, text=titulos_sistema[i], font=("Times New Roman", 9))
    titulo.grid(row=0, column=i, padx=(5, 5))
    for j in range(4):
        entrada_matriz = tk.Entry(marco_entradas_sistema, width=8, justify="center")
        entrada_matriz.grid(row=j+1, column=i, padx=(5, 5), pady=(2, 2))
        separacion = tk.Label(marco_entradas_sistema, text="|", font=("Times New Roman", 9, "bold"))
        separacion.grid(row=j+1, column=4, padx=(5, 5))
        entrada_resultado = tk.Entry(marco_entradas_sistema, width=8, justify="center")
        entrada_resultado.grid(row=j+1, column=5, padx=(5, 5), pady=(2, 2))
        entradas_sistema.append((entrada_matriz, entrada_resultado))
titulo_resultado_sistema = tk.Label(marco_entradas_sistema, text="b", font=("Times New Roman", 9))
titulo_resultado_sistema.grid(row=0, column=5, padx=(5, 5))
titulos_pivoteos = ["Sin pivoteo", "Con pivoteo parcial"]
pivoteo_seleccionado = tk.StringVar(value=titulos_pivoteos[0])
for i in range(2):
    boton_pivoteo = tk.Radiobutton(marco_entradas_sistema, text=titulos_pivoteos[i], variable=pivoteo_seleccionado, value=titulos_pivoteos[i], font=("Times New Roman", 9))
    boton_pivoteo.grid(row=i, column=6, padx=(10, 2), pady=(2, 0))
boton_calcular_sistema = tk.Button(marco_entradas_sistema, text="Calcular", font=("Times New Roman", 9), width=12, command=calcular_sistema)
boton_calcular_sistema.grid(row=2, column=6, padx=(10, 2), pady=(2, 0))
boton_borrar_sistema = tk.Button(marco_entradas_sistema, text="Borrar valores", font=("Times New Roman", 9), width=12, command=borrar_valores_sistema)
boton_borrar_sistema.grid(row=3, column=6, padx=(10, 2), pady=(2, 0))
boton_valores_prueba_sistema = tk.Button(marco_entradas_sistema, text="Valores de prueba", font=("Times New Roman", 9), width=12, command=valores_prueba_sistema)
boton_valores_prueba_sistema.grid(row=4, column=6, padx=(10, 2), pady=(2, 0))
titulos_resultados_sistema = ["x1 =", "x2 =", "x3 =", "x4 ="]
for i in range(0, 4):
    titulo_resultado = tk.Label(marco_entradas_sistema, text=titulos_resultados_sistema[i], font=("Times New Roman", 9))
    titulo_resultado.grid(row=i, column=7, padx=(50, 2), pady=(2, 2))
    resultado_sistema = tk.Entry(marco_entradas_sistema, state="readonly", width=15)
    resultado_sistema.grid(row=i, column=8, padx=(5, 5), pady=(2, 2))

titulo_calculo_integral_definida = tk.LabelFrame(marco_principal, text="", padx=10, pady=5, width=650)
titulo_calculo_integral_definida.grid(row=9, column=0, sticky="we", pady=(5, 0))
titulo_texto_calculo_integral_definida = tk.Label(titulo_calculo_integral_definida, text="Cálculo de la integral definida (Simpson 1/3 compuesta)", font=("Times New Roman", 12, "bold"))
titulo_texto_calculo_integral_definida.pack(anchor="w")
marco_entradas_integral = tk.Frame(marco_principal)
marco_entradas_integral.grid(row=10, column=0, sticky="we", pady=(5, 5))
titulo_intervalo_integracion = tk.Label(marco_entradas_integral, text="Intervalo de integración:", font=("Times New Roman", 9))
titulo_intervalo_integracion.grid(row=0, column=0, sticky="e", padx=(25, 5))
titulo_a = tk.Label(marco_entradas_integral, text="a:", font=("Times New Roman", 9))
titulo_a.grid(row=0, column=1)
entrada_a = tk.Entry(marco_entradas_integral, width=10, justify="center")
entrada_a.grid(row=0, column=2, padx=(2, 10))
titulo_b = tk.Label(marco_entradas_integral, text="b:", font=("Times New Roman", 9))
titulo_b.grid(row=0, column=3, padx=(10, 2))
entrada_b = tk.Entry(marco_entradas_integral, width=10, justify="center")
entrada_b.grid(row=0, column=4, padx=(2, 10))
titulo_cantidad_subintervalos = tk.Label(marco_entradas_integral, text="Cantidad de subintervalos (par):", font=("Times New Roman", 9))
titulo_cantidad_subintervalos.grid(row=1, column=0, columnspan=2, sticky="e", padx=(0, 5), pady=(5, 0))
entrada_cantidad_subintervalos = tk.Entry(marco_entradas_integral, width=10, justify="center")
entrada_cantidad_subintervalos.grid(row=1, column=2, sticky="w", padx=(2, 10), pady=(5, 0))
boton_calcular_integral = tk.Button(marco_entradas_integral, text="Calcular", font=("Times New Roman", 9), width=10, command=calcular_integral_definida)
boton_calcular_integral.grid(row=0, column=5, padx=(20, 10))
titulo_resultado_integral = tk.Label(marco_entradas_integral, text="Integral definida:", font=("Times New Roman", 9))
titulo_resultado_integral.grid(row=0, column=6, padx=(10, 2))
resultado_integral = tk.Entry(marco_entradas_integral, width=12, state="readonly")
resultado_integral.grid(row=0, column=7, padx=(2, 10))
ventana.mainloop()              