class Stagiaire:
    def __init__(self, num_inscription, nom, prenom, filiere, niveau, note_prog_th, note_prog_tp, note_logiciel):
        self.num_inscription = num_inscription
        self.nom = nom
        self.prenom = prenom
        self.filiere = filiere
        self.niveau = niveau
        self.note_prog_th = note_prog_th
        self.note_prog_tp = note_prog_tp
        self.note_logiciel = note_logiciel

        # Coefficients
        self.coef_prog_th = 5
        self.coef_prog_tp = 5
        self.coef_logiciel = 3

        # Calcul de la moyenne
        self.moyenne_generale = self.calcul_moyenne_generale()

    def calcul_moyenne_generale(self):
        total_notes = (
            self.note_prog_th * self.coef_prog_th +
            self.note_prog_tp * self.coef_prog_tp +
            self.note_logiciel * self.coef_logiciel
        )
        total_coefs = self.coef_prog_th + self.coef_prog_tp + self.coef_logiciel
        return total_notes / total_coefs

    def afficher_ligne_bulletin(self, module, note, coef):
        note_coef = note * coef
        print(f"| {module:<20} | {note:<7} | {coef:<4} | {note_coef:<10} | {'...':<11} |")

    def afficher_bulletin(self):
        total = (
            self.note_prog_th * self.coef_prog_th +
            self.note_prog_tp * self.coef_prog_tp +
            self.note_logiciel * self.coef_logiciel
        )
        moyenne = self.moyenne_generale
        resultat = "Réussi" if moyenne >= 10 else "Échoué"

        print("\nGroupe IPIRNET")
        print("   Berrechid")
        print("                         BULLETIN DE NOTES")
        print(f"Nom et prénom : {self.nom} {self.prenom:<25}Filière : {self.filiere}")
        print(f"Niveau : {self.niveau:<39}Année : 2022/2023")
        print("|----------------------|---------|------|------------|-------------|")
        print("| Module               | Note    | Coef | Note*Coef  | Observation |")
        print("|----------------------|---------|------|------------|-------------|")

        self.afficher_ligne_bulletin("Programmation TH", self.note_prog_th, self.coef_prog_th)
        self.afficher_ligne_bulletin("Programmation TP", self.note_prog_tp, self.coef_prog_tp)
        self.afficher_ligne_bulletin("Logiciel", self.note_logiciel, self.coef_logiciel)

        print("|----------------------|---------|------|------------|-------------|")

        # Espaces dans la colonne Module
        print(f"| {'':<22} | Total   : {total:<8} |")
        print(f"| {'':<22} | Moyenne : {moyenne:<8.2f} |")
        print(f"| {'':<22} | Résultat: {resultat:<8} |")
        print("=" * 66)


# === Exemple de stagiaire ===

stagiaire = Stagiaire(1002, "Rachid", "El Amrani", "Génie civil", "2ème année", 9.5, 10.0, 11.5)
stagiaire.afficher_bulletin()
