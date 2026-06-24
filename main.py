from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_sistema() -> None:
    mi_restaurante = Restaurante("El Buen Sabor")
    producto_1 = Producto("Ceviche Mixto", 15.50, True)
    producto_2 = Producto("Arroz con Pollo", 10.00, True)
    cliente_1 = Cliente(101, "Carlos Mendoza", True)

    mi_restaurante.agregar_producto(producto_1)
    mi_restaurante.agregar_producto(producto_2)
    mi_restaurante.registrar_cliente(cliente_1)

    mi_restaurante.mostrar_menu()
    mi_restaurante.mostrar_clientes()

if __name__ == "__main__":
    ejecutar_sistema()