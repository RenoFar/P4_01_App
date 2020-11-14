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
    tournoi = Tournoi(nom, lieu, date, mode_jeu, nbre_tour, description)
    return tournoi


def ajouter_joueur():  # ajouter les joueurs
    ajout = ""
    ajout1 = 0
    for j in enumerate(joueurs_connus): print(j)
    while ajout not in ('1', '2'):
        ajout = input('\nAjouter un joueur connu : 1'
                      '\nCréer un nouveau joueur : 2\n')
    if ajout == '1':
        while ajout1 not in (enumerate(joueurs_connus)):
            ajout1 = input('\nSélectionner le numero du joueur: ')
        return joueurs_connus(ajout1)
    if ajout == '2':
        nouveau_joueur = creer_joueur()
        joueurs_connus.append(nouveau_joueur)
        ajouter_joueur()

def creer_joueur():
    nom = ""
    prenom = ""
    date_naissance =""
    sexe =""
    classement = 0
    while len(nom) < 1 or not nom.isalnum():
        nom = input("\nVeuillez saisir le nom du joueur: ")
    while len(prenom) < 1 or not prenom.isalnum():
        prenom = input("Veuillez saisir le prénom du joueur: ")

    date_naissance = input("Veuillez saisir la date de naissance du joueur: ")

    while sexe.lower() not in ('f', 'm'):
        sexe = input("Veuillez saisir le sexe du joueur (F/M): ")
    while true:
        classement = input("Veuillez saisir le classement du joueur: ")
        try:
            classement = int(classement)
            if classement > 0 : break
        except ValueError: print('Veuillez saisir un entier positif!\n')
    joueur = Joueur(nom, prenom, date_naissance, sexe, classement)
    return joueur


def main():
    """Fonction principale d'exécution de l'application"""
joueurs_connus = []
tournois_existants = []
choix =""
while choix not in ('1', '2'):
    choix = input('\nMenu principal: '
                  '\nCréer un tournoi : 1'
                  '\nExécuter un tournoi: 2'
                  '\nVoir les rapports : 3')
if choix == '1':
    choix1 = creer_tournoi()
    tournois_existantschoix1
    ajouter_joueur()
elif choix == '2': pass

elif choix == '3': pass




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
