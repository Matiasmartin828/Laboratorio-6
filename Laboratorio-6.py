# LABORATORIO 6
# AUTORES MATÍAS MARTIN E IVO DI MARCO
# LINK DEL REPOSITORIO DE GITHUB: https://github.com/Matiasmartin828/Laboratorio-6

import tkinter as tk                                                #Librerías
from tkinter import messagebox
import math

def calcular_integral_definida():
    print("Calcular integral definida")

def calcular_sistema():
    matriz_sistema = []
    for i in range(4):
        fila = []
        for j in range(4):
            try:
                valor = float(entradas_sistema[j * 4 + i][0].get())
            except ValueError:
                messagebox.showerror("Error", "Todos los valores de la matriz deben ser numéricos.")
                return
            fila.append(valor)
        matriz_sistema.append(fila)
    vector_b = []
    for i in range(4):
        try:
            valor = float(entradas_sistema[12 + i][1].get())
        except ValueError:
            messagebox.showerror("Error", "Todos los valores del vector b deben ser numéricos.")
            return
        vector_b.append(valor)

    usar_pivoteo = (pivoteo_seleccionado.get() == "Con pivoteo parcial")
    dimension = 4
    for columna in range(dimension - 1):
        if usar_pivoteo:
            fila = columna
            for i in range(columna + 1, dimension):
                if abs(matriz_sistema[i][columna]) > abs(matriz_sistema[fila][columna]):
                    fila = i
            if abs(matriz_sistema[fila][columna]) < 1e-14:
                messagebox.showerror("Error de Sistema", "El sistema es singular o no tiene una solución única.")
                return
            if fila != columna:
                matriz_sistema[columna], matriz_sistema[fila] = matriz_sistema[fila], matriz_sistema[columna]
                vector_b[columna], vector_b[fila] = vector_b[fila], vector_b[columna]
        else:
            if abs(matriz_sistema[columna][columna]) < 1e-14:
                messagebox.showerror("Error de Pivote", 'Se encontró un pivote nulo. Seleccione "Con pivoteo parcial".')
                return
        for k in range(columna + 1, dimension):
            m = matriz_sistema[k][columna] / matriz_sistema[columna][columna]
            for j in range(columna, dimension):
                matriz_sistema[k][j] -= m * matriz_sistema[columna][j]
            vector_b[k] -= m * vector_b[columna]
    if abs(matriz_sistema[dimension - 1][dimension - 1]) < 1e-14:
        messagebox.showerror("Error de Sistema", "El sistema no tiene una solución única (matriz singular).")
        return
    resultado_variables = [0.0] * dimension
    for i in range(dimension - 1, -1, -1):
        suma = sum(matriz_sistema[i][j] * resultado_variables[j] for j in range(i + 1, dimension))
        resultado_variables[i] = (vector_b[i] - suma) / matriz_sistema[i][i]
    for i in range(dimension):
        entradas_resultados_sistema[i].config(state="normal")
        entradas_resultados_sistema[i].delete(0, tk.END)
        entradas_resultados_sistema[i].insert(0, str(round(resultado_variables[i], 8)))
        entradas_resultados_sistema[i].config(state="readonly")

def borrar_valores_sistema():
    for entrada in entradas_sistema:
        entrada[0].delete(0, tk.END)
        entrada[1].delete(0, tk.END)
    for entrada in entradas_resultados_sistema:
        entrada.config(state="normal")
        entrada.delete(0, tk.END)
        entrada.config(state="readonly")

def valores_prueba_sistema():
    borrar_valores_sistema()
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
    try:
        x0 = float(entrada_xcero.get())
        dx = float(entrada_dx.get())
    except ValueError:
        messagebox.showerror("Error", "Los valores de x0 y dx deben ser numéricos.")
        return
    try:
        coeficientes = []
        for entrada in entradas:
            coeficientes.append(float(entrada.get()))
    except ValueError:
        messagebox.showerror("Error", "Todos los coeficientes ingresados al polinomio deben ser numéricos.")
        return

    def funcion_evaluada(valor):
        resultado = 0
        grado = 6
        for coefiente in coeficientes:
            resultado += coefiente * (valor ** grado)
            grado -= 1
        return resultado
    derivada_primera = (funcion_evaluada(x0 + dx) - funcion_evaluada(x0 - dx)) / (2 * dx)
    resultado_derivada_primera.config(state="normal")
    resultado_derivada_primera.delete(0, tk.END)
    resultado_derivada_primera.insert(0, str(round(derivada_primera, 8)))
    resultado_derivada_primera.config(state="readonly")

