print("Departamendo de confecciones")
print("1. Ingresar producto a fabrica")
print("2. Mostrar inventario en fabrica")
print("0. SALIR")
opcion = 100
listaProductos =[]
while(opcion != 0):
    opcion = int(input("Digita una opción: "))
    if opcion == 1:
        print("Vamos a ingrasar un nuevo producto")
        producto = input("Digita el producto que ingresa a fabricacion:")
        listaProductos.append(producto)
    elif opcion == 2:
        print(f"Mostrando el inventario:  {listaProductos}")
    elif opcion == 0:
        print("GRACIAS")
    else:
        print("opcion invalida")
print("FIN DEL PROGRAMA")