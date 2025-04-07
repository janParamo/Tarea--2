"""
Ejercicio #5: Procesamiento de pedidos y clientes

Crear una clase Cliente con atributos básicos (por ejemplo, ID, nombre y contacto) y una clase Pedido que contenga información sobre el cliente, 
la lista de productos solicitados y el total de la venta. 
Debe diferenciar entre tipos de clientes (por ejemplo, cliente regular y cliente VIP) 
y aplicar descuentos especiales.

•	[ ] Se ha diseñado una clase Producto con los atributos requeridos.
•	[ ] Se ha implementado una clase Inventario para gestionar la colección de productos.
•	[ ] La clase Inventario incluye métodos para agregar, buscar, actualizar y eliminar productos.
•	[ ] El código sigue los principios de la programación orientada a objetos.

"""

class Cliente:
    def __init__(self, id_cliente, nombre, contacto, tipo_cliente):
        # Inicializa los atributos del cliente
        self.id_cliente = id_cliente  # ID único del cliente
        self.nombre = nombre          # Nombre del cliente
        self.contacto = contacto      # Información de contacto del cliente
        self.tipo_cliente = tipo_cliente  # Tipo de cliente: 'regular' o 'VIP'

    def aplicar_descuento(self, total):
        """Aplica un descuento si el cliente es VIP."""
        if self.tipo_cliente == 'VIP':
            descuento = total * 0.1  # 10% de descuento para clientes VIP
            return total - descuento   # Retorna el total después de aplicar el descuento
        return total  # Retorna el total sin descuento para clientes regulares


class Pedido:
    def __init__(self, cliente, productos):
        # Inicializa los atributos del pedido
        self.cliente = cliente  # Cliente que realiza el pedido
        self.productos = productos  # Lista de productos solicitados (tuplas de nombre y precio)
        self.total = self.calcular_total()  # Calcula el total del pedido

    def calcular_total(self):
        """Calcula el total de la venta aplicando descuentos si corresponde."""
        # Suma los precios de todos los productos
        total = sum(precio for _, precio in self.productos)
        # Aplica el descuento correspondiente al cliente
        total_con_descuento = self.cliente.aplicar_descuento(total)
        return total_con_descuento  # Retorna el total final

    def mostrar_detalles(self):
        """Muestra los detalles del pedido."""
        # Imprime la información del cliente
        print(f"Cliente: {self.cliente.nombre} (ID: {self.cliente.id_cliente})")
        print("Productos solicitados:")
        # Imprime cada producto y su precio
        for producto, precio in self.productos:
            print(f"- {producto}: ${precio:.2f}")
        # Imprime el total a pagar
        print(f"Total a pagar: ${self.total:.2f}")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear clientes
    cliente_regular = Cliente(1, "Juan Pérez", "123456789", "regular")  # Cliente regular
    cliente_vip = Cliente(2, "María López", "987654321", "VIP")  # Cliente VIP

    # Crear pedidos
    productos_cliente_regular = [("Producto A", 100), ("Producto B", 200)]  # Productos del cliente regular
    pedido_regular = Pedido(cliente_regular, productos_cliente_regular)  # Pedido del cliente regular

    productos_cliente_vip = [("Producto C", 150), ("Producto D", 250)]  # Productos del cliente VIP
    pedido_vip = Pedido(cliente_vip, productos_cliente_vip)  # Pedido del cliente VIP

    # Mostrar detalles de los pedidos
    print("Detalles del pedido del cliente regular:")
    pedido_regular.mostrar_detalles()  # Muestra los detalles del pedido regular
    print()  # Línea en blanco para separación
    print("Detalles del pedido del cliente VIP:")
    pedido_vip.mostrar_detalles()  # Muestra los detalles del pedido VIP