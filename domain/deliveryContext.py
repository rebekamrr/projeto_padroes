class DeliveryContext:
    
    def calcularTaxaDelivery(self, notafiscal, meioEntrega):
        taxa_calculada = meioEntrega.calcula(notafiscal)
        return taxa_calculada