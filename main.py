from datetime import date
from domain import *
from domain.builder.notaFiscalBuilder import CriadorNotaFiscal
from domain.deliveryContext import DeliveryContext
from domain.stategies.bikeStratey import BikeStrategy
from domain.stategies.motocicletaStrategy import MotocicletaStrategy

from domain.item import Item





if __name__ == '__main__':

    context = DeliveryContext()
    bikeStrategy = BikeStrategy()
    motocicletaStrategy = MotocicletaStrategy()

    cardapio = Item()

    itensCardapio = cardapio.listarItens()


    print("************ CARDAPIO *************")
    for item in itensCardapio:
        print(f"{item['item']} ............. R$ {item['valor']:.2f}")

    print()

    cesta = []
    while True:
        
        print("******** ESCOLHA A OPÇÃO DESEJADA **********")
        print(f"Cesta: {cesta}")
        print(" 1 - Inserir item na cesta")
        print(" 2 - Esvaziar cesta")
        print(" 3 - Finalizar Pedido")
        print(" 4 - Sair")


        try:

            escolha = int(input("Escolha: "))

            if escolha == 1:

                print("************ CARDAPIO *************")
                for item in itensCardapio:
                    print(f"{item['item']} ............. R$ {item['valor']:.2f}")

                print()
                print('********* PEDIDO *********')
                
                itemAdd = str(input("Digite o nome do item para adicioná-lo na cesta: "))
                if (cardapio.buscarItem(itemAdd)):
                    itemInserido = cardapio.buscarItem(itemAdd)
                    cesta.append(itemInserido)

                print()
                
            elif escolha == 2:
                print()
                cesta = []
            
            elif escolha == 3:
                print()
                if len(cesta) > 0:
                    # Utilizando o builder
                    nota = CriadorNotaFiscal().com_itens(cesta).com_cnpj('01928391827321').com_razao_social('FHSA Limitada').com_data_de_emissao(date.today()).constroi()

                    escolha_delivery = int(input("Informe o método de entrega [1] - Bicicleta e [2] - Moto: "))

                    # Utilizando o strategy
                    if escolha_delivery == 1:
                        delivery = context.calcularTaxaDelivery(nota, bikeStrategy)
                    else:
                        delivery = context.calcularTaxaDelivery(nota, motocicletaStrategy)
                    print()
                    print()
                    print("******* NOTA FISCAL ********")
                    print(f" Data Emissao: {nota.data_de_emissao}\n Razão Social: {nota.razao_social}\n Subtotal: R$ {nota.valor_total:.2f}\n TOTAL: R$ {delivery:.2f}")
                    print("******* *********** ********")
                    print()
                    print()
                    cesta = []
                else:
                    print("Cesta Vazia")

            elif escolha == 4:
                break
            
        except ValueError as err:
            print("Digite apenas números inteiros")
            