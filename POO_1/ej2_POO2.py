class Golondrina:
  def init(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
      if self.energia - (10 + kms) >0:
        self.energia -= 10 + kms
      else:
        print ("no tiene energia suficiente para volar")
   
  def equilibrio(self, energia):
      if self.energia >= 150 and self.energia <= 300:
          print("esta en equilibrio")
      else:
        print("no esta en equilibrio")