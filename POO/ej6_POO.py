class Calculadora:
    def __init__(self):
        self
    def cargar(self, valor):
        self.valor = valor

    def sumar(self, valor):
        self.valor += valor

    def restar(self, valor):
        self.valor -= valor

    def multiplicar(self, valor):
        self.valor *= valor

    def valorActual(self):
        print(self.valor)

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()
       

