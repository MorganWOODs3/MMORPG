from Peronnage import Personnage

class Guerrier(Personnage):
    def __init__(self, pseudo: str, lvl: int = 1):
        super().__init__(pseudo,lvl)
        self.action = lvl * 8 + 6
        self.pv = lvl * 4 + 6


    def __str__(self):
        return f"Guerrier {super().__str__()}"

    def soin(self, soin:int):
        self.__soin= soin
        self.__pv = self.__lvl * 5 + 3

    def degats(self) -> int:
        return self.lvl * 2 + 2
