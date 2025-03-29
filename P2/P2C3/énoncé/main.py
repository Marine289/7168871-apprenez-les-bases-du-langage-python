 def salaire_mensuel(salaire_annuel):
...     resultat = salaire_annuel / 12
...     return resultat
def salaire_hebdomadaire(salaire_mensuel):
...     resultat = salaire_mensuel / 4
...     return resultat
def salaire_horaire(salaire_hebdomadaire,heures_travaillees):
...     resultat = salaire_hebdomadaire / heures_travaillees
...     return resultat

