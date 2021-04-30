"""
Partiendo del principio de que cada clase de esta aplicación tendrá atributos, constructor,
métodos y método string:

a) Crear la clase **ShopCart** que se corresponde con el carrito de la compra para una sesión de compra en una plataforma ecommerce
b) Crear la clase **Product** que se corresponde con un producto en una plataforma ecommerce
c) Crear la clase **Customer** que se corresponde con un cliente en una plataforma ecommerce
d) Crear la clase **Direction** que se corresponde con una dirección de cliente en una plataforma ecommerce

Como orientación, debemos saber que un objeto de la clase **Shopcart** básico va a incluir:
 1) Un identificador de carrito
 2) Una lista de productos
 3) Un cliente asociado
 4) Una fecha de compra, es decir, la fecha en la que se crea el carrito

Asimismo, se puede conocer que un objeto de la clase **Producto** (cuyos atributos no deben ser accesibles directamente):
 1) Un identificador de producto, un número entero
 2) SKU, una cadena de texto que será un identificador único para cada producto
 3) Nombre del producto
 4) Fecha de creación del producto (usaremos el módulo datetime para asignarla)
 5) Precio del producto
 6) Peso del producto

Nota: todos los atributos de la clase Producto estarán encapsulados, 
por lo que crearemos métodos getter y setter, es decir, métodos que 
permitan acceder a sus propiedades y métodos que permitan asignarles un 
nuevo valor.

De la clase **Cliente** necesitaremos:
 1) Un identificador de cliente
 2) Nombre del cliente
 3) Apellidos del cliente
 4) Nif del cliente
 5) Fecha de cumpleaños del cliente
 6) Fecha de registro del cliente
 7) Dirección del cliente (un objeto de la clase Direction)

Por último, los datos de la dirección de un cliente podrían ser (clase Direction):
 1) Un identificador de dirección
 2) Calle
 3) Código Postal
 4) Localidad o ciudad
 5) País

De lo anterior concluimos:
 1) Un carrito tiene asociados una lista de productos y un cliente
 2) Un cliente tiene asociada una dirección

Por ello, se instanciará primero una dirección que deberá posteriomente formar parte de un cliente.
A continuación se instanciarán tres productos, que con la información de
 cliente anterior conformarán una instancia de carrito de compra, la 
cual presentaremos por consola.

Para una correcta visualización a través de la consola implementaremos el método string en cada una de las clases.
"""
import datetime

# Creación de clases:

class ShopCart:

    def __init__(self, id, products, customer):
        self.id = id
        self.product = products
        self.customer = customer
        self.creation_date = datetime.datetime.now()

        # TODO - @Leticia-Orive


class Dimension:
    def __init__(self, id, height=0.0, width=0.0, weight=0.0, fragile=False):
        self.id = id
        self.height = height
        self.width = width
        self.weight = weight
        self.fragile = fragile

        # TODO - DanielPerezRos


class Product:
    def __init__(self, id, sku, name, description, color, price, dimension, digital, peso):
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.color = color
        self.price = price
        self.dimension = dimension
        self.digital = digital
        self.peso = peso     # nuevo

        # TODO - Aroita


class Customer:
    def __init__(self, id, first_name, last_name, nif, birth_date, direction):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nif = nif
        self.birth_date = birth_date
        self.creation_date = datetime.datetime.now()
        self.direction = direction

        # TODO - ArielisGT


class Direction:
    def __init__(self, id, street, postal_code, province, country):
        self.id = id
        self.street = street
        self.postal_code = postal_code
        self.province = province
        self.country = country

    def __str__(self):
        return f'Direction(' \
               f'id={self.id}, ' \
               f'street={self.street}, ' \
               f'postal_code={self.postal_code}, ' \
               f'province={self.province}, ' \
               f'country={self.country})'

    def __repr__(self):
        return self.__str__()


# Asociaciones

# TODO - Crear Direction y customer y asociarlos - Evaristo

# TODO - Crear 3 Dimension y 3 Product y asociarlos

# TODO - Crear lista de productos a partir de los 3 productos anteriores y crear ShopCart con esa lista de productos
