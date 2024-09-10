from Veiculo import Veiculo
class Caminhao(Veiculo):
    def __init__(self, marca, modelo, placa, ano, capacidade):
        super().__init__(marca, modelo, placa, ano)
        self.__capacidade = capacidade
    #Overide - Sobrescrever o método __str__()
    def __str__(self):
        retorner = super().__str__()
        return f'''{retorner}
- Capacidade: {self.__capacidade}'''

# adicione = input()
# adicione = 1
# print(adicione.__str__())