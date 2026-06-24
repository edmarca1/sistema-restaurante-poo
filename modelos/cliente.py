class Cliente:
    def __init__(self, id_cliente: int, nombre: str, es_frecuente: bool):
        self.id_cliente: int = id_cliente
        self.nombre: str = nombre
        self.es_frecuente: bool = es_frecuente

    def __str__(self) -> str:
        tipo_cliente = "Frecuente ⭐" if self.es_frecuente else "Regular"
        return f"Cliente [{self.id_cliente}]: {self.nombre} | Tipo: {tipo_cliente}"