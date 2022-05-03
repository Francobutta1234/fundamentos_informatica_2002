class Gorrion:
    def __init__(self):
        self.gramosActuales = 0
        self.kmsActuales = 0
        self.listaGramos = []
        self.listaKms = []

    def comer(self, gramos):
        self.listaGramos.append(gramos)
        self.gramosActuales += gramos

    def volar(self, kms):
        self.listaKms.append(kms)
        self.listaKms += kms

    def css(self):
        if self.gramosActuales > 0:
            self.kmsActuales / self.gramosActuales
        else:
            return None

    def cssp(self):
        return max(self.listaKms) / max(self.listaGramos)

    def cssv(self):
        return len(self.listaKms) / len(self.listaGramos)

    def esta_en_equilibrio(self):
        return 0.5 <= self.css() <= 2
   
                        
