from abc import abstractmethod, ABC


class VeiculoAbstract(ABC):
    @abstractmethod
    def calcula(self, notafiscal):
        pass
