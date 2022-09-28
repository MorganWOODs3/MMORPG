import Peronnage as perso
import Guerrier as guerre
import Mage as magi
import Joueur as lej
import pickle
import string
import json

p = perso.Personnage("Morgan",1)
p1 = perso.Personnage("yop",1)
p2 = perso.Personnage("julien",35)
p3 = perso.Personnage("Comcombre",500)
p4 = perso.Personnage("Morgan",10)
g = guerre.Guerrier("momo",1)
m = magi.Mage("toto",1)
# print("\n")
# print("-----------------Personnage-----------------")
# print("\n")
# print(p)
# print(p1)
# print(p2)
# print(p3)
# print(g)
# print(m)
# print("\n")
# print("-------------attaque--------------")
# print("\n")
# p.attaque(p1)
# if (p.lvl>0):
#     print(f"le personnage {p.pseudo} a vaincu {p1.pseudo}")
# elif (p1.lvl>0):
#     print(f"le personnage {p1.pseudo} a vaincu {p.pseudo}")
# print("\n")
#
# print("---------------différence perso--------")
# print(p,"\n",p4)
# if p4 == p:
#     print("les peronnage sont identiques")
# else:
#     print("les personnage sont différents")
#
# print("\n")
# print("-------------------------combat--------------------")
# print("\n")
#
#
# g.combat(m)
#
#
# if (m.lvl>0):
#     print(f"le personnage {m.pseudo} a vaincu {g.pseudo}")
# elif (g.lvl>0):
#     print(f"le personnage {g.pseudo} a vaincu {m.pseudo}")
#
#
#

print("\n")
print("------------------------list---------------")
j= lej.Joueur('J1')
j.ajout(p1)
j.ajout(p)
j.ajout(p3)
j.ajout(m)
j.ajout(g)

#j.supr(p1)

print([i.pseudo for i in j.get_perso()])
print("\n")
print("------------------------Json---------------")

A = lej.Joueur()
with open('mypicklefile','wb') as f1:
    pickle.dump(A, f1)
with open ('mypicklefile','rb') as f1:
    B = pickle.load(f1)
print(B)

print("\n")

