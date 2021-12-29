from datetime import date

class NotaFiscal:
    
    def __init__(self, razao_social, cnpj, itens, data_de_emissao, valor_total, detalhes = ''):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        self.__detalhes = detalhes
        self.__itens = itens
        self.__valorItens = 0.0
        self.__valor_total = valor_total
    
    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return self.__itens

    @property
    def valor_total(self):
        return self.__valor_total
