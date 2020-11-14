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

    def __init__(self, nom, lieu, date, nbre_tour=4, mode_jeu, description=""):
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
    - son classement
    - numéro de l'indice joueur en mémoire"""

    def __init__(self, nom, prenom, date_naissance, sexe, classement=0, indice=""):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        self.indice = indice


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
    nom = "", lieu = "", date = "", nbre_tour = 4, mode_jeu, description = ""
    while len(nom) < 1 or not nom.isalnum():
        nom = input("\nVeuillez saisir le nom du tournoi: ")
    while len(lieu) < 1:
        lieu = input("Veuillez saisir le Lieu du tournoi: ")
    while len(date) < 1:
        date = input("Date du tournoi: ")
    while len(description) < 1:
        description = input("Veuillez saisir la Description du tournoi: ")
    while True:
        nbre_tour = input('le nombre de tours par défaut est de 4.'
                                  '\nSaisissez un autre nombre ou Entrée pour valider: ')
        if len(nbre_tour) < 1:  # si rien n'est saisi
            nbre_tour = 4
            break
        else:
            try:
                nbre_tour = int(nbre_tour)  # conversion en entier
                if nbre_tour > 0: break
            except ValueError: print('Veuillez saisir un entier positif!\n')
    print('le nombre de tours est de ' + str(nbre_tour))
    while mode_jeu.lower() not in ('bullet', 'blitz', 'rapide'):
        mode_jeu = input("Veuillez saisir le mode du tournoi (bullet / blitz / rapide): ")
    tournoi = Tournoi(nom, lieu, date, nbre_tour, mode_jeu, description)
    return tournoi


def ajouter_joueur():  # ajouter les joueurs
    ajout = ""
    while ajout not in ('1', '2'):
        ajout = input('\nAjouter un joueur connu : 1'
                      '\nAjouter un nouveau joueur : 2')
    if ajout == '1':

    if ajout == '2':
        creer_joueur_()


def creer_joueur_:()
    nom = "", prenom = "", date_naissance ="", sexe ="", classement = 0, indice = ""
    while len(nom) < 1 or not nom.isalnum():
        nom = input("\nVeuillez saisir le nom du joueur: ")
    while len(prenom) < 1 or not prenom.isalnum():
        prenom = input("Veuillez saisir le prénom du joueur: ")

    date_naissance = input("Veuillez saisir la date de naissance du joueur: ")

    while sexe.lower() not in ('f', 'm'):
        sexe = input("Veuillez saisir le sexe du joueur (F/M): ")
    while true:
        classement = input("Veuillez saisir le classement du joueur: ")
        try
            classement = int(classement)
            if classement > 0 : break
        except ValueError: print('Veuillez saisir un entier positif!\n')
    joueur = Joueur(nom, prenom, date_naissance, sexe, classement, indice)
    return joueur


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


def main():
    """Fonction principale d'exécution de l'application"""
choix =""
while choix not in ('1', '2'):
    choix = input('\nMenu principal: '
                  '\nCréer un tournoi : 1'
                  '\nVoir les raports : 2')
if choix == '1':
    choix1 = creer_tournoi()
    ajouter_joueur()
if choix == '2': pass



if __name__ == "__main__":
    main()
