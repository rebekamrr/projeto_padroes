import json

class Item:
    def __init__(self):
        self.__descricao = ''
        self.__valor = 0.0

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

    def listarItens(self):
        with open('./data/itens.json', 'r') as file:

            cardapio = json.load(file)
        return cardapio

    def buscarItem(self, item):
        cardapio = self.listarItens()
        for itemCardapio in cardapio:
            if itemCardapio['item'] == item:
                return itemCardapio
        return False

    