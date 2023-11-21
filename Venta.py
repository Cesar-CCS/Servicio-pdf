class Venta:
    def __init__(self, id_venta, fecha, total_venta, usuario):
        self.id_venta = id_venta
        self.fecha = fecha
        self.total_venta = total_venta
        self.usuario = usuario

    def __str__(self):
        return f"ID: {self.id_venta}, Fecha: {self.fecha}, Total Venta: {self.total_venta}, Usuario: {self.usuario}"