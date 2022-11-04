# POO EXERCICE DE MISE EN SITUATION 4

# ---
class Personne:
    def __init__(self, nom: str, age: int):
        self.nom = nom
        self.age = age

    def SePresenter(self):
        print("Je m'appelle", self.nom, "J'ai ", self.age, "ans")

        print()

# ---
nombre_de_personne = int(input("veuillez entrer le nombre de personne a enregistrer : "))

list_des_personnes = []

for n in range(nombre_de_personne):
    nom = input("Nom de la personne " + str(n+1) + " : ")
    age = int(input("Veuillez entrer l'age de " + nom + " : " ))
    list_des_personnes.append(Personne(nom, age))

def FindPerson():
    nom = input("Veuillez entrer le nom rechercher : " )

    for personne in list_des_personnes:
        if personne.nom == nom:
            personne.SePresenter()

print(FindPerson())