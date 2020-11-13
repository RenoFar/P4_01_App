#! /usr/bin/env python3
# coding: utf-8

import Package.fonctions


class Tournoi:  # Définition de notre classe Tournoi
    """Classe définissant un tournoi caractérisé par :
    - son nom
    - son lieu
    - sa date
    - son nombre de tour
    - sa liste de tournées
    - sa liste de joueurs
    - son controleur du temps
    - sa descrition"""

    def __init__(self, nom="", lieu="", date="", nbre_tour=4, tournee=[], indices_joueurs=[], description=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbre_tour = nbre_tour
        self.tournee = tournee
        self.indices_joueurs = indices_joueurs
        self.description = description


class Joueur:  # Définition de notre classe Joueur
    """Classe définissant un joueur caractérisé par :
    - son nom
    - son prénom
    - sa date de naissance
    - son sexe
    - sa classement"""

    def __init__(self, nom="", prenom="", date_naissance="", sexe="", classement=1):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.sexe = sexe
        self.classement = classement


class Tour:  # Définition de notre classe Tour
    """Classe définissant un tour caractérisé par :
    - sa liste de matchs"""

    def __init__(self):
        self.liste_matchs = []


def main():
    pass
#créer tournoi
    #Ajouter huit joueurs
    #executer les tours
        #déterminer la liste des matchs
            #générer les paires de joueurs (instance de ronde)
        #lancer les matchs
            #entrer les résultats
        #sauvegarder le controleur de temps



if __name__ == "__main__":
    main()