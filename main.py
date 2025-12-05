import voiture
import parking
import random
import time
import threading
import interface


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
reponse = input(">>> ")





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
        place = f"{random.randint(0, 4)}{random.randint(1, 80)}"
        # on ajoute une voiture
        if option == "ajouter_voiture":
            self.parking.ajouter_voiture(voiture_use)
        # on en retire une
        elif option == "retirer_voiture":
            i = 0
            while self.parking.place_vide(place):
                place = f"{random.randint(0, 4)}{random.randint(1, 80)}"
                if i == 10:
                    break
            else:
                self.parking.retirer_voiture(place)
        # on abonne une voiture
        elif option == "abonnement":
            self.parking.abonnement(voiture_use)
        # on en desabonne une
        elif option == "desabonnement":
            liste_abos = self.parking.get_abonnes().keys()
            if not liste_abos == []:
                return
            voiture_use = random.choice(liste_abos)
            self.parking.desabonnement(voiture_use)
        return None
    

    def boucle(self):
        global thread_boucle
        while thread_boucle:
            self.aleatoire()
            time.sleep(0.1)



            



action = Actions(parking1, liste_voitures)

thread_boucle = True
thread_actions = threading.Thread(target=action.boucle, daemon=True)
thread_actions.start()

for _ in range(10):
    print()

# si l'utilisateur choisis la console
print(reponse)
if reponse == "1":
    actions = Actions(parking1, liste_voitures)
    while True:
        print()
        print("tapez x pour arreter")
        print("numero de l'etage : ")
        num_etage = input(">>> ")
        for _ in range(5):
            print()
        if num_etage == "x":
            break
        else:
            try:
                if 0 <= int(num_etage) < 5:
                    parking1.affiche_etage(num_etage)
                else:
                    print("l'etage selectionne n'est pas valide")
            except Exception as e:
                print("ce n'est pas un chiffre")
                print(e)


elif reponse == "2":
    interface.Fenetre(parking1)




if thread_actions.is_alive():
    thread_boucle = False
print("le code a fini de s'executer normalement")



