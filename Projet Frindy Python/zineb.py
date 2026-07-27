 # Définition de la classe Stagiaire
class Stagiaire:
    def __init__(self, num_inscription, nom_prenom, filiere, niveau):
        self.num_inscription = num_inscription
        self.nom_prenom = nom_prenom
        self.filiere = filiere
        self.niveau = niveau

    def __repr__(self):
        return f"{self.num_inscription} | {self.nom_prenom} | {self.filiere} | {self.niveau}"

# A. Chargement des données des stagiaires
def charger_donnees():
    # Liste des stagiaires pour l'année 2022/2023
    stagiaires_globale = [
        Stagiaire(1001, "Ahmed Zaki", "TSDI", "1ère année"),
        Stagiaire(1002, "Sofia Benali", "TSGE", "2ème année"),
        Stagiaire(1003, "Yassine Ait", "TGI", "1ère année"),
        Stagiaire(1004, "Meryem Lahlou", "OPAD", "2ème année"),
        Stagiaire(1005, "Khalid Hani", "TSDI", "1ère année"),
        Stagiaire(1006, "Laila Fassi", "TGI", "2ème année"),
        Stagiaire(1007, "Omar Tazi", "OPAD", "1ère année"),
        Stagiaire(1008, "Rania Lahrach", "TSGE", "1ère année")
    ]
    return stagiaires_globale

# B. Tri par numéro d'inscription
def trier_par_num_inscription(stagiaires_globale):
    return sorted(stagiaires_globale, key=lambda x: x.num_inscription)

# C. Tri par nom et prénom
def trier_par_nom_prenom(stagiaires_globale):
    return sorted(stagiaires_globale, key=lambda x: x.nom_prenom)

# D. Affichage de l'état global avec un tableau formaté
def afficher_etat_global(stagiaires_globale):
    # Affichage des informations dans le format désiré
    print("Groupe IPIRNET")
    print("    Berrechid")
    print("        LISTE DES STAGIARES GLOBALE")
    print("            Année : 2022/2023")
    print("-" * 50)
    
    # Affichage du tableau
    print("+--------------------+------------------------------+---------------+---------------+")
    print("| Num inscription    | Nom Prenom                   | Filière       | Niveau        |")
    print("+--------------------+------------------------------+---------------+---------------+")
    
    # Affichage de chaque stagiaire dans un format structuré
    for stagiaire in stagiaires_globale:
        print(f"| {stagiaire.num_inscription:<18} | {stagiaire.nom_prenom:<30} | {stagiaire.filiere:<13} | {stagiaire.niveau:<13} |")
    
    print("+--------------------+------------------------------+---------------+---------------+")

# E. Affichage des stagiaires par filière avec un tableau formaté
def afficher_par_filiere(stagiaires_globale):
    filieres = {}
    for stagiaire in stagiaires_globale:
        if stagiaire.filiere not in filieres:
            filieres[stagiaire.filiere] = []
        filieres[stagiaire.filiere].append(stagiaire)

    for filiere, stagiaires_filiere in filieres.items():
        # Affichage des informations dans le format désiré
        print(f"\nGroupe IPIRNET")
        print(f"    Berrechid")
        print(f"        LISTE DES STAGIARES GLOBALE")
        print(f"            Année : 2022/2023")
        print(f"\nFilière : {filiere}")
        print("-" * 50)
        
        # Affichage du tableau
        print("+--------------------+------------------------------+---------------+---------------+")
        print("| Num inscription    | Nom Prenom                   | Niveau        |")
        print("+--------------------+------------------------------+---------------+---------------+")
        
        for stagiaire in stagiaires_filiere:
            print(f"| {stagiaire.num_inscription:<18} | {stagiaire.nom_prenom:<30} | {stagiaire.niveau:<13} |")
        
        print("+--------------------+------------------------------+---------------+---------------+")

# F. Menu
def menu():
    print("\n=== Menu de gestion de l'école IPIRNET ===")
    print("1. Afficher l'état global des stagiaires")
    print("2. Afficher l'état des stagiaires trié par numéro d'inscription")
    print("3. Afficher l'état des stagiaires trié par nom et prénom")
    print("4. Afficher les stagiaires par filière")
    print("5. Quitter")
    return input("\nEntrez votre choix (1-5) : ")

# G. Gérer le menu
def gerer_menu():
    stagiaires_globale = charger_donnees()

    while True:
        choix = menu()

        if choix == "1":
            print("\n=== État global des stagiaires ===")
            afficher_etat_global(stagiaires_globale)
        elif choix == "2":
            print("\n=== État des stagiaires trié par numéro d'inscription ===")
            stagiaires_tries_num = trier_par_num_inscription(stagiaires_globale)
            afficher_etat_global(stagiaires_tries_num)
        elif choix == "3":
            print("\n=== État des stagiaires trié par nom et prénom ===")
            stagiaires_tries_nom = trier_par_nom_prenom(stagiaires_globale)
            afficher_etat_global(stagiaires_tries_nom)
        elif choix == "4":
            print("\n=== Affichage des stagiaires par filière ===")
            afficher_par_filiere(stagiaires_globale)
        elif choix == "5":
            print("\nMerci d'avoir utilisé l'application. À bientôt !")
            break
        else:
            print("\nChoix invalide. Veuillez entrer un numéro entre 1 et 5.")

# H. Exécution
if __name__ == "__main__":
    gerer_menu()
