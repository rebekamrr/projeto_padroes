from datetime import date
from domain.item import Item
from domain.notafiscal import NotaFiscal


class CriadorNotaFiscal:
    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = date.today()
        self.__detalhes = None
        self.__itens = None
        #self.__cliente = None
        self.__valor_total = None


    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def com_cliente(self, cpf):
        self._cliente = cpf
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def constroi(self):
        if self.__razao_social is None:
            raise Exception('Razao social deve ser preenchida')

        if self.__cnpj is None:
            raise Exception('CNPJ deve ser preenchido')

        if self.__itens is None:
            raise Exception('Os itens devem ser preenchidos')

        if self.__data_de_emissao is None:
            self.__data_de_emissao = date.today()

        if self.__detalhes is None:
            self.__detalhes = ''

        if self.__valor_total == None:
            self.__valor_total = 0.0
            for i in self.__itens:
                self.__valor_total = self.__valor_total + i['valor']
            
        
            
        return NotaFiscal(
            razao_social=self.__razao_social,
            cnpj=self.__cnpj,
            itens=self.__itens,
            #cliente=self.__cliente,
            data_de_emissao=self.__data_de_emissao,
            valor_total=self.__valor_total,
            detalhes=self.__detalhes
            
        )
