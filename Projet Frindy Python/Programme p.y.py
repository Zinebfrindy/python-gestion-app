# Liste pour stocker les stagiaires
stagiaires = []

# Fonction pour afficher les stagiaires
def afficher_stagiaires():
    print("\nListe des stagiaires:")
    for stagiaire in stagiaires:
        print(stagiaire)

# Fonction pour ajouter un stagiaire
def ajouter_stagiaire(num_inscription, nom, prenom, niveau, filiere):
    # Vérification si le stagiaire existe déjà
    for stagiaire in stagiaires:
        if stagiaire['num_inscription'] == num_inscription:
            print(f"Le stagiaire avec le numéro {num_inscription} existe déjà.")
            return
    # Ajout du stagiaire
    stagiaires.append({
        'num_inscription': num_inscription,
        'nom': nom,
        'prenom': prenom,
        'niveau': niveau,
        'filiere': filiere
    })
    afficher_stagiaires()

# Fonction pour rechercher un stagiaire par numéro d'inscription
def rechercher_stagiaire(num_inscription_partiel):
    print(f"\nRecherche des stagiaires pour le numéro d'inscription partiel: {num_inscription_partiel}")
    found = False
    for stagiaire in stagiaires:
        if num_inscription_partiel in stagiaire['num_inscription']:
            print(stagiaire)
            found = True
    if not found:
        print("Aucun stagiaire trouvé.")

# Fonction pour modifier un stagiaire
def modifier_stagiaire(num_inscription, nom=None, prenom=None, niveau=None, filiere=None):
    for stagiaire in stagiaires:
        if stagiaire['num_inscription'] == num_inscription:
            if nom:
                stagiaire['nom'] = nom
            if prenom:
                stagiaire['prenom'] = prenom
            if niveau:
                stagiaire['niveau'] = niveau
            if filiere:
                stagiaire['filiere'] = filiere
            print(f"\nStagiaire {num_inscription} modifié:")
            afficher_stagiaires()
            return
    print(f"Stagiaire avec le numéro {num_inscription} non trouvé.")

# Fonction pour supprimer un stagiaire
def supprimer_stagiaire(num_inscription):
    global stagiaires
    stagiaires = [stagiaire for stagiaire in stagiaires if stagiaire['num_inscription'] != num_inscription]
    print(f"\nStagiaire avec le numéro {num_inscription} supprimé.")
    afficher_stagiaires()

# Test des fonctions avec des noms marocains
ajouter_stagiaire("12345", "Boulahbib", "Mouad", "L3", "Informatique")
ajouter_stagiaire("67890", "El Amrani", "Rachid", "M1", "Génie civil")
rechercher_stagiaire("123")
modifier_stagiaire("12345", nom="El Yassir", prenom="Siham")
supprimer_stagiaire("67890")
