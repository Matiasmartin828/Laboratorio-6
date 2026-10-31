#Laboratorio VI - Informática II
#Cálculo de raices, derivadas, sistemas de ecuaciones lineales e integrales con GUI.
#Autores: Ivo Di Marco y Matias Martin
#Repositorio: https://github.com/Matiasmartin828/Laboratorio-6


import math                    

# Los polinomios los guardo como lista de coeficientes de MAYOR a MENOR grado:
COEF_PRUEBA = [0, 1, 0, -8, 0, 82, -25]   
COEF_EJEMPLO = [0, 0, 0, 1, 0, -2, 2]      


def evaluar_polinomio(coef, x):
    resultado = 0.0
    for a in coef:
        resultado = resultado * x + a
    return resultado


def derivar_coeficientes(coef):
    grado = len(coef) - 1
    return [coef[i] * (grado - i) for i in range(grado)]


# ---------- criterio de parada ----------

def es_desde_cifras(n):
      #e_s = (0.5 * 10^(2-n)) %
    return 0.5 * 10 ** (2 - n)


def cifras_desde_es(es):
    n = math.floor(2 - math.log10(es / 0.5) + 1e-9)
    return max(1, min(n, 15))


def error_relativo_porcentual(nuevo, anterior):
    """ea = |(nuevo - anterior) / nuevo| * 100"""
    if nuevo == 0:
        # no se puede dividir por cero, devuelvo infinito para que el método siga iterando
        return math.inf
    return abs((nuevo - anterior) / nuevo) * 100


def formatear_cifras(x, cifras):
    if x == 0 or not math.isfinite(x):
        return str(x)
    decimales = cifras - 1 - math.floor(math.log10(abs(x)))
    if decimales < 0:
        return f"{round(x, decimales):.0f}"
    return f"{x:.{decimales}f}"


# ---------- métodos para hallar raíces ----------

def _resultado(ok, mensaje, raiz=None, iteraciones=0, ea=None, fxr=None):
    return {"ok": ok, "mensaje": mensaje, "raiz": raiz,
            "iteraciones": iteraciones, "ea": ea, "fxr": fxr}


def biseccion(coef, xl, xu, es, max_iter):
    if xl >= xu:
        return _resultado(False, "Intervalo inválido: xl tiene que ser menor que xu.")

    fl = evaluar_polinomio(coef, xl)
    fu = evaluar_polinomio(coef, xu)

    # si alguno de los extremos ya es raíz, devuelvo el resultsado
    if fl == 0:
        return _resultado(True, "ok", xl, 0, 0.0, 0.0)
    if fu == 0:
        return _resultado(True, "ok", xu, 0, 0.0, 0.0)

    # condición clave: f(xl) y f(xu) con distinto signo (producto negativo)
    if fl * fu > 0:
        return _resultado(False, "No hay cambio de signo en [xl, xu]: f(xl) y f(xu) tienen el "
                                 "mismo signo, así que no se puede asegurar una raíz en el intervalo.")

    xr = xl            # lo inicializo para tener un "valor anterior"
    ea = math.inf      # en la primera iteración todavía no hay error aproximado
    for i in range(1, max_iter + 1):
        xr_anterior = xr
        xr = (xl + xu) / 2                 # punto medio
        fxr = evaluar_polinomio(coef, xr)

        if i > 1:                          # recién desde la 2da iteración puedo calcular ea
            ea = error_relativo_porcentual(xr, xr_anterior)

        # me quedo con la mitad del intervalo donde sigue estando el cambio de signo
        test = fl * fxr
        if test < 0:
            xu = xr
        elif test > 0:
            xl = xr
            fl = fxr
        else:
            ea = 0.0                       # f(xr) = 0 justo: raíz exacta

        if ea < es:
            return _resultado(True, "ok", xr, i, ea, fxr)

    return _resultado(False, f"Se llegó al máximo de iteraciones ({max_iter}) sin alcanzar la "
                             f"tolerancia. Última aproximación: x = {xr:.6g}, ea = {ea:.4g} %.")


def newton_raphson(coef, x0, es, max_iter):
    dcoef = derivar_coeficientes(coef)     # coeficientes de f'(x), los calculo una sola vez

    xr = x0
    ea = math.inf
    for i in range(1, max_iter + 1):
        x_anterior = xr
        fx = evaluar_polinomio(coef, x_anterior)
        dfx = evaluar_polinomio(dcoef, x_anterior)

        # si f'(x) = 0 la tangente es horizontal y no corta al eje: no se puede seguir
        if dfx == 0:
            return _resultado(False, f"La derivada es nula en x = {x_anterior:.6g} (iteración {i}), "
                                     "no se puede continuar con Newton-Raphson. Probá con otro x0.")

        xr = x_anterior - fx / dfx
        if not math.isfinite(xr):
            return _resultado(False, "El método divergió (el valor se fue a infinito). Probá con otro x0.")

        fxr = evaluar_polinomio(coef, xr)
        ea = 0.0 if fxr == 0 else error_relativo_porcentual(xr, x_anterior)

        if ea < es:
            return _resultado(True, "ok", xr, i, ea, fxr)

    return _resultado(False, f"Se llegó al máximo de iteraciones ({max_iter}) sin converger. "
                             f"Última aproximación: x = {xr:.6g}, ea = {ea:.4g} %. "
                             "Puede que el método esté oscilando entre valores.")


def secante(coef, x_prev, x0, es, max_iter):
    xa, xb = x_prev, x0                    # xa = x_(i-1), xb = x_i
    fa = evaluar_polinomio(coef, xa)
    fb = evaluar_polinomio(coef, xb)

    xr = xb
    ea = math.inf
    for i in range(1, max_iter + 1):
        denominador = fb - fa
        # si f(xa) = f(xb) la recta secante es horizontal y no hay cruce con el eje x
        if denominador == 0:
            return _resultado(False, f"División por cero: f(x(i-1)) = f(x(i)) en la iteración {i}. "
                                     "Probá con otros valores iniciales.")

        xr = xb - fb * (xb - xa) / denominador
        if not math.isfinite(xr):
            return _resultado(False, "El método divergió.. "
                                     "Probá con otros valores iniciales.")

        fxr = evaluar_polinomio(coef, xr)
        ea = 0.0 if fxr == 0 else error_relativo_porcentual(xr, xb)

        if ea < es:
            return _resultado(True, "ok", xr, i, ea, fxr)

        # corro los puntos: el viejo xb pasa a ser xa, y xr pasa a ser el nuevo xb
        xa, fa = xb, fb
        xb, fb = xr, fxr

    return _resultado(False, f"Se llegó al máximo de iteraciones ({max_iter}) sin converger. "
                             f"Última aproximación: x = {xr:.6g}, ea = {ea:.4g} %.")
