# POO EXERCICE DE MISE EN SITUATION 1
# genre
#   False : Femme
#   True  : Homme
class Personne:
    def __init__(self, nom: str, age: int, genre: bool):
        self.nom = nom   # crée une variable d'instance : nom
        self.age = age
        self.genre = genre
        print("Constructeur personne " + self.nom)

    def SePresenter(self):
        # Bonjour, je m'appelle Jean, j'ai 30 ans
        # Je suis majeur
        print("Bonjour, je m'appelle " + self.nom + ", j'ai " + str(self.age) + " ans")

        genre_str =  "Masculin" if self.genre else "Feminin"
        print("Genre :", genre_str)

        e_optionnel = ""
        e_optionnel = e_optionnel if self.genre else "e"

        status_str = "Je suis majeur" + e_optionnel if self.EstMajeur() else "Je suis mineur" + e_optionnel
        print(status_str)
        
        print()

    def EstMajeur(self):
        return self.age >= 18

personne1 = Personne("Jean", 25, True)
personne1.SePresenter()

personne2 = Personne("Emilie", 17, False)
personne2.SePresenter()

personne2 = Personne("Michel", 56, True)
personne2.SePresenter()