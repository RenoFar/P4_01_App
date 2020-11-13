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

    def __init__(self, nom="", lieu="", date="", nbre_tour=4, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbre_tour = nbre_tour
        self.description = description
        """self.tournee = tournee"""
        """self.indices_joueurs = indices_joueurs"""
        """self.duree = duree"""


class Joueur:  # Définition de la classe Joueur
    """Classe définissant un joueur caractérisé par :
    - son nom
    - son prénom
    - sa date de naissance
    - son sexe
    - son classement
    - Liste des indices correspondant aux instances du joueur"""

    def __init__(self, nom="", prenom="", date_naissance="", sexe="", classement=1):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement
        """"self.indices = indices"""


class Tour:  # Définition de la classe Tour
    """Classe définissant un tour caractérisé par :
    - sa liste de matchs"""

    def __init__(self):
        self.liste_matchs = []


def creer_tournoi():  #créer le tournoi
    tournoi = Tournoi()
    while len(tournoi.nom)<1 or not tournoi.nom.isalpha():
        tournoi.nom = input("\nVeuillez saisir le nom du tournoi: ")
    while len(tournoi.lieu) < 1 or not tournoi.lieu.isalpha():
        tournoi.lieu = input("\n saisir le Lieu du tournoi: ")

    tournoi.date = input("\nDate du tournoi: ")

    while len(tournoi.description) < 1 or not tournoi.description.isalpha():
        tournoi.description = input("\nVeuillez saisir la Description du tournoi: ")

    nbre_tour = input('\nle nombre de tours par défaut est de {}.\nSaisissez un autre nombre ou Entrée pour valider: '.
                      format(tournoi.nbre_tour))
    if nbre_tour is int or len(nbre_tour)>0:
        tournoi.nbre_tour = nbre_tour
    print('\nle nombre de tours est de ' + str(tournoi.nbre_tour))


def Ajouter_joueur():  #Ajouter les joueurs
    joueur = Joueur()
    while len(joueur.nom) < 1 or not joueur.nom.isalpha():
        joueur.nom = input("\nVeuillez saisir le nom du joueur: ")
    while len(joueur.prenom) < 1 or not joueur.prenom.isalpha():
        joueur.prenom = input("\nVeuillez saisir le prénom du joueur: ")

    joueur.date_naissance = input("\nVeuillez saisir la date de naissance du joueur: ")

    while joueur.sexe.lower() != 'f' or joueur.sexe.lower() != 'm':
        joueur.sexe = input("\nVeuillez saisir le sexe du joueur (F/M): ")

    #déterminer la liste des matchs
        #générer les paires de joueurs (instance de ronde)
    #lancer les matchs
        #entrer les résultats
        #sauvegarder le controleur de temps
    #mise a jour manuel du classement
    #afficher les résultats

#Générer des rapports
    #lister les acteurs
    #lister les joueurs du tournoi
    #lister les tournois
    #lister les matchs du tournoi
    #Remarque du directeur


def main():
    """"Fonction principale d'exécution de l'application"""
    creer_tournoi()
    pass


if __name__ == "__main__":
    main()