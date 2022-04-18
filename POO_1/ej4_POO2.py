class Vehiculo:
    def __init__(self, combustible):
        self.combustible = combustible
    
    def cargar_combustible(self, combustible):
        self.combustible += combustible
    
class Moto(Vehiculo):
    def cantidad_maxima(self):
        self