def calcular_raiz():
    try:
        iteraciones_maximas = int(entrada_max_iter.get())
        if parada_seleccionada.get() == "εs (%):":
            error_relativo = float(entrada_es.get())
            if error_relativo <= 0:
                messagebox.showerror("Error", "El valor de εs debe ser mayor que cero.")
                return
            elif error_relativo >= 100:
                messagebox.showerror("Error", "El valor de εs debe ser menor que 100.")
                return
        else:
            cifras = int(entrada_cifras.get())
            error_relativo = 0.5 * (10 ** (2 - cifras))   
    except ValueError:
        messagebox.showerror("Error", "Los valores de la condición de parada y Máx. iter. deben ser numéricos.")
        return
    
    try:
        coeficientes = []
        for entrada in entradas:
            coeficientes.append(float(entrada.get()))
    except ValueError:
        messagebox.showerror("Error", "Todos los coeficientes ingresados al polinomio deben ser numéricos.")
        return
    
    def funcion_evaluada(valor):
        resultado = 0
        grado = 6
        for coefiente in coeficientes:
            resultado += coefiente * (valor ** grado)
            grado -= 1
        return resultado
    
    def derivada_evaluada(valor):
        resultado = 0
        grado = 6
        for coefiente in coeficientes:
            if grado > 0:
                resultado += coefiente * grado * (valor ** (grado - 1))
            grado -= 1
        return resultado
    
    metodo = metodo_seleccionado.get()
    error_aproximado = 100.0  
    iteraciones = 0       
    punto_medio = 0.0    
    if metodo == "Bisección":
        try:
            xl = float(entrada_xl.get())
            xu = float(entrada_xu.get())
        except ValueError:
            messagebox.showerror("Error", "Los extremos ingresados xl y xu deben ser numéricos.")
            return
        fl = funcion_evaluada(xl)
        fu = funcion_evaluada(xu)
        if fl * fu > 0:
            messagebox.showerror("Error", "f(xl) y f(xu) deben tener signos opuestos. El intervalo no encierra la raíz.")
            return
        punto_medio = xl
        while error_aproximado >= error_relativo and iteraciones < iteraciones_maximas:
            xr_old = punto_medio
            punto_medio = (xl + xu) / 2.0 
            fr = funcion_evaluada(punto_medio)
            iteraciones += 1
            if punto_medio != 0.0:
                error_aproximado = abs((punto_medio - xr_old) / punto_medio) * 100.0  
            if fl * fr < 0.0:
                xu = punto_medio
            elif fl * fr > 0.0:
                xl = punto_medio
                fl = fr
            else:
                error_aproximado = 0.0
                break

    elif metodo == "Newton-Raphson":
        try:
            valor_incial_x0 = float(valor_inicial_x0.get())
        except ValueError:
            messagebox.showerror("Error", "x0 debe ser numérico.")
            return
        x = valor_incial_x0
        while error_aproximado >= error_relativo and iteraciones < iteraciones_maximas:
            x_old = x
            derivada = derivada_evaluada(x)
            if abs(derivada) < 1e-14:
                messagebox.showerror("Error", "Derivada (pendiente) cercana a cero. No se puede continuar con el método de Newton-Raphson.")
                break
            x = x - funcion_evaluada(x) / derivada
            iteraciones += 1
            if x != 0.0:
                error_aproximado = abs((x - x_old) / x) * 100.0 
        punto_medio = x

    elif metodo == "Secante":
        try:
            x_menos1 = float(valor_inicial_x_menos1.get())  
            x0 = float(valor_inicial_x0.get())         
        except ValueError:
            messagebox.showerror("Error", "Los valores iniciales deben ser numéricos.")
            return
        fmenos1 = funcion_evaluada(x_menos1) 
        f0 = funcion_evaluada(x0)   
        x1 = x_menos1 
        x2 = x0  
        x_anterior_2 = x_menos1
        x_anterior_1 = x0
        f_anterior_2 = funcion_evaluada(x_anterior_2)
        f_anterior_1 = funcion_evaluada(x_anterior_1)
        while error_aproximado >= error_relativo and iteraciones < iteraciones_maximas and f_anterior_2 != f_anterior_1:
            x_nuevo = x_anterior_1 - f_anterior_1 * (x_anterior_2 - x_anterior_1) / (f_anterior_2 - f_anterior_1)
            iteraciones += 1
            if x_nuevo != 0.0:
                error_aproximado = abs((x_nuevo - x_anterior_1) / x_nuevo) * 100.0 
            x_anterior_2 = x_anterior_1
            f_anterior_2 = f_anterior_1
            x_anterior_1 = x_nuevo
            f_anterior_1 = funcion_evaluada(x_nuevo)
        punto_medio = x_anterior_1
    var_raiz.set(str(round(punto_medio, 12)))
    var_iter.set(str(iteraciones))
    var_ea.set(str(round(error_aproximado, 12)))
    var_f_raiz.set(str(round(funcion_evaluada(punto_medio), 12)))  

def alternar_condicion_raiz():
    if parada_seleccionada.get() == "εs (%):":
        entrada_es.config(state="normal")
        entrada_cifras.delete(0, tk.END)
        entrada_cifras.config(state="readonly")
    else:
        entrada_es.delete(0, tk.END)
        entrada_es.config(state="readonly")
        entrada_cifras.config(state="normal")

def cambiar_interfaz_raiz():
    metodo = metodo_seleccionado.get()
    if metodo == "Bisección":
        interfaz_biseccion()
    elif metodo == "Newton-Raphson":
        interfaz_newton_raphson()
    elif metodo == "Secante":
        interfaz_secante()

def limpiar_parametros_raiz():
    for elemento in elementos_parametros_raiz:
        elemento.destroy()
    elementos_parametros_raiz.clear()

def interfaz_biseccion():
    global entrada_xl, entrada_xu
    limpiar_parametros_raiz()
    titulo_xl = tk.Label(marco_calculo_raiz, text="xl:", font=("Times New Roman", 9))
    titulo_xl.grid(row=1, column=0, padx=(0, 2), sticky="e")
    entrada_xl = tk.Entry(marco_calculo_raiz, width=8, justify="center")
    entrada_xl.grid(row=1, column=1, padx=(0, 10))
    titulo_xu = tk.Label(marco_calculo_raiz, text="xu:", font=("Times New Roman", 9))
    titulo_xu.grid(row=1, column=2, padx=(0, 2), sticky="e")
    entrada_xu = tk.Entry(marco_calculo_raiz, width=8, justify="center")
    entrada_xu.grid(row=1, column=3, padx=(0, 10))
    elementos_parametros_raiz.extend([titulo_xl, entrada_xl, titulo_xu, entrada_xu])

def interfaz_newton_raphson():
    global valor_inicial_x0
    limpiar_parametros_raiz()
    titulo_x0 = tk.Label(marco_calculo_raiz, text="x0:", font=("Times New Roman", 9))
    titulo_x0.grid(row=1, column=0, padx=(0, 2), sticky="e")
    valor_inicial_x0 = tk.Entry(marco_calculo_raiz, width=8, justify="center")
    valor_inicial_x0.grid(row=1, column=1, padx=(0, 10))
    elementos_parametros_raiz.extend([titulo_x0, valor_inicial_x0])

def interfaz_secante():
    global valor_inicial_x_menos1, valor_inicial_x0
    limpiar_parametros_raiz()
    titulo_x_menos1 = tk.Label(marco_calculo_raiz, text="x(-1):", font=("Times New Roman", 9))
    titulo_x_menos1.grid(row=1, column=0, padx=(0, 2), sticky="e")
    valor_inicial_x_menos1 = tk.Entry(marco_calculo_raiz, width=8, justify="center")
    valor_inicial_x_menos1.grid(row=1, column=1, padx=(0, 10))
    titulo_x0 = tk.Label(marco_calculo_raiz, text="x0:", font=("Times New Roman", 9))
    titulo_x0.grid(row=1, column=2, padx=(0, 2), sticky="e")
    valor_inicial_x0 = tk.Entry(marco_calculo_raiz, width=8, justify="center")
    valor_inicial_x0.grid(row=1, column=3, padx=(0, 10))
    elementos_parametros_raiz.extend([titulo_x_menos1, valor_inicial_x_menos1, titulo_x0, valor_inicial_x0])

