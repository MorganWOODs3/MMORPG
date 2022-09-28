from Peronnage import Personnage

class Joueur(Personnage):
    def __init__(self, nom: str, list_perso: list = []):
        self.__nom = nom
        self.__list_perso = list_perso

    def __str__(self):
        return f"{self.__nom} -> Personnage:"+",".join([i for i in self.__list_perso])



    def ajout(self, Personnage):
        if len(self.__list_perso) >= 5:
            print("limite de personnage")
        elif len(self.__list_perso) <= 5:
            self.__list_perso.append(Personnage)

    def supr(self, Personnage):
        return self.__list_perso.remove(Personnage)


    def get_perso(self,recherche = None):
        if type (recherche)==str:
            for i in self.__list_perso:
                if i.pseufo == recherche:
                    return i
        elif type(recherche)==int:
            return self.__list_perso[recherche%len(self.__list_perso)]
        elif type(recherche)==Personnage:
            return "a faire"

        return [i for i in self.__list_perso]


