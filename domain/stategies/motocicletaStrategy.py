from domain.templateMethod.VeiculoAbstract import VeiculoAbstract


class MotocicletaStrategy(VeiculoAbstract):
    def calcula(self, notafiscal):
        return notafiscal.valor_total + 8.00