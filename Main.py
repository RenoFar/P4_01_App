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
    - sa date
    - son heure de début
    - son heure de fin
    - sa liste de matchs"""

    def __init__(self, nom, date, debut, fin):
        self.nom = nom
        self.date = date
        self.debut = debut
        self.fin = fin
        self.liste_matchs = []


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
    tournoi = Tournoi(nom, lieu, date, mode_jeu, nbre_tour, description)
    return tournoi


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
                               '\nAjouter un nouveau joueur : 2\n')
            if choix_menu == '1':
                while choix_joueur not in listing_joueur:
                    choix_joueur = input('Sélectionner le numéro du joueur : ')
            elif choix_menu == '2':
                nouveau_joueur = creer_joueur()
                liste_joueurs.append([nouveau_joueur.nom, nouveau_joueur.prenom, nouveau_joueur.date_naissance,
                                      nouveau_joueur.sexe, nouveau_joueur.classement])
    return [choix_joueur, liste_joueurs]


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
    joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
    return joueur


def main():
    """Fonction principale d'exécution de l'application"""
    joueurs_connus = [['j1', 'qhh', '12', 'f', 18], ['j2', 'qgth', '14', 'm', 7]]
    tournois_existants = []
    choix = ""
    while choix not in ('1', '2', '3', '4'):
        choix = input('\n---------- Menu principal -----------'
                      '\nCréer un tournoi : 1'
                      '\nExécuter un tournoi: 2'
                      '\nVoir les rapports : 3\n'
                      '\nSaisissez le Numéro de votre choix: ')
    if choix == '1':
        nouveau_tournoi = creer_tournoi()
        for n in range(3):
            print('\n--------- Selectionner le joueur numéro ' + str(n+1) + ' ---------')
            joueurs_tournoi = ajouter_joueur(joueurs_connus)
            joueurs_connus = joueurs_tournoi[1]
            print('liste à jour : ', joueurs_connus)
            nouveau_tournoi.indices_joueurs.append(joueurs_tournoi[0])
            print('numéro des joueurs choisis : ', nouveau_tournoi.indices_joueurs)
        tournois_existants.append([nouveau_tournoi.nom, nouveau_tournoi.lieu, nouveau_tournoi.date,
                                   nouveau_tournoi.mode_jeu, nouveau_tournoi.nbre_tour,
                                   nouveau_tournoi.description, nouveau_tournoi.indices_joueurs])
    elif choix == '2':
        pass
    elif choix == '3':
        pass
    elif choix == '4':
        pass
    print('\nliste des joueurs connus: ', joueurs_connus)
    print('\nliste des tournois connus: ', tournois_existants, '\n')


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
