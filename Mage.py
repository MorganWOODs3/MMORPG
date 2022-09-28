from Peronnage import Personnage
class Mage (Personnage):
    def __init__(self, pseudo: str, lvl: int = 1):
        super().__init__(pseudo, lvl)
        self.action = lvl * 8 + 6
        self.pv = lvl * 4 + 6
        self.mana = lvl*5
    def __str__(self):
        return f"Mage {super().__str__()}"

    def soin(self):
        self.__pv = self.__lvl*5+10
        self.mana = self.__lvl *5

    def degats(self)-> int:
        degat = super().degats()
        if self.mana > 4:
            degat += 3
            self.mana -= 4
        return degat


