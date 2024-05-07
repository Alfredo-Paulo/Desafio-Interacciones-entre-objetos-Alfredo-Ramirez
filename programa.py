from tienda import Restaurante, Supermercado, Farmacia
from producto import Producto

def main():
    nombre_tienda = input("Defina el nombre de la tienda: ")
    delivery = float(input("Defina el valor del delivery: "))
    tienda = Supermercado(nombre_tienda, delivery)
    
    while True:
        print(
            """
            ******** M E N U ********
            1) Ingresar Producto
            2) Listar Productos
            3) Realizar Venta
            4) Salir
            *************************
            """
            )

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto: "))
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingreso_productos(producto)
            print("Producto ingresado con éxito.")
        elif opcion == "2":
            print(tienda.listar_productos())
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.venta(nombre_producto, cantidad)
            print("Venta realizada con éxito.")
        elif opcion == "4":
            print("¡Hasta luego!")
            exit(0)
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()