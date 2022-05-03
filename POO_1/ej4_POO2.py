class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def combustibleActual(self):
        return self.combustible

    def entran(self, personas):
        return personas <= self.cantidad_maxima()        
    
    def cargar_combustible(self, cantidad):
        self.combustible += cantidad
    
class Moto(MedioDeTransporte):
    def cantidad_maxima(self):
        return 2

    def recorrer(self, kms):
        self.combustible -= kms

class Auto(MedioDeTransporte):
    def cantidad_maxima(self):
        return 5

    def recorrer(self, kms):
        self.combustible -= kms/2   

auto = Auto(100)
moto = Moto(80)
print(auto.entran(3))
print(moto.entran(3))
auto.recorrer(50)
print(auto.combustibleActual())
