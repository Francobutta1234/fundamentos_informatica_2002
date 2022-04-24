from fundamentos_informatica_2002.POO_1.ej3_POO2 import Ornitologo


class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
        if self.energia - (10 + kms) > 0:
            self.energia -= 10 + kms
        else:
            print("no tiene energia suficiente para volar")    

pepita= Golondrina (100)

print(pepita.comer_alpiste(30))
print(pepita.energia)
print(pepita.volar_en_circulos())
print(pepita.energia)
print(pepita.volar_en_circulos())
print(pepita.volar_en_circulos())
print(pepita.volar_en_circulos())
print(pepita.energia)
print(pepita.volar(180))
print(pepita.energia)