def borrar_valores_prueba_polinomio():                                           
    for entrada in entradas:
        entrada.delete(0, tk.END)
    for variable in variables_resultados:
        variable.set("")
    for entrada in [entrada_es, entrada_cifras, entrada_max_iter, entrada_dx, entrada_a, 
                    entrada_b, entrada_cantidad_subintervalos, entrada_xcero]:
                    entrada.delete(0, tk.END)
    resultado_derivada_primera.config(state="normal")
    resultado_derivada_primera.delete(0, tk.END)     
    resultado_derivada_primera.config(state="readonly")
    resultado_integral.config(state="normal")
    resultado_integral.delete(0, tk.END)     
    resultado_integral.config(state="readonly")            
    metodo = metodo_seleccionado.get()
    if metodo == "Bisección":
        entrada_xl.delete(0, tk.END)
        entrada_xu.delete(0, tk.END)
    elif metodo == "Newton-Raphson":
        valor_inicial_x0.delete(0, tk.END)
    elif metodo == "Secante":
        valor_inicial_x_menos1.delete(0, tk.END)
        valor_inicial_x0.delete(0, tk.END)
    
def valores_prueba():
    borrar_valores_prueba_polinomio()
    valores = [0, 1, 0, -8, 0, 82, -25]
    for i in range(7):
        entradas[i].delete(0, tk.END)
        entradas[i].insert(0, str(valores[i]))
    metodo = metodo_seleccionado.get()
    if metodo == "Bisección":
        entrada_xl.delete(0, tk.END)
        entrada_xl.insert(0, "0")
        entrada_xu.delete(0, tk.END)
        entrada_xu.insert(0, "1")
    elif metodo == "Newton-Raphson":
        valor_inicial_x0.delete(0, tk.END)
        valor_inicial_x0.insert(0, "0")
    elif metodo == "Secante":
        valor_inicial_x_menos1.delete(0, tk.END)
        valor_inicial_x_menos1.insert(0, "-1")
        valor_inicial_x0.delete(0, tk.END)
        valor_inicial_x0.insert(0, "0")
    entrada_xcero.delete(0, tk.END)
    entrada_xcero.insert(0, "1")
    entrada_dx.delete(0, tk.END)
    entrada_dx.insert(0, "0.1")
    entrada_a.delete(0, tk.END)
    entrada_a.insert(0, "0")
    entrada_b.delete(0, tk.END)
    entrada_b.insert(0, "2")
    entrada_cantidad_subintervalos.delete(0, tk.END)
    entrada_cantidad_subintervalos.insert(0, "2")

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
boton_borrar = tk.Button(marco_coeficientes, text="Borrar valores", command=borrar_valores_prueba_polinomio, font=("Time new roman", 9), width=15)
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
elementos_parametros_raiz = []
metodos = ["Bisección", "Newton-Raphson", "Secante"]
metodo_seleccionado = tk.StringVar(value=metodos[0]) 
titulo_metodo = tk.Label(marco_calculo_raiz, text="Método:", font=("Times New Roman", 9))
titulo_metodo.grid(row=0, column=0, padx=(0, 5))
for i in range(3):
    boton_metodo = tk.Radiobutton(marco_calculo_raiz, text=metodos[i], variable=metodo_seleccionado, value=metodos[i],font=("Times New Roman", 9), command=cambiar_interfaz_raiz)
    boton_metodo.grid(row=0, column=i+1, padx=(0, 2))
interfaz_biseccion()

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
entradas_resultados_sistema = []
titulos_resultados_sistema = ["x1 =", "x2 =", "x3 =", "x4 ="]
for i in range(0, 4):
    titulo_resultado = tk.Label(marco_entradas_sistema, text=titulos_resultados_sistema[i], font=("Times New Roman", 9))
    titulo_resultado.grid(row=i, column=7, padx=(50, 2), pady=(2, 2))
    resultado_sistema = tk.Entry(marco_entradas_sistema, state="readonly", width=15)
    resultado_sistema.grid(row=i, column=8, padx=(5, 5), pady=(2, 2))
    entradas_resultados_sistema.append(resultado_sistema)

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