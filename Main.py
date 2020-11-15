#! /usr/bin/env python3
# coding: utf-8

import Package.fonctions


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

    def __init__(self, nom, lieu, date, mode_jeu, nbre_tour=4, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbre_tour = nbre_tour
        self.mode_jeu = mode_jeu
        self.description = description
        self.tournee = []
        self.indices_joueurs = []


class Joueur:  # Définition de la classe Joueur
    """Classe définissant un joueur caractérisé par :
    - son nom
    - son prénom
    - sa date de naissance
    - son sexe
    - son classement"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement=0):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement


class Tour:  # Définition de la classe Tour
    """Classe définissant un tour caractérisé par :
    - son nom
    - son heure de début
    - son heure de fin
    - sa liste de matchs"""

    def __init__(self, nom, debut, fin, liste_matchs):
        self.nom = nom
        self.debut = debut
        self.fin = fin
        self.liste_matchs = liste_matchs


def creer_tournoi():  # créer le tournoi
    nom = ""
    lieu = ""
    date = ""
    mode_jeu = ""
    description = ""
    while len(nom) < 1 or not nom.isalnum():
        nom = input("\nVeuillez saisir le nom du tournoi: ")
    while len(lieu) < 1:
        lieu = input("Veuillez saisir le Lieu du tournoi: ")
    while len(date) < 1:
        date = input("Date du tournoi: ")
    while len(description) < 1:
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


def creer_joueur():
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
    return Joueur(nom, prenom, date_naissance, sexe, classement)


def creer_tour(joueurs_selectionnes, numero_tour):
    debut = "debut"
    fin = " "
    liste_matchs = []
    if numero_tour == 0:
        nom = "round " + str(numero_tour + 1)
        list_classement = sorted(joueurs_selectionnes, key=lambda classement: classement[4])
        """print('\n liste joueurs classés: ', *list_classement, '\n')"""
        for m in range(len(list_classement)//2):
            joueur1 = list_classement[m][0]
            joueur2 = list_classement[((len(list_classement)//2)+m)][0]
            liste_matchs.append([joueur1, joueur2])
    else:
        nom = "round " + str(numero_tour + 1)
    return Tour(nom, debut, fin, liste_matchs)


def ajouter_joueur(liste_joueurs):  # ajouter les joueurs
    choix_joueur = -1
    while choix_joueur == -1:
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
                nouveau_joueur = creer_joueur()
                liste_joueurs.append([nouveau_joueur.nom, nouveau_joueur.prenom, nouveau_joueur.date_naissance,
                                      nouveau_joueur.sexe, nouveau_joueur.classement])
    return [choix_joueur, liste_joueurs]


def selectionner_tournoi(liste_tournoi):
    listing_tournoi = []
    print('\n---------- Liste des tournois enregistrés: ----------')
    for a, elt in enumerate(liste_tournoi):
        print(str(a) + ' : ' + str(elt))
        listing_tournoi.append(str(a))
    choix_tournoi = ""
    while choix_tournoi not in listing_tournoi:
        choix_tournoi = input('Sélectionner le numéro du tournoi : ')
    return [liste_tournoi[int(choix_tournoi)], choix_tournoi]


def main():
    """Fonction principale d'exécution de l'application"""
    joueurs_connus = [['j1', 'qhh', '12', 'f', 18], ['j2', 'qgth', '14', 'm', 7], ['j3', 'qsfh', '17', 'm', 8],
                      ['j4', 'qdhg', '7', 'm', 48], ['j5', 'qazeah', '36', 'f', 1], ['j6', 'ararh', '16', 'm', 21],
                      ['j7', 'qsfq', '3', 'm', 3], ['j8', 'kjqsg', '28', 'f', 9]]
    tournois_existants = [['t1', 'shqshq', '26', 'bullet', 4, 'qsdggq', ['0', '1', '2', '3', '4', '5', '6', '7'], []]]
    while True:
        choix = ""
        while choix not in ('1', '2', '3', '4'):
            choix = input('\n---------- Menu principal -----------'
                          '\nCréer un tournoi : 1'
                          '\nExécuter un tournoi: 2'
                          '\nVoir les rapports : 3'
                          '\nFermer l\'application : 4'
                          '\nSaisissez le Numéro de votre choix: ')
        if choix == '1':
            nouveau_tournoi = creer_tournoi()
            for n in range(7):
                print('\n--------- Selectionner le joueur numéro ' + str(n + 1) + ' ---------')
                joueurs_tournoi = ajouter_joueur(joueurs_connus)
                joueurs_connus = joueurs_tournoi[1]
                nouveau_tournoi.indices_joueurs.append(joueurs_tournoi[0])
            tournois_existants.append([nouveau_tournoi.nom, nouveau_tournoi.lieu, nouveau_tournoi.date,
                                       nouveau_tournoi.mode_jeu, nouveau_tournoi.nbre_tour,
                                       nouveau_tournoi.description, nouveau_tournoi.indices_joueurs,
                                       nouveau_tournoi.tournee])
        elif choix == '2':
            tournoi_selectionne = selectionner_tournoi(tournois_existants)
            print('\ntournoi selectionné: ', tournoi_selectionne[0])

            selection_joueurs = []
            for p in range(len(tournoi_selectionne[0][6])):
                selection_joueurs.append(joueurs_connus[int(tournoi_selectionne[0][6][p])])
            print('liste des joueurs selectionnés: ', selection_joueurs)

            for t in range(tournoi_selectionne[0][4]):
                print('\n---------- Exécution du tour numéro ' + str(t + 1) + ' -----------')
                ronde = creer_tour(selection_joueurs, t)
                liste_match = list(ronde.liste_matchs)
                ronde.liste_matchs.clear()
                print('liste_match ', liste_match)
                for m in range(len(liste_match)):
                    score = 0
                    print('\nMatch numéro ' + str(m+1) + ': ' + str(liste_match[m]))
                    while score not in ('1', '2', '3'):
                        score = input('Choississez le gagnant du match'
                                      '\n tapez 1 pour: ' + str(liste_match[m][0]) +
                                      '\n tapez 2 pour: ' + str(liste_match[m][1]) +
                                      '\n tapez 3 pour: Match nul'
                                      '\n votre choix: ')
                    if score == '1':
                        ronde.liste_matchs.append(([liste_match[m][0], '1'], [liste_match[m][1], '0']))
                    if score == '2':
                        ronde.liste_matchs.append(([liste_match[m][0], '0'], [liste_match[m][1], '1']))
                    if score == '3':
                        ronde.liste_matchs.append(([liste_match[m][0], '1/2'], [liste_match[m][1], '1/2']))
                print(ronde.liste_matchs)
                tour_suivant = ""
                while tour_suivant.lower() != 'y':
                    tour_suivant = input('\nSouhaitez vous exécuter la ronde suivante? (Y): ')
                """tournois_existants[tournoi_selectionne[1]]"""
        elif choix == '3':
            pass
        elif choix == '4':
            break


if __name__ == "__main__":
    main()

    # déterminer la liste des matchs
    # générer les paires de joueurs (instance de ronde)
    # lancer les matchs
    # entrer les résultats
    # sauvegarder le controleur de temps
    # mise a jour manuel du classement
    # afficher les résultats

# générer des rapports
# lister les acteurs
# lister les joueurs du tournoi
# lister les tournois
# lister les matchs du tournoi
# Remarque du directeur
