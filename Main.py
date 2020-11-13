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
    - son controleur de temps
    - sa descrition"""

    def __init__(self, nom="", lieu="", date="", nbre_tour=4, description=""):
        self.nom = nom
        self.lieu = lieu
        self.date = date
        self.nbre_tour = nbre_tour
        """self.tournee = tournee"""
        """self.indices_joueurs = indices_joueurs"""
        """self.duree = duree"""
        self.description = description


class Joueur:  # Définition de notre classe Joueur
    """Classe définissant un joueur caractérisé par :
    - son nom
    - son prénom
    - sa date de naissance
    - son sexe
    - son classement"""

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
    """"Fonction principale d'exécution de l'application"""
creer_tournoi()

def creer_tournoi():  #créer le tournoi
    tournoi = Tournoi()
    tournoi.nom = input("Nom du tournoi: ")
    tournoi.lieu = input("Lieu du tournoi: ")
    tournoi.date = input("Date du tournoi: ")
    tournoi.description = input("Description du tournoi: ")
    nbre_tour= input('le nombre de tours par défaut est de {}.\nSaisissez un autre nombre ou Entrée pour valider: ',
                     format(tournoi.nbre_tour))
    if int(nbre_tour) > 0:
        tournoi.nbre_tour = nbre_tour
    print('\nle nombre de tours est de ' + str(tournoi.nbre_tour))
    #Ajouter huit joueurs

    #executer les tours
        #déterminer la liste des matchs
            #générer les paires de joueurs (instance de ronde)
        #lancer les matchs
            #entrer les résultats
        #sauvegarder le controleur de temps
    #mise a jour manuel du classement
    #afficher les résultats
    pass

#Générer des rapports
    #lister les acteurs
    #lister les joueurs du tournoi
    #lister les tournois
    #lister les matchs du tournoi
    #Remarque du directeur

if __name__ == "__main__":
    main()