class Ornitologo:
    def __init__(self):
        self.aves = []

    def estudiarAve(self, ave):
        self.aves.append(ave)

    def aves_en_estudio(self):
        return self.aves

    def aves_en_equilibrio(self):
        return [self.aves[i].esta_en_equilibrio() for i in range(len(self.aves))]

    def realizar_rutina_sobre_aves(self):
        [self.aves[i].comer(80) for i in range(len(self.aves))]
        [self.aves[i].volar(70) for i in range(len(self.aves))]
        [self.aves[i].comer(10) for i in range(len(self.aves))]

ornitologo = Ornitologo()
ornitologo.estudiarAve("Gorrion")
ornitologo.estudiarAve("Gorrion")
ornitologo.aves_en_estudio()  


        

