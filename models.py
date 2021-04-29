# 1 - crear clase
class Car:
    # 1.1. Atributos de clase
    num_ruedas = 4
    encendido = False

    # 1.2 Método constructor
    def __init__(self, manufacturer="", model="", color="", cc=0.0, cv=0.0, peso=0.0):
        # Atributos de instancia
        self.manufacturer = manufacturer
        self.model = model
        self.color = color
        self.cc = cc
        self.cv = cv
        self.peso = peso


class Engine:

    def __init__(self, version, cc, cv):
        self.version = version
        self.cc = cc
        self.cv = cv

