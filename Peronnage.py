import json

class Personnage:
    def __init__(self,pseudo:str,lvl:int=1):
        self.__pseudo = pseudo
        self.__lvl = lvl
        self.__pv = lvl
        self.__action = lvl

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.__pseudo, self.__lvl, self.__pv,self.__action)

    def __str__(self):
        return f"{self.__pseudo} de niveau {self.__lvl}, avec {self.__pv} point de vie et {self.__action} point d'inisiative."

    def __eq__(self, other):
        return self.pseudo == other.pseudo

    def degats(self):
        return self.lvl

    def attaque(self,opposant):
        print(f"{self.__pseudo}:{self.__pv}pv |attaque| {opposant.__pseudo}: {opposant.__pv}pv ")
        if self.__action > opposant.__action:
            opposant.__pv -= self.degats()
            if opposant.__pv > 0:
                self.__pv -= opposant.degats()
        elif opposant.__action > self.__action:
            self.__pv -= opposant.degats()
            if self.__pv > 0:
                opposant.__pv -= self.degats()
        else:
            opposant.__pv -= self.degats()
            self.__pv -= opposant.degats()




    def combat(self,opposant):
        while (self.__pv>0 and opposant.__pv>0):
            self.attaque(opposant)


    def soin(self, soin:int):
        self.__soin = soin
        self.__pv = self.__soin




    @property
    def pv(self):
        self.__pv = self.__lvl
    @property
    def pv(self)-> int:
        return self.__pv
    @pv.setter
    def pv(self, pv):
        if pv > 0 :
            self.__pv = pv
    @property
    def action(self) -> int:
        return self.__action
    @action.setter
    def action(self, action):
        if action > 0 :
            self.__action = action
    @property
    def pseudo(self):
        return self.__pseudo
    @pseudo.setter
    def pseudo(self,ps):
        self.__pseudo = ps
    @property
    def lvl(self)-> int:
        return self.__lvl
    @lvl.setter
    def lvl(self, lvl):
        if lvl > 0:
            self.__lvl = lvl

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)