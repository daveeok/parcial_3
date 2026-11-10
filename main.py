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
    3. Finalizar""")
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
    else: SystemExit


def mostrarProductos(productos):
    for codigo, (nombre, precio, stock) in productos.items():
        print(f"Código: {codigo}, {nombre}, ${precio}, stock: {stock}")
    volverMenu()

def registrarPorducto(productos, pedido):
    while True:
        codigo = int(input("codigo: "))
        if codigo in productos:
            cantidad = int(input("Cantidad: "))
            nombre, precio, existencias = productos[codigo]
            pedido.append((nombre, precio, cantidad))
            print(pedido)
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

mostrarMenu()