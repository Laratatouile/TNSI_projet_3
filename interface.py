import customtkinter as ctk
from PIL import Image
import random

class Fenetre(ctk.CTk):
    def __init__(self, parking:object):
        super().__init__()

        # options de la fenetre
        self.title("Les parkings")
        self.geometry("1150x694+100+40")
        self.minsize(1150, 694)
        self.maxsize(1150, 5500)

        self.parking = parking.parking

        self.etage = ctk.StringVar(self, value="0")
        # les frames
        self.frame_titre = FrameTitre(self)
        self.frame_parking = FrameParking(self)
        self.frame_etage = FrameEtage(self, self)


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
            width=1080,
            height=624,
            corner_radius=0,
        )
        self.pack(side="left")
        self.master = master
        self.colone_place = [0, 2, 3, 5, 6, 8, 9, 11]
        self.ligne_place = range(1, 9)
        self.colone_place_gauche = [0, 3, 6, 9]
        self.tableau = [[False for _ in range(12)] for _ in range(12)]
        CASE_WIDTH, CASE_HEIGHT = 90, 52  # taille de tes cases

        # Voiture droite
        img_tmp = Image.open("images/voiture.png").rotate(270, expand=True)
        img_tmp = img_tmp.resize((CASE_WIDTH, CASE_HEIGHT))
        self.img_voiture_droite = ctk.CTkImage(img_tmp, size=(CASE_WIDTH, CASE_HEIGHT))

        # Voiture gauche
        img_tmp = Image.open("images/voiture.png").rotate(90, expand=True)
        img_tmp = img_tmp.resize((CASE_WIDTH, CASE_HEIGHT))
        self.img_voiture_gauche = ctk.CTkImage(img_tmp, size=(CASE_WIDTH, CASE_HEIGHT))

        # Parking droite
        img_tmp = Image.open("images/place.png").rotate(270, expand=True)
        img_tmp = img_tmp.resize((CASE_WIDTH, CASE_HEIGHT))
        self.img_parking_droite = ctk.CTkImage(img_tmp, size=(CASE_WIDTH, CASE_HEIGHT))

        # Parking gauche
        img_tmp = Image.open("images/place.png").rotate(90, expand=True)
        img_tmp = img_tmp.resize((CASE_WIDTH, CASE_HEIGHT))
        self.img_parking_gauche = ctk.CTkImage(img_tmp, size=(CASE_WIDTH, CASE_HEIGHT))

        # creation de la grille
        for i in range(12):
            self.rowconfigure(i, weight=1)
        for i in range(12):
            self.columnconfigure(i, weight=1)


        # creation de la grille
        for ligne in range(12):
            for colone in range(12):
                case = ctk.CTkFrame(
                    self,
                    fg_color="#333",
                    corner_radius=0,
                    width=90,
                    height=52
                )

                case.grid(row=ligne, column=colone, padx=0, pady=0)

                label = ctk.CTkLabel(case, text="", width=90, height=52)
                label.pack(expand=True, fill="both", padx=0, pady=0)

                self.tableau[ligne][colone] = label
        self.remplir_grille()


    

    def remplir_grille(self):
        i = 1
        for ligne in range(12):
            for colone in range(12):
                if not colone in self.colone_place:
                    continue
                if not ligne in self.ligne_place:
                    continue
                voiture = self.master.parking[self.master.etage.get()][f"{str(i)}"]
                if voiture != None:
                    self.tableau[ligne][colone].configure(image=(self.img_voiture_gauche if colone in self.colone_place_gauche else self.img_voiture_droite))
                    self.tableau[ligne][colone].image_ref = (self.img_voiture_gauche if colone in self.colone_place_gauche else self.img_voiture_droite)
                    self.tableau[ligne][colone].bind(
                        '<Double-Button-1>',
                        lambda event, v=voiture: self.ouvrir_menu(event, v)
                    )
                else:
                    self.tableau[ligne][colone].configure(image=(self.img_parking_gauche if colone in self.colone_place_gauche else self.img_parking_droite))
                    self.tableau[ligne][colone].image_ref = (self.img_parking_gauche if colone in self.colone_place_gauche else self.img_parking_droite)
                i += 1


    def ouvrir_menu(self, event, voiture:object):
        OuvrirMenu(self.master, voiture)








class FrameEtage(ctk.CTkFrame):
    """ frame qui contient le systeme d'etages """
    def __init__(self, event, master:Fenetre):
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
        self.master.frame_parking.remplir_grille()

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
        self.master.frame_parking.remplir_grille()





class OuvrirMenu(ctk.CTkToplevel):
    def __init__(self, fenetre:object, voiture:object):
        super().__init__(fenetre)
        self.title("Informations sur la voiture")
        self.geometry("250x250+200+200")
        self.attributes("-topmost", True)

        # les infos
        ctk.CTkLabel(
            self,
            text="Nom :",
            font=('Arial', 20)
        ).place(x=20, y=20)
        ctk.CTkLabel(
            self, 
            text=f"e",#{voiture.proprio}",
            font=('Arial', 20)
        ).place(x=20, y=50)
        ctk.CTkLabel(
            self,
            text="Marque :",
            font=('Arial', 20)
        ).place(x=20, y=80)
        ctk.CTkLabel(
            self,
            text=f"e",#{voiture.marque}",
            font=('Arial', 20)
        ).place(x=20, y=110)
        ctk.CTkLabel(
            self,
            text="Plaque :",
            font=('Arial', 20)
        ).place(x=20, y=140)
        ctk.CTkLabel(
            self,
            text=f"e",#{voiture.plaque}",
            font=('Arial', 20)
        ).place(x=20, y=170)

