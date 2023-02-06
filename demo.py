class Automovil:
    def __init__(self,placa):
        self.placa = placa

    def mostrarme_placa(self):
        return self.placa

minibus = Automovil("XYZ-123")
print(minibus.mostrarme_placa())