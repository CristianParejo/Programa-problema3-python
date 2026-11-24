"""
Fase 5 - Evaluación Final POA
Curso: Fundamentos de Programación (213022)
Problema 3: Reabastecimiento de inventario

Herramienta que determina la cantidad exacta a pedir de cada artículo
a partir del stock actual y del stock mínimo requerido.
"""

# ---------------------------------------------------------------
# 1. DATOS INICIALES (R1)
# Matriz con formato: [Código, Nombre, Stock actual, Stock mínimo]
# ---------------------------------------------------------------
inventario = [
    ["A001", "Teclado", 5, 10],
    ["A002", "Mouse", 20, 15],
    ["A003", "Monitor", 3, 8],
    ["A004", "Cable HDMI", 12, 12],
    ["A005", "Memoria USB", 0, 25],
]


# ---------------------------------------------------------------
# 2. MÓDULO / FUNCIÓN (R3 y R4)
# Calcula la cantidad exacta a pedir de un artículo.
# ---------------------------------------------------------------
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


# ---------------------------------------------------------------
# 3. PROGRAMA PRINCIPAL (R2 y R5)
# Recorre la matriz, llama a la función y muestra el informe.
# ---------------------------------------------------------------
print("INFORME DE REABASTECIMIENTO")
print("-" * 40)

for articulo in inventario:
    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

    print(f"{nombre}: pedir {cantidad} unidades")

print("-" * 40)
print("Fin del informe")
