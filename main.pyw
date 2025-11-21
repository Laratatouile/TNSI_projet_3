import voiture
import parking


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
if reponse == "1":
    while True:
        print("voiture")
elif reponse == "2":
    print("interface")






# si l'utilisateur choisis la console
if input("Type de parking : ") == "1":





