class Contador:
    def __init__(self, valor):
        self.valor = valor
        self.ultimo = ""

    def inc(self):
        self.valor += 1
        self.ultimo = "Incremento"
    def dis(self):
        self.valor -= 1
        self.ultimo = "Disminucion"
    def reset(self):
        self.valor = 0
        self.ultimo = "Reset"
    def valorActual(self):
        print(self.valor)
        self.ultimo = "Actualizacion"
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
        self.ultimo = "Actualizacion"
    def ultimoComando(self):
        print(self.ultimo)


contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.ultimoComando()
contador.valorActual()
contador.ultimoComando()