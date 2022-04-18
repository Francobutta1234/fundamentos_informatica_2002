#3
class Notebook:
    def __init__(self,marca,modelo,precio):
        self.marca = marca
        self.modelo= modelo
        self.precio= precio
    def descuento(self,porcentaje):
        descuento1= self.precio *(porcentaje/100)
        print ("el valor es de "+ str(descuento1 + self.precio))

compu1= Notebook("Mac","thinkpad",1000)
compu1.descuento(10)