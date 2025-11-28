class Parking:
    def __init__(self):
        self.dict_abo = {}
        self.liste_place_abo_libres = []
        self.parking = {f"{etage}" : {f"{i}" : None for i in range(1, 81)} for etage in range(0, 5)}



    def ajouter_voiture(self, voiture:object) -> bool:
        """ ajoute une voiture sur le parking """
        # si la voiture est abonee
        if voiture in self.dict_abo.keys():
            place = str(self.dict_abo[voiture])
            if self.parking[place[0]][place[1:]] == None:
                self.parking[place[0]][place[1:]] = voiture
            else:
                place = self.__premiere_place_libre()
                self.parking[place[0]][place[1:]] = voiture
        # si elle n'est pas abonee
        else:
            place = str(self.__premiere_place_libre())
            self.parking[place[0]][place[1:]] = voiture


    def retirer_voiture(self, place:str) -> None:
        """ retire une voiture d'une place """
        self.parking[place[0]][place[1:]] = None
        return None

    



    def place_vide(self, place:int) -> any:
        """ renvoie si une place est vide ou non """
        if type(self.parking[str(place)[0]][str(place)[1:]]) == None:
            return False
        return self.parking[str(place)[0]][str(place)[1:]]
    


    def get_abonnes(self) -> dict:
        """ renvoie le dictionnaire des abonnes """
        return self.dict_abo
    



    def abonnement(self, voiture:object) -> None:
        """ abone une voiture """
        if self.liste_place_abo_libres != []:
            self.dict_abo[voiture] = self.liste_place_abo_libres.pop(0)
        else:
            self.dict_abo[voiture] = self.__premiere_place_libre()


    def desabonnement(self, voiture:object) -> None:
        """ retire l'abonnement d'une voiture """
        del self.dict_abo[voiture]
        





    def __premiere_place_libre(self):
        """ renvoie la premiere place libre du parking """
        for nbr_etage, etage in self.parking.items():
            for place, voiture in etage.items():
                if voiture == None:
                    return f"{nbr_etage}{place}"
        return None


    
    def affiche_etage(self, numero_etage:str):
        liste_voiture = [False for _ in range(80)]
        for place, voiture in self.parking[numero_etage].items():
            if voiture != None :
                liste_voiture[place] = True 
        print(liste_voiture)
        







