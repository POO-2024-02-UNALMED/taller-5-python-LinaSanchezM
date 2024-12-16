from zooAnimales.animal import Animal

class Ave(Animal):
    listado = []
    halcones = 0
    aguilas = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None, colorPlumas=None):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = colorPlumas
        Ave.listado.append(self)
    
    def movimiento(self):
        return "volar"

    @staticmethod
    def getCantidadAves():
        return len(Ave.listado)

    @staticmethod
    def crearHalcon(nombre, edad, genero):
        Ave.halcones += 1
        Animal._totalAnimales += 1
        return Ave(nombre, edad, "montanas", genero, "cafe glorioso")

    @staticmethod
    def crearAguila(nombre, edad, genero):
        Ave.aguilas += 1
        Animal._totalAnimales += 1
        return Ave(nombre, edad, "montanas", genero, "blanco y amarillo")
    
    def getColorPlumas(self):
        return self._colorPlumas

    def setColorPlumas(self, color_plumas):
        self._colorPlumas = color_plumas