from domain.templateMethod.VeiculoAbstract import VeiculoAbstract


class BikeStrategy(VeiculoAbstract):
    def calcula(self, notafiscal):
        return notafiscal.valor_total + 5.00