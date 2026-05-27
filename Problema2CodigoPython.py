def calcular_precio_final(nombre_del_producto, categoria_objetivo, precio_umbral):
    #LOGICA DE NEGOCIO PARA CALCULAR PRECIO FINAL

    nombre = nombre_del_producto[0]
    categoria = nombre_del_producto[1]
    precio_base = nombre_del_producto [2]

    if categoria.lower() == categoria_objetivo.lower() and precio_base > precio_umbral: 
       descuento = precio_base * 0.15
       precio_final = precio_base - descuento
    else: precio_final = precio_base
    return precio_final

def generar_informe_menu():
    #INFORMACION MENÚ DEL RESTAURANTE

    MATRIZ_PRODUCTOS = [    
        ["Hamburguesa Premium", "Plato Fuerte", 25000],
        ["Papas Fritas", "Acompañamiento", 8000],
        ["Limonada Cerezada", "Bebidas", 9500],
        ["Corte de Res Tomahawk", "Plato Fuerte", 65000],
        ["Volcán de Chocolate", "Postres", 14000],
        ["Club Colombia", "Bebidas", 7000]]
    
    #DISEÑO TABLA DE PROMOCIÓN
    Promocion = "Plato Fuerte"
    umbral_precio = 20000   

    print("="*65)
    print("     INFORME DE PRECIOS SEGUN PROMOCIÓN - MENÚ RESTAURANTE     ")
    print("="*65)
    print(f"Promoción activa para: {Promocion} con precio > ${umbral_precio:,}")
    print("-"*65)
    print(f"{'Producto':<25} | {'Categoría':<15} | {'P. Base':<9} | {'P. Final':<9}")
    print("-"*65)

    #PRECIO FINAL ORGANIZADO EN COLUMNA
    for producto in MATRIZ_PRODUCTOS:
        precio_f = calcular_precio_final(producto, Promocion, umbral_precio)

        #SALIDAD DE FINAL
        print(f"{producto[0]:<25} | {producto[1]:<15} | ${producto[2]:<8,} | ${int(precio_f):<8,}")
        print("-" * 65)

    #EJECUTAR EL PROGRAMA
if __name__ == "__main__":
    generar_informe_menu()