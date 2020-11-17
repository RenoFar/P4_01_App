#! /usr/bin/env python3
# coding: utf-8


class Tournoi:  # Définition de la classe Tournoi
    """Classe définissant un tournoi caractérisé par :
    - son nom
    - son lieu
    - sa date
    - son nombre de tour
    - sa liste de tournées
    - sa liste de joueurs
    - son controleur de temps
    - sa descrition"""

    def __init__(self, nom, lieu, date, mode_jeu, nbre_tour=4, description="description"):
        """"Constructeur de la classe"""
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbre_tour = nbre_tour
        self.mode_jeu = mode_jeu
        self.description = description
        self.tournee = []
        self.indices_joueurs = []

    def get_nom(self):
        return self.nom

    def get_lieu(self):
        return self.lieu

    def get_date(self):
        return self.date

    def get_nbre_tour(self):
        return self.nbre_tour

    def get_mode_jeu(self):
        return self.mode_jeu

    def get_description(self):
        return self.description

    def get_tournee(self):
        return self.tournee

    def get_indices_joueur(self):
        return self.indices_joueurs

    def set_tournee(self):
        return

    def set_indices_joueurs(self):
        return

    def set_description(self):
        return

    """tournee = property(set_tournee)
    indices_joueurs = property(set_indices_joueurs)
    description = property(set_description)"""


class Joueur:  # Définition de la classe Joueur
    """Classe définissant un joueur caractérisé par :
    - son nom
    - son prénom
    - sa date de naissance
    - son sexe
    - son classement"""

    def __init__(self, nom, prenom, date_naissance, sexe, indice, classement):
        """"Constructeur de la classe"""
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.indice = indice
        self.classement = classement

    def get_nom(self):
        return self.nom

    def get_prenom(self):
        return self.prenom

    def get_date_naissance(self):
        return self.date_naissance

    def get_sexe(self):
        return self.sexe

    def get_indice(self):
        return self.indice

    def get_classement(self):
        return self.classement

    def set_indice(self):
        return

    def set_classement(self):
        return


class Tour:  # Définition de la classe Tour
    """Classe définissant un tour caractérisé par :
    - son nom
    - son heure de début
    - son heure de fin
    - sa liste de matchs"""

    def __init__(self, nom, debut, fin=""):
        """"Constructeur de la classe"""
        self.nom = nom
        self.debut = debut
        self.fin = fin
        self.liste_matchs = []

    def get_nom(self):
        return self.nom

    def get_debut(self):
        return self.debut

    def get_fin(self):
        return self.fin

    def get_liste_matchs(self):
        return self.liste_matchs

    def set_fin(self):
        return

    def set_liste_matchs(self):
        return

    """nom = property(get_nom)
    debut = property(get_debut)
    fin = property(get_fin, set_fin)
    liste_matchs = property(get_liste_matchs, set_liste_matchs)"""


def creer_tournoi():  # créer le tournoi
    nom = ""
    lieu = ""
    date = ""
    mode_jeu = ""
    while len(nom) < 1 or not nom.isalnum():
        nom = input("\nVeuillez saisir le nom du tournoi: ")
    while len(lieu) < 1:
        lieu = input("Veuillez saisir le Lieu du tournoi: ")
    while len(date) < 1:
        date = input("Date du tournoi: ")
    description = input("Veuillez saisir la Description du tournoi: ")
    while True:
        nbre_tour = input('le nombre de tours par défaut est de 4,\n'
                          '  saisissez un autre nombre ou Entrée pour valider: ')
        if len(nbre_tour) < 1:  # si rien n'est saisi
            nbre_tour = 4
            break
        else:
            try:
                nbre_tour = int(nbre_tour)  # conversion en entier
                if nbre_tour > 0:
                    print('le nombre de tours est modifié à : ' + str(nbre_tour))
                    break
            except ValueError:
                print('\nVeuillez saisir un entier positif!')
    while mode_jeu.lower() not in ('bullet', 'blitz', 'rapide'):
        mode_jeu = input("Veuillez saisir le mode du tournoi (bullet / blitz / rapide): ")
    return Tournoi(nom, lieu, date, mode_jeu, nbre_tour, description)


def selectionner_joueur(liste_joueurs):  # ajouter les joueurs
    choix_joueur = '-1'
    while choix_joueur == '-1':
        listing_joueur = []
        print('\n---------- Liste des joueurs connus: ----------')
        for a, elt in enumerate(liste_joueurs):
            print(str(a) + ' : ' + str(elt))
            listing_joueur.append(str(a))
        choix_menu = ""
        while choix_menu not in ('1', '2'):
            choix_menu = input('\nSelectionner un joueur connu : 1'
                               '\nAjouter un nouveau joueur : 2'
                               '\nVotre choix:')
            if choix_menu == '1':
                while choix_joueur not in listing_joueur:
                    choix_joueur = input('Sélectionner le numéro du joueur : ')
            elif choix_menu == '2':
                choix_joueur = '-2'
    return choix_joueur


def creer_joueur(indice):
    nom = ""
    prenom = ""
    date_naissance = ""
    sexe = ""
    classement = 0
    while len(nom) < 1 or not nom.isalnum():
        nom = input("\nVeuillez saisir le nom du joueur: ")
    while len(prenom) < 1 or not prenom.isalnum():
        prenom = input("Veuillez saisir le prénom du joueur: ")

    date_naissance = input("Veuillez saisir la date de naissance du joueur: ")

    while sexe.lower() not in ('f', 'm'):
        sexe = input("Veuillez saisir le sexe du joueur (F/M): ")
    while True:
        classement = input("Veuillez saisir le classement du joueur: ")
        try:
            classement = int(classement)
            if classement > 0: break
        except ValueError:
            print('\nVeuillez saisir un entier positif!')
    return Joueur(nom, prenom, date_naissance, sexe, indice, classement)


def creer_tour(numero_tour):
    nom = "round " + str(numero_tour + 1)
    debut = "debut"
    fin = " "
    return Tour(nom, debut, fin)


