productos ={
    1: ("Café", 3000, 20),
    2: ("Jugo natural", 5000, 15),
    3: ("Sandwich", 8000, 10),
    4: ("Empanada", 2500, 25),
    5: ("Hamburguesa", 12000, 8)

}
pedido = []

def mostrarMenu():
    print(f"""
    ======MENU======
    1. Mostrar productos
    2. Agregar producto al pedido
    3. Finalizar pedido
    0. Salir""")
    seleccionarOpcion()

def volverMenu():
    volver = input("Presione [Enter] para volver al menu.")
    mostrarMenu()

def seleccionarOpcion():
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        mostrarProductos(productos)
    elif opcion == 2:
        registrarPorducto(productos, pedido)
    elif opcion == 3:
        mostrarResumen(pedido)
    else: 
        print("Saliendo")
        SystemExit


def mostrarProductos(productos):
    for codigo, (nombre, precio, stock) in productos.items():
        print(f"Código: {codigo}, {nombre}, ${precio}, stock: {stock}")
    volverMenu()

def registrarPorducto(productos, pedido):
    while True:
        codigo = int(input("codigo: "))
        if codigo in productos:
            nombre, precio, existencias = productos[codigo]
            cantidad = int(input("Cantidad: "))
            if cantidad <= 0:
                print("Cantidad invalida, intente nuevamente")
            elif cantidad > existencias:
                print("Stock insuficiente, ingrese un valor menor")
            else:
                pedido.append((codigo, nombre, cantidad, precio * cantidad))
                print(f"exito, aregaste {pedido} a tu pedido")
                productos[codigo] = (nombre, precio, existencias - cantidad)
                confirmar = input("¿Agregar otro pedido al prodcuto? s/n ")
                if not "s" in confirmar:
                    mostrarMenu()
                    break
                else: None
        else:
            print("El prodcuto no existe")
            confirmar = input("Producto no existente, ¿intentar de nuevo? s/n ")
            if not "s" in confirmar:
                mostrarMenu()
                break
            else: None

def calcular_total(pedido):
    total = 0
    for codigo, nombre, cantidad, subtotal in pedido:
        total += subtotal
    return total

def mostrarResumen(pedido):
    total = calcular_total(pedido)
    descuento = total * 0.10 if total >= 50000 else 0
    total_final = total - descuento

    print("\n========== RESUMEN DEL PEDIDO ==========")
    print(f"{'Producto':<20}{'Cantidad':<10}{'Subtotal'}")
    print("-" * 41)
    for codigo, nombre, cantidad, subtotal in pedido:
        print(f"{nombre:<20}{cantidad:<10}{subtotal}")
    print("-" * 41)
    print(f"Total : ${total:.0f}")
    print(f"Descuento : ${descuento:.0f}")
    print(f"TOTAL A PAGAR : ${total_final:.0f}")
    print("========================================")

mostrarMenu()