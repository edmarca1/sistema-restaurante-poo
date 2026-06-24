from modelos.producto import Producto
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante: str = nombre_restaurante
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.lista_productos.append(producto)

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def mostrar_menu(self) -> None:
        print(f"\n--- MENÚ DE {self.nombre_restaurante.upper()} ---")
        for prod in self.lista_productos:
            print(prod)

    def mostrar_clientes(self) -> None:
        print(f"\n--- CLIENTES REGISTRADOS ---")
        for cli in self.lista_clientes:
            print(cli)