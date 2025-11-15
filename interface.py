import customtkinter as ctk
from PIL import Image, ImageTk
import random

class Fenetre(ctk.CTk):
    def __init__(self, parking:object):
        super().__init__()

        # options de la fenetre
        self.title("Les parkings")
        self.geometry("1060x642+100+40")
        self.minsize(1060, 642)
        self.maxsize(6000, 5500)

        self.parking = parking

        self.etage = ctk.StringVar(self, value="0")
        # les frames
        self.frame_titre = FrameTitre(self)
        self.frame_parking = FrameParking(self)
        self.frame_etage = FrameEtage(self)


        self.mainloop()




class FrameTitre(ctk.CTkFrame):
    """ frame qui contient le titre """
    def __init__(self, master:Fenetre):
        """ constructeur """
        super().__init__(
            master,
            height=70,
            corner_radius=0,
            border_width=2,
            border_color="#a8a8a8",
            fg_color="#6D6D6D"
        )
        self.pack(fill="x")
        ctk.CTkLabel(
            self,
            text="Getion du parking",
            text_color="#000000",
            font=('Arial', 35)
        ).place(x=120, y=12)





class FrameParking(ctk.CTkFrame):
    """ frame qui contient le dessin des parkings """
    def __init__(self, master:Fenetre):
        """ constructeur """
        super().__init__(
            master,
            width=990,
            height=572,
            corner_radius=0,
        )
        self.pack(side="left")
        self.master = master
        self.colone_place = [0, 2, 3, 5, 6, 8, 9, 11]
        self.ligne_place = range(1, 11)
        self.colone_place_gauche = [0, 3, 6, 9]
        self.tableau = [[False for _ in range(11)] for _ in range(11)]
        self.img_voiture_droite = ImageTk.PhotoImage(Image.open("images/voiture.png").rotate(90))
        self.img_voiture_gauche = ImageTk.PhotoImage(Image.open("images/voiture.png").rotate(270))
        self.img_parking_droite = ImageTk.PhotoImage(Image.open("images/place.png").rotate(90))
        self.img_parking_gauche = ImageTk.PhotoImage(Image.open("images/place.png").rotate(270))
        # creation de la grille
        for ligne in range(11):
            for colone in range(11):
                cell = ctk.CTkFrame(
                    self,
                    width=90,
                    height=52,
                    fg_color="#333",
                    corner_radius=0
                )
                self.tableau[ligne][colone] = ctk.CTkLabel(self)
                cell.grid(row=ligne, column=colone)
        self.remplir_grille()


    

    def remplir_grille(self):
        liste_places = [False]*80
        for place, voiture in self.master.parking.items():
            print('ok')
            if place[0] == self.master.etage:
                if voiture == True:
                    liste_places[place[1:]] = True

        i = 0
        for ligne in range(11):
            for colone in range(11):
                if not colone in self.colone_place:
                    continue
                if not ligne in self.ligne_place:
                    continue
                if liste_places[i]:
                    self.tableau[ligne][colone].configure(image=(self.img_voiture_gauche if ligne in self.colone_place_gauche else self.img_voiture_droite))
                    self.tableau[ligne][colone].image_ref = image=(self.img_voiture_gauche if ligne in self.colone_place_gauche else self.img_voiture_droite)
                else:
                    self.tableau[ligne][colone].configure(image=(self.img_parking_gauche if ligne in self.colone_place_gauche else self.img_parking_droite))
                    self.tableau[ligne][colone].image_ref = image=(self.img_parking_gauche if ligne in self.colone_place_gauche else self.img_parking_droite)
                i += 1








class FrameEtage(ctk.CTkFrame):
    """ frame qui contient le systeme d'etages """
    def __init__(self, master:Fenetre):
        """ constructeur """
        self.master = master
        super().__init__(
            master,
            width=70,
            corner_radius=0,
            fg_color="#525252"
        )
        self.pack(fill="y", side="right")
        # le texte de l'etage
        self.txt_etage = ctk.CTkLabel(
            self,
            text=master.etage.get(),
            text_color="#000000",
            font=('Arial', 35)
        )
        self.txt_etage.place(x=25, y=180)
        # le bouton pour monter
        ctk.CTkButton(
            self,
            width=50,
            text="/\\",
            font=('Arial', 35, "bold"),
            fg_color="#525252",
            hover_color="#525252",
            text_color="#000000",
            command=self.etage_haut
        ).place(x=10, y=110)
        # le bouton pour descendre
        ctk.CTkButton(
            self,
            width=50,
            text="\\/",
            font=('Arial', 35, "bold"),
            fg_color="#525252",
            hover_color="#525252",
            text_color="#000000",
            command=self.etage_bas
        ).place(x=10, y=245)


    def etage_haut(self):
        """ monte d'un etage """
        etage = int(self.master.etage.get())
        if etage <= 0:
            self.master.etage.set("1")
        elif etage >= 4:
            self.master.etage.set("4")
        else:
            self.master.etage.set(f"{etage+1}")
        etage = self.master.etage.get()
        self.txt_etage.configure(text=etage)

    def etage_bas(self):
        """ descend d'un etage """
        etage = int(self.master.etage.get())
        if etage <= 0:
            self.master.etage.set("0")
        elif etage >= 4:
            self.master.etage.set("3")
        else:
            self.master.etage.set(f"{etage-1}")
        etage = self.master.etage.get()
        self.txt_etage.configure(text=etage)








Fenetre({f"{etage}" : {f"{etage}{i}" : random.choice([False, True]) for i in range(1, 81)} for etage in range(0, 5)})