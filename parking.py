class Parking:
    def __init__(self):
        self.dict_abo = {}
        self.liste_place_abo_libres = []
        self.parking = {f"{etage}" : {f"{etage}{i}" : None for i in range(1, 81)} for etage in range(0, 5)}



    def ajouter_voiture(self, voiture:object) -> bool:
        """ ajoute une voiture sur le parking """
        # si la voiture est abonee
        if voiture in self.dict_abo.keys():
            place = str(self.dict_abo[voiture])
            if self.parking[place] == None:
                self.parking[place] = voiture
            else:
                place = self.__premiere_place_libre()
                self.parking[place] = voiture
        # si elle n'est pas abonee
        else:
            self.parking[str(self.__premiere_place_libre())] = voiture
    



    def place_vide(self, place:int) -> any:
        """ renvoie si une place est vide ou non """
        if type(self.parking[str(place)]) == None:
            return False
        return self.parking[str(place)]
    




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
        for place, voiture in self.parking.items():
            if voiture == None:
                return place
        return False




    
    def affiche_etage(self, numero):
        # generer une liste correspondant aux places de l'etage
        for place, voiture in self.parking.items(): # place str , voiture objet
            # verifier si le premier chiffre de la place est egal a notre numero d'etage faire (attention aux types int et str)
            # si la place est dans l'etage :
                # modifier la case de la liste correspondant a la place dans l'etage par True
            pass
        # afficher la liste
        







