from modelo.Futbolista import *
equi = Equipo("Manchester United", "Inglaterra")
f = Futbolista("Antonio","Valencia", equi,"lateral",25)
f2 = Futbolista("Alex", "Aguinaga", equi,"mediocentro", 4)
f3 = Futbolista("Felipe", "Caicedo", equi,"delantero",32)

print(f.presentar())
print(f2.presentar())
print(f3.presentar())

