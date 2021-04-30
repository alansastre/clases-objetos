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

class CreditCard: id, titular, numero, fecha expiracion, ccv -- Dani Perez
TODO - class Store: id, name, products, customers, street, country   -  Dani
TODO - class Order: id, customer, shopcart, creation_date  - salasPMJ
TODO - class Category: id, name, color, creation_date  -- Ariel
TODO - Añadir el atributo category a la clase Product y crear objetos y asociarlos  -- Ariel
TODO - Dani Perez - En la clase customer añadir un atributo lista para objetos de la clase CreditCard. Probar a crear objetos y asociarlos
class Offer - id, name, init_date, finish_date, discount - @alansastre
"""
import datetime


# Creación de clases:
class Offer:
    def __init__(self, id, name, init_date, finish_date, discount):
        self.id = id
        self.name = name
        self.init_date = init_date
        self.finish_date = finish_date
        self.creation_date = datetime.datetime.now()
        self.discount = discount

    def __str__(self):
        return f"Offer(id={self.id}, " \
                f"name= {self.name}, " \
                f"init_date= {self.init_date}, " \
                f"finish_date= {self.finish_date}, " \
                f"discount= {self.discount}" \
                f")"

    def __repr__(self):
        return self.__str__()

class ShopCart:

    def __init__(self, id, products, customer):
        self.id = id
        self.product = products
        self.customer = customer
        self.creation_date = datetime.datetime.now()

    def __str__(self):
        return f"ShopCart(id={self.id}, " \
                f"products= {self.product}, " \
                f"customer= {self.customer}, " \
                f"creation_date= {self.creation_date}, " \
                f")"

    def __repr__(self):
        return self.__str__()

        # TODO - @Leticia-Orive


class Dimension:
    def __init__(self, id, height=0.0, width=0.0, weight=0.0, fragile=False):
        self.id = id
        self.height = height
        self.width = width
        self.weight = weight
        self.fragile = fragile

    def __str__(self):
        return f"Dimension(id={self.id}, " \
               f"height= {self.height}, " \
               f"width= {self.width}, " \
               f"weight= {self.weight}, " \
               f"fragile= {self.fragile}" \
               f")"

    def __repr__(self):
        return self.__str__()


# ------------------------------  AROA --------------------------------------------
class Product:

    def __init__(self, id, sku, name, description, color, price, dimension, digital, category, offer):
        self.id = id
        self.sku = sku
        self.name = name
        self.description = description
        self.color = color
        self.price = price
        self.dimension = dimension
        self.digital = digital
        self.category = category
        self.offer = offer

    def __str__(self):
        return f"product(id{self.id}, " \
            f"sku= {self.sku}, " \
            f"name= {self.name}, " \
            f"description= {self.description}, " \
            f"color= {self.color}, " \
            f"price= {self.price}, " \
            f"dimension= {self.dimension}, " \
            f"digital= {self.digital}, " \
            f"category= {self.category}" \
            f"offer= {self.offer}" \
            f")"

    # TODO - Aroita


# TODO - class Category: id, name, color, creation_date  -- Ariel

class Category:
    def __init__(self, id, name, color, creation_date):
        self.id = id
        self.name = name
        self.color = color
        self.creation_date = creation_date

    def __str__(self):
        return f"Category(id={self.id}, " \
               f"name= {self.name}, " \
               f"color= {self.color}, " \
               f"creation_date= {self.creation_date}, " \
               f")"

    def __repr__(self):
        return self.__str__()


# TODO - Aroita  ----------------------------------------------------------------


class Customer:
    def __init__(self, id, first_name, last_name, nif, birth_date, direction, cards):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.nif = nif
        self.birth_date = birth_date
        self.creation_date = datetime.datetime.now()
        self.direction = direction
        self.cards = cards

# TODO - ArielisGT
    def __str__(self):
        """
            Método especial para obtener una representación textual del objeto
        :return:
        """
        return f"Customer(id={self.id}, " \
                   f"first_name= {self.first_name}, " \
                   f"last_name= {self.last_name}, " \
                   f"nif= {self.nif}, " \
                   f"birth_date= {self.birth_date}, " \
                   f"creation_date= {self.creation_date}, " \
                   f"direction= {self.direction}, " \
                   f")"

    def __repr__(self):
        return self.__str__()


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

# Crear Direction y customer y asociarlos - Evaristo
fecha_nacimiento = datetime.date(1970, 12, 1)
direccion_jose = Direction(1, 'luna', 28100, 'Alcobendas', 'España')
cards1 = []
jose = Customer(1, 'Jose', 'Perez', '7777777B', fecha_nacimiento, direccion_jose, cards1)
print(direccion_jose)
print(jose)


# TODO - Crear 3 Dimension y 3 Product y asociarlos

# TODO - Crear lista de productos a partir de los 3 productos anteriores y crear ShopCart con esa lista de productos

class CreditCard:
    def __init__(self, id, titular, number, expiration_date, ccv):
        self.id = id
        self.titular = titular
        self.number = number
        self.expiration_date = expiration_date
        self.ccv = ccv

    def __str__(self):
        return f"CreditCard(id={self.id}, " \
               f"titular= {self.titular}, " \
               f"number= {self.number}, " \
               f"expiration_date= {self.expiration_date}, " \
               f"ccv= {self.ccv}" \
               f")"

    def __repr__(self):
        return self.__str__()


# TODO - Añadir el atributo category a la clase Product y crear objetos y asociarlos  -- Ariel
#     class Category:
#         def __init__(self, id, name, color, creation_date):
#             self.id = id
#             self.name = name
#             self.color = color
#             self.creation_date = creation_date

category_books = Category(1, "Books", "white", datetime.date.today())
category_computers = Category(2, "Computers", "green", datetime.date.today())


visa1 = CreditCard(1, "Carlos López", "0001 0002 0003 4444", datetime.date(2022, 1, 31), 554)
visa2 = CreditCard(2, "Manuel Pérez", "0001 0002 0003 5555", datetime.date(2024, 12, 15), 554)
cards2 = [visa1, visa2]
print("=========Cliente1===============")
cliente1 = Customer(1, "Carlos", "López", "00000002E", datetime.date(1950, 1, 31), "Calle Falsa", [visa1, visa2])
print(cliente1)
