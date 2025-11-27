import voiture
import parking
import random
import time
import threading


# instancier un parking pour la generation de la liste des voitures
parking1 = parking.Parking()

# recuperer la liste des voitures
liste_voitures = voiture.generer_voiture_aleatoire(parking1)



# demander a l'utilisateur le type d'interface

print("""
    Choisissez l'interface que vous souhaitez
     ______________________________________________
    |                                              |
    |   1 : Parking affiche dans la console        |
    |                                              |
    |   2 : Parking dans une interface graphique   |
    |______________________________________________|
    
    Entrez 1 ou 2
""")
reponse = input(">>>")





class Actions:
    """ gere les actions pour le parking """
    def __init__(self, parking:object, liste_voitures:list) -> None:
        """ initialise les variables pour les actions """
        self.parking = parking
        self.liste_voitures = liste_voitures
        self.actions_possibles = ["ajouter_voiture", "retirer_voiture", "abonnement", "desabonnement"]


    def aleatoire(self) -> None:
        """ realise une action aleatoire sur le parking """
        voiture_use = random.choice(self.liste_voitures)
        option = random.choice(self.actions_possibles)
        place = f"{random.randint(0, 4)}{random.randint(1, 81)}"
        if option == "ajouter_voiture":
            self.parking.ajouter_voiture(voiture_use)
        elif option == "retirer_voiture":
            i = 0
            while self.parking.place_vide(place):
                place = f"{random.randint(0, 4)}{random.randint(1, 81)}"
                if i == 10:
                    break
            else:
                self.parking.retirer_voiture(place)
        elif option == "abonnement":
            self.parking.abonnement(voiture_use)
        elif option == "desabonnement":
            liste_abos = self.parking.get_abonnes().keys()
            if not liste_abos == []:
                return
            voiture_use = random.choice(liste_abos)
            self.parking.desabonnement(voiture_use)
        return None
            
        
            



action = Actions(parking1, liste_voitures)


def boucle():
    while True:
        action.aleatoire()


thread_actions = threading.Thread(target=boucle())
thread_actions.start()



# si l'utilisateur choisis la console
if reponse == "1":
    actions = Actions(parking1, liste_voitures)
    while True:
        print("numero de l'etage : ")
        num_etage = int(input(">>>"))
        print(num_etage)
        #self.parking.affiche_etage(num_etage)