def creer_match(joueurs_selectionnes):
    liste_matchs = []
    list_classement = sorted(joueurs_selectionnes, key=lambda classement: classement[1])
    """print('\n liste joueurs classés: ', *list_classement, '\n')"""
    for m in range(len(list_classement) // 2):
        joueur1 = list_classement[m][0]
        joueur2 = list_classement[((len(list_classement) // 2) + m)][0]
        liste_matchs.append([joueur1, joueur2])
    return liste_matchs


def main():
    """Fonction principale d'exécution de l'application"""


# initialisation des variables
joueurs_connus = [['j1', 'qhh', '12', 'f', '0', 18], ['j2', 'qgth', '14', 'm', '1', 7],
                  ['j3', 'qsfh', '17', 'm', '2', 8], ['j4', 'qdhg', '7', 'm', '3', 48],
                  ['j5', 'qazeah', '36', 'f', '4', 1], ['j6', 'ararh', '16', 'm', '5', 21],
                  ['j7', 'qsfq', '3', 'm', '6', 3], ['j8', 'kjqsg', '28', 'f', '7', 9]]
tournois_existants = [['t1', 'shqshq', '26', 'bullet', 4, 'qsdggq', ['0', '1', '2', '3', '4', '5', '6', '7'], []]]
nouveau_tournoi = creer_tournoi()

# selection des joueurs
"""nouveau_tournoi_indices_joueurs = []"""
for n in range(8):
    print('\n--------- Sélectionner le joueur numéro ' + str(n + 1) + ' ---------')
    joueur_choisi = selectionner_joueur(joueurs_connus)
    if joueur_choisi == '-2':
        joueur_tournoi = creer_joueur(str(len(joueurs_connus)))
        joueurs_connus.append([joueur_tournoi.nom, joueur_tournoi.prenom, joueur_tournoi.date_naissance,
                               joueur_tournoi.sexe, joueur_tournoi.indice, joueur_tournoi.classement])
        joueur_choisi = joueur_tournoi.indice
    nouveau_tournoi.indices_joueurs.append(joueur_choisi)

# réaliser la ronde
tableau_score = {} # initialisation du tableau des scores du tournoi
for t in range(nouveau_tournoi.nbre_tour):
    print('\n---------- Exécution du tour numéro ' + str(t + 1) + ' -----------')
    ronde = creer_tour(t)

    # générer les matchs
    classement_actuel = []
    for c in range(len(nouveau_tournoi.indices_joueurs)):
        if t == 0:  # prendre le classement connu
            tableau_score[nouveau_tournoi.indices_joueurs[c]] = 0
            classement_actuel.append([nouveau_tournoi.indices_joueurs[c],
                                      joueurs_connus[int(nouveau_tournoi.indices_joueurs[c])][5]])
        else: # prendre le score total des tours précédents
            classement_actuel.append([nouveau_tournoi.indices_joueurs[c],
                                      tableau_score[nouveau_tournoi.indices_joueurs[c]]])
    liste_match = creer_match(classement_actuel)

    # saisir les résultats
    for m in range(len(liste_match)):
        score = 0
        print('\nMatch numéro ' + str(m + 1) + ': ' + str(liste_match[m]))
        while score not in ('1', '2', '3'):
            score = input('Choississez le gagnant du match'
                          '\n tapez 1 pour: ' + str(liste_match[m][0]) +
                          '\n tapez 2 pour: ' + str(liste_match[m][1]) +
                          '\n tapez 3 pour: Match nul'
                          '\n votre choix: ')
        if score == '1':
            ronde.liste_matchs.append(([liste_match[m][0], 1], [liste_match[m][1], 0]))
            tableau_score[liste_match[m][0]] += 1
        if score == '2':
            ronde.liste_matchs.append(([liste_match[m][0], 0], [liste_match[m][1], 1]))
            tableau_score[liste_match[m][1]] += 1
        if score == '3':
            ronde.liste_matchs.append(([liste_match[m][0], 1/2], [liste_match[m][1], 1/2]))
            tableau_score[liste_match[m][0]] += 1/2
            tableau_score[liste_match[m][1]] += 1/2
    print(ronde.liste_matchs)

    # finir le tour
    tour_suivant = ""
    while tour_suivant.lower() != 'y':
        tour_suivant = input('\nSouhaitez vous exécuter la ronde suivante? (Y): ')
    ronde.fin = "fin"
    nouveau_tournoi.tournee.append([ronde.nom, ronde.debut, ronde.fin, ronde.liste_matchs])

# sauvegarder le tournoi
print('\n---------- Tournoi sauvegardé -----------\n')
tournois_existants.append([nouveau_tournoi.nom, nouveau_tournoi.lieu, nouveau_tournoi.date,
                           nouveau_tournoi.mode_jeu, nouveau_tournoi.nbre_tour,
                           nouveau_tournoi.description, nouveau_tournoi.indices_joueurs,
                           nouveau_tournoi.tournee])

# mettre à jour le classement
miseajour_classement = ""
while miseajour_classement.lower() != 'y':
    miseajour_classement = input('\nSouhaitez vous mettre à jour le classement? (Y): ')

print('\n---------- tableau des scores du tournoi -----------')
for num, point in tableau_score.items():
    print("le joueur {} obtient le score de {}.".format(num, point))

print('\n---------- Saisissez le nouveau classement -----------')
for numero in tableau_score.keys():
    while True:
        nouveau_classement = input("Veuillez saisir le nouveau classement du joueur numéro " + str(numero) + ": ")
        try:
            nouveau_classement = int(nouveau_classement)
            if nouveau_classement > 0: break
        except ValueError:
            print('\nVeuillez saisir un entier positif!')
    joueurs_connus[tableau_score[numero]][5] = nouveau_classement

# afficher le classement
print('\n---------- Nouveau classement -----------')
classement_trie = sorted(joueurs_connus, key=lambda classement: classement[5])
for tri in classement_trie:
    print('N° {} du classement: joueur {} '.format(str(classement_trie[tri][5]), classement_trie[tri][0])



if __name__ == "__main__":
    main()
