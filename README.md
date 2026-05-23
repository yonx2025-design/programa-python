# Problema 2: Gestión de Precios y Promociones de Menú

def calcular_precio_final(producto, categoria_objetivo, umbral_precio):
    """
    Módulo encargado de calcular el precio final de un producto individual.
    Aplica 15% de descuento si cumple la categoría y supera el umbral de precio.
    """
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]
    
    # Lógica de negocio establecida por la guía
    if categoria.lower() == categoria_objetivo.lower() and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base
        
    return precio_final

def generar_informe_menu():
    """
    Módulo principal que contiene la matriz de datos y genera la salida en pantalla.
    """
    # Matriz inicial con 6 productos de diversas categorías
    matriz_productos = [
        ["Hamburguesa Premium", "Plato Fuerte", 25000],
        ["Papas Fritas", "Acompañamiento", 8000],
        ["Limonada Cerezada", "Bebidas", 9500],
        ["Corte de Res Tomahawk", "Plato Fuerte", 65000],
        ["Volcán de Chocolate", "Postres", 14000],
        ["Club Colombia", "Bebidas", 7000]
    ]
    
    # Parámetros definidos para la promoción
    categoria_objetivo = "Plato Fuerte"
    umbral_precio = 20000
    
    print("=" * 65)
    print("        INFORME DE CONTROL DE PRECIOS - MENÚ RESTAURANTE        ")
    print("=" * 65)
    print(f"Promoción activa para: {categoria_objetivo} con precio > ${umbral_precio:,}")
    print("-" * 65)
    print(f"{'Producto':<25} | {'Categoría':<15} | {'P. Base':<9} | {'P. Final':<9}")
    print("-" * 65)
    
    # Procesar cada fila de la matriz
    for producto in matriz_productos:
        precio_f = calcular_precio_final(producto, categoria_objetivo, umbral_precio)
        
        # Formatear salida para impresión organizada
        print(f"{producto[0]:<25} | {producto[1]:<15} | ${producto[2]:<8,} | ${int(precio_f):<8,}")
        
    print("=" * 65)
    # Ejecución del programa
if __name__ == "__main__":
    generar_informe_menu()
