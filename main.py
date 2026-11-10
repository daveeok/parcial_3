productos ={
    1: ("Café", 3000, 20),
    2: ("Jugo natural", 5000, 15),
    3: ("Sandwich", 8000, 10),
    4: ("Empanada", 2500, 25),
    5: ("Hamburguesa", 12000, 8)

}
pedido = []
codigo = int(input("codigo: "))
cantidad = int(input("Cantidad"))


def mostrarMenu():
    print(f"""
    ======MENU======
    1. Mostrar productos
    2. Agregar producto al pedido
    3. Finalizar""")
    seleccionarOpcion

def seleccionarOpcion():
    opcion = input("\nIngrese una opcion: ")
    if opcion == 1:
        mostrarProductos(productos)
    elif opcion == 2:
        registrarPorducto(productos , pedido , codigo, cantidad)
    else: SystemExit


def mostrarProductos(productos):
    for codigo, (nombre, precio, stock) in productos.items():
        print(f"Código: {codigo}, {nombre}, ${precio}, stock: {stock}")

    

def registrarPorducto(productos , pedido , codigo, cantidad):
    if codigo in productos:
        print("Existe")
    else:
        print("Producto no existente")


mostrarProductos(productos)