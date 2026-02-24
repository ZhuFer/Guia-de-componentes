# componentes/inductor.py

VALORES_BANDA_IND = {
    "Negro": 0, "Café": 1, "Rojo": 2, "Naranja": 3, "Amarillo": 4,
    "Verde": 5, "Azul": 6, "Violeta": 7, "Gris": 8, "Blanco": 9
}

MULTIPLICADORES_IND = {
    "Negro": 1, "Café": 10, "Rojo": 100, "Naranja": 1000, "Amarillo": 10000,
    "Verde": 100000, "Azul": 1000000,
    "Dorado": 0.1, "Plateado": 0.01
}

TOLERANCIAS_IND = {
    "Café": "±1%", "Rojo": "±2%", "Naranja": "±3%", "Amarillo": "±4%",
    "Dorado": "±5%", "Plateado": "±10%", "Ninguna": "±20%"
}

def calcular_inductor_4_bandas(color_b1, color_b2, color_mult, color_tol):
    """
    Calcula el valor del inductor en microhenrios (µH) y devuelve un string formateado.
    """
    if color_b1 not in VALORES_BANDA_IND or color_b2 not in VALORES_BANDA_IND:
        return "Color de valor inválido"
    if color_mult not in MULTIPLICADORES_IND:
        return "Color de multiplicador inválido"
    if color_tol not in TOLERANCIAS_IND:
        return "Color de tolerancia inválido"

    v1 = VALORES_BANDA_IND[color_b1]
    v2 = VALORES_BANDA_IND[color_b2]
    mult = MULTIPLICADORES_IND[color_mult]
    tol = TOLERANCIAS_IND[color_tol]

    valor_base = (v1 * 10) + v2
    inductancia_uh = valor_base * mult

    return formatear_henrios(inductancia_uh, tol)

def formatear_henrios(uh, tolerancia):
    """
    Convierte microhenrios a milihenrios o henrios para fácil lectura.
    """
    if uh >= 1000000:
        texto = f"{uh / 1000000:.2f} H"
    elif uh >= 1000:
        texto = f"{uh / 1000:.2f} mH"
    else:
        texto = f"{uh:.2f} µH"
        
    texto = texto.replace(".00", "")
    return f"{texto} {tolerancia}"

# Prueba local
if __name__ == "__main__":
    print(calcular_inductor_4_bandas("Amarillo", "Violeta", "Marrón", "Dorado")) # Debería ser 470 µH ±5%