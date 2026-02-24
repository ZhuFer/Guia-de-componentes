# componentes/resistor.py

# Diccionarios de datos basados en el estándar de colores
VALORES_BANDA = {
    "Negro": 0, "Café": 1, "Rojo": 2, "Naranja": 3, "Amarillo": 4,
    "Verde": 5, "Azul": 6, "Violeta": 7, "Gris": 8, "Blanco": 9
}

MULTIPLICADORES = {
    "Negro": 1, "Café": 10, "Rojo": 100, "Naranja": 1000, "Amarillo": 10000,
    "Verde": 100000, "Azul": 1000000, "Violeta": 10000000,
    "Dorado": 0.1, "Plateado": 0.01
}

TOLERANCIAS = {
    "Café": "±1%", "Rojo": "±2%", "Verde": "±0.5%", 
    "Azul": "±0.25%", "Violeta": "±0.1%", "Dorado": "±5%", "Plateado": "±10%"
}

def calcular_resistencia_4_bandas(color_b1, color_b2, color_mult, color_tol):
    """
    Calcula el valor de la resistencia y devuelve un string formateado.
    """
    # Validaciones de seguridad
    if color_b1 not in VALORES_BANDA or color_b2 not in VALORES_BANDA:
        return "Color de valor inválido"
    if color_mult not in MULTIPLICADORES:
        return "Color de multiplicador inválido"
    if color_tol not in TOLERANCIAS:
        return "Color de tolerancia inválido"

    # Extraer valores numéricos
    v1 = VALORES_BANDA[color_b1]
    v2 = VALORES_BANDA[color_b2]
    mult = MULTIPLICADORES[color_mult]
    tol = TOLERANCIAS[color_tol]

    # Calcular valor base
    valor_base = (v1 * 10) + v2
    resistencia_final = valor_base * mult

    return formatear_ohmios(resistencia_final, tol)

def formatear_ohmios(valor, tolerancia):
    """
    Convierte números grandes en kilo-ohmios o mega-ohmios para fácil lectura.
    """
    if valor >= 1000000:
        texto = f"{valor / 1000000:.2f} MΩ"
    elif valor >= 1000:
        texto = f"{valor / 1000:.2f} kΩ"
    else:
        texto = f"{valor:.2f} Ω"
        
    # Limpiamos decimales innecesarios (ej. 47.00 -> 47)
    texto = texto.replace(".00", "")
    
    return f"{texto} {tolerancia}"

# Pequeña prueba local (se ejecuta solo si corres este archivo directamente)
if __name__ == "__main__":
    print(calcular_resistencia_4_bandas("Amarillo", "Violeta", "Rojo", "Dorado")) 
    # Debería imprimir: 4.70 kΩ ±5%