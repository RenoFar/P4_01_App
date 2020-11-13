#! /usr/bin/env python3
# coding: utf-8

import Package.fonctions

class Tournoi: # Définition de notre classe Tournoi
    """Classe définissant un tournoi caractérisé par :
    - son nom
    - son lieu
    - sa date
    - son nombre de tour
    - sa liste de tournées
    - sa liste de joueurs
    - son controleur du temps
    - sa descrition"""

    def __init__(self):  # Notre méthode constructeur
        """Pour l'instant, on ne va définir que les attribut"""
        self.nom = ""
        self.lieu = ""
        self.date= ""
        self.nbre_tour = 1
        self.tournee = []
        self.indices_joueurs = []
        self.description = ""


class Joueur: # Définition de notre classe Joueur
    """Classe définissant un joueur caractérisé par :
    - son nom
    - son prénom
    - sa date de naissance
    - son sexe
    - sa classement"""

    def __init__(self):  # Notre méthode constructeur
        """Pour l'instant, on ne va définir que les attribut"""
        self.nom = ""
        self.prenom = ""
        self.date_naissance = ""
        self.sexe = ""
        self.classement = 1


class Tour: # Définition de notre classe Tour
    """Classe définissant un tour caractérisé par :
    - sa liste de matchs"""

    def __init__(self):  # Notre méthode constructeur
        """Pour l'instant, on ne va définir que les attribut"""
        self.liste_matchs = []


def main():
    pass

if __name__ == "__main__":
    main()