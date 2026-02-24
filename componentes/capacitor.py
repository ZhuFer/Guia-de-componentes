# componentes/capacitor.py

TOLERANCIAS_CAP = {
    "F": "±1%",
    "G": "±2%",
    "J": "±5%",
    "K": "±10%",
    "M": "±20%",
    "Z": "+80%/-20%",
    "Ninguna": ""
}

def calcular_capacitor_codigo(d1, d2, mult, letra_tol):
    """
    Calcula el valor del capacitor basado en el código de 3 dígitos y una letra.
    """
    try:
        # Asegurarnos de que los 3 primeros valores sean enteros
        val1 = int(d1)
        val2 = int(d2)
        ceros = int(mult)
    except ValueError:
        return "Código inválido"

    if letra_tol not in TOLERANCIAS_CAP:
        return "Tolerancia inválida"

    # Calcular el valor en picofaradios (pF)
    valor_pf = (val1 * 10 + val2) * (10 ** ceros)
    
    # Formatear el resultado
    resultado_base = formatear_capacitancia(valor_pf)
    tolerancia_str = TOLERANCIAS_CAP[letra_tol]

    # Unir valor y tolerancia
    if tolerancia_str:
        return f"{resultado_base} {tolerancia_str}"
    return resultado_base

def formatear_capacitancia(pf):
    """
    Convierte picofaradios a nF o µF según el tamaño del valor.
    """
    if pf >= 1000000:
        # Convertir a microfaradios (µF)
        texto = f"{pf / 1000000:.3f}".rstrip('0').rstrip('.')
        return f"{texto} µF"
    elif pf >= 1000:
        # Convertir a nanofaradios (nF)
        texto = f"{pf / 1000:.3f}".rstrip('0').rstrip('.')
        return f"{texto} nF"
    else:
        # Mantener en picofaradios (pF)
        return f"{int(pf)} pF"

# Prueba local
if __name__ == "__main__":
    print(calcular_capacitor_codigo("1", "0", "4", "K")) # Debería imprimir: 100 µF ±10% (Corrección: 0.1 µF) -> Imprimirá 100 nF ±10% o 0.1 µF.
    print(calcular_capacitor_codigo("4", "7", "3", "J")) # Debería imprimir: 47 nF ±5%
    print(calcular_capacitor_codigo("2", "2", "1", "M")) # Debería imprimir: 220 pF ±20%