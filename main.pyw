import parking
import random





class Voiture:
    def __init__(self, imatriculation, marque, nom_proprio, abonnement):
        self.imatriculation = imatriculation
        self.marque = marque
        self.proprio = nom_proprio
        self.abonnement = abonnement




def generer_voiture_aleatoire():
    liste_voiture = []
    place = random.randint(20, 25)
    imatriculation = f"{random.randint(1000, 9999)}-{random.choice(['AA', 'BB', 'CC', 'DD', 'EE'])}-{random.randint(1, 99)}"
    marques = ['Toyota', 'ford' , 'BMW', 'Audi', 'Mercedes', 'Honda', 'Chevrolet', 'Nissan', 'Volkswagen', 'Hyundai', 'Kia', 'Mazda', 'Subaru', 'Dodge', 'Jeep', 'Lexus', 'Cadillac', 'Acura', 'Infiniti', 'Volvo']
    nom_proprio = [
    "Aaron Martin", "Abel Moreau", "Adam Bernard", "Adrian Laurent",
    "Aiden Dubois", "Alban Lefèvre", "Alex Barre", "Alexis Perrot",
    "Ali Tessier", "Allan Mercier", "Amaury Caron", "Ambroise Colin",
    "Amine Petit", "Anas Fontaine", "André Rousseau", "Antoine Lemoine",
    "Anton Garnier", "Aram Roux", "Arnaud Brun", "Arthur Richard",
    "Aubin Chevalier", "Audric Hubert", "Augustin Millet", "Aurélien Boucher",
    "Axel Rolland", "Ayden Noël", "Baptiste Barret", "Basile Parent",
    "Benjamin Faucher", "Bilal Cohen", "Boris Chauvin", "Brayan Fleury",
    "Briac Vaillant", "Brice Muller", "Caleb Boulanger", "Camille Robin",
    "Cédric Joly", "Celian Harel", "Charles Germain", "Charlie Renard",
    "Chris Lambert", "Christian Dupont", "Christopher Navarro", "Clarence Fouquet",
    "Clément Bourdon", "Clovis Renou", "Colin Prévot", "Corentin Blanchard",
    "Cyril Roche", "Damien Marchal", "Daniel Maurel", "David Langlois",
    "Denis Marquet", "Didier Robert", "Diego Garnier", "Dimitri Tissot",
    "Dorian Pelletier", "Driss Leroy", "Dylan Aubert", "Eddy Leclerc",
    "Edgar Morin", "Édouard Gaillard", "Eli Carpentier", "Elian Marty",
    "Elias Rault", "Elie Gillet", "Elliot Picard", "Eloan Pruvost",
    "Eloi Pottier", "Elouan Breton", "Emilien Chauvet", "Emir Camus",
    "Emmanuel Laporte", "Enes Dumont", "Enzo Cottin", "Erwan Breton",
    "Esteban Riou", "Ethan Marais", "Étienne Duhamel", "Evan Lejeune",
    "Ewen Albert", "Fabien Roger", "Fabrice Breton", "Fares Giraud",
    "Farid Meunier", "Félix Vaillant", "Fernand Poulain", "Flavio Debray",
    "Flavien Gosselin", "Florian Marechal", "Florentin Jacques", "Franck Roger",
    "François Paris", "Gabin Denis", "Gabriel Fournier", "Gaël Leroy",
    "Gaétan Riou", "Gary Roche", "Gauthier Samson", "Gautier Marin",
    "Geoffrey Lesage", "Georges Colin", "Gérald Charlier", "Germain Joubert",
    "Ghislain Benoit", "Gianni Duquesne", "Grégory Tessier", "Guillaume Deloire",
    "Gustave Roche", "Hakim Louvet", "Hamza Chevrier", "Hassan Martin",
    "Henri Badeau", "Herbert Giraud", "Hervé Rouillé", "Hicham Belin",
    "Hugo Lefort", "Hugues Racine", "Ibrahim Khalil", "Ilian Morand",
    "Imran Berthier", "Isaac Nicolas", "Ismaël Lagarde", "Ivan Poulin",
    "Ivo Gravier", "Iwan Cordier", "Jad Rey", "Jacky Garnier",
    "Jacob Montfort", "Jacques Delmas", "James Flament", "Jassem Millet",
    "Jason Brochard", "Jean Rochefort", "Jérémie Rollin", "Jérôme Letellier",
    "Jibril Hervieux", "Joachim Alves", "Joan Bruneau", "Johan Deschamps",
    "Jonathan Blin", "Jordan Boucher", "José Lemaitre", "Joseph Gérard",
    "Joshua Roland", "Josué Barthelemy", "Jules Marceau", "Julien Fabre",
    "Junior Poirier", "Justin Renier", "Kamel Da Costa", "Karim Teixeira",
    "Kassim Boudet", "Kévin Robert", "Killian Riou", "Kylian Fabre",
    "Lamine Guérin", "Laurent Hubert", "Léo Cantin", "Lenny Guillet",
    "Lenzo Martel", "Lilian Roche", "Lino Seguin", "Lionel Germain",
    "Livio Ramos", "Loïc Mahe", "Logan Adam", "Lorenzo Delaunay",
    "Loris Gaudin", "Loup Plouhinec", "Louis Bernard", "Luc Wurtz",
    "Lucas Muller", "Lucien Humbert", "Ludovic Terrier", "Maël Le Goff",
    "Mahé Boyer", "Malik Karoui", "Malone Renault", "Manuel Torres",
    "Marc Aubry", "Marcel Morel", "Marco Ferron", "Marin Le Dantec",
    "Mario Collin", "Marius Perrault", "Marouane Durand", "Martin Bellanger",
    "Marvin Garel", "Mateo Rivière", "Mathéo Roussel", "Mathias Despres",
    "Mathieu Colin", "Mathis Roche", "Matias Kaci", "Matteo Pierron",
    "Maxence Delorme", "Maxime Hardy", "Mehdi Haddad", "Melvin Clermont",
    "Mickaël Bernard", "Miguel Lopez", "Milann Gros", "Milan Garel",
    "Mohamed Benali", "Morgan Guillet", "Moussa Sylla", "Nabil Louati",
    "Nassim Derrien", "Naël Ricard", "Nathan Gosselin", "Nathanaël Barry",
    "Neil Prigent", "Nelson Gaborit", "Nicolas Herbin", "Nils Genet",
    "Nilton Bazin", "Noah Vernier", "Noam Maillot", "Nohan Faveron",
    "Nolan Le Borgne", "Norbert Raguet", "Omar Haddou", "Oscar Tardy",
    "Ossian Page", "Ousmane Cissé", "Pablo Garcia", "Pascal Guyot",
    "Patrice Reynaud", "Patrick Marot", "Paul Morlat", "Paulin Darras",
    "Philibert Cardon", "Philippe Lambert", "Pierre Roux", "Quentin Lefort",
    "Rafaël Arnaud", "Rayan Touati", "Rayane Kelian", "Reda Guel",
    "Rémi Letourneau", "Rémy Panneau", "Renan Gilbert", "René Durieux",
    "Riad Ben Amar", "Riley Chauveau", "Robin Bell", "Rodolphe Hennequin",
    "Romain Jean", "Roméo Garcia", "Ronald Gallois", "Ruben Cortes",
    "Rudy Le Hen", "Ryan Lopez", "Sacha Lopez", "Safwan Hammoud",
    "Salim Kader", "Samuel Alves", "Sandro Perez", "Saïd Khouma",
    "Samy Mellah", "Scott Berenger", "Sean Latour", "Sélim Tahar",
    "Sergio Donati", "Sidney Hanin", "Simon Vigne", "Sofiane Zerari",
    "Stanislas Perrin", "Stéphane Guyon", "Swann Riou", "Taha Meziane",
    "Tanguy Hellou", "Téo Leduc", "Théo Gauthier", "Thierry Tronet",
    "Thomas Baudin", "Thyméo Rigal", "Timothé Gane", "Timothée Aversenq",
    "Tony Girault", "Tristan Loriot", "Ugo Chatel", "Valentin Naud",
    "Victor Corre", "Viktor Almeida", "Vincent Andrieu", "Virgil Bernier",
    "Vivien Loire", "Wael Messaoud", "Wassim Bendaoud", "William Hardy",
    "Willy Brégeon", "Wissem Kamel", "Xavier Josselin", "Yacine Baya",
    "Yanis Hariri", "Yann Marchand", "Yannick Laurent", "Yohann Tessier",
    "Youssef Amrani", "Yvan Ferré", "Zacharie Bonin", "Zakaria El Idrissi",
    "Aaron Smith", "Adam Johnson", "Aiden Turner", "Alan Brooks",
    "Albert Mitchell", "Alex Carter", "Andrew Foster", "Anthony Hughes",
    "Arthur Gray", "Austin Rogers", "Barry Coleman", "Benjamin Scott",
    "Bernard Bryant", "Blake Adams", "Bradley Moore", "Brandon Cox",
    "Brent Jenkins", "Brian Kelley", "Bruce Simmons", "Caleb Ward",
    "Carl Fisher", "Carter Jordan", "Chad Howard", "Charles Hayes",
    "Chris Griffin", "Clarence Neal", "Cole Barker", "Colin Drake",
    "Connor Abbott", "Craig Hammond", "Curtis Stevenson", "Cyril Bates",
    "Damian Brady", "Damon Burke", "Dan Ryan", "Daniel Fleming",
    "Darren Doyle", "Dean Walton", "Dennis Arnold", "Derek Walsh",
    "Derrick Doyle", "Don Barrett", "Douglas Walton", "Dustin Max",
    "Dwight Reed", "Earl Hunter", "Edwin Pope", "Elias Dawson",
    "Elijah Jacobs", "Elliot Bowen", "Emmett Palmer", "Eric Gilbert",
    "Ethan Murray", "Eugene Marsh", "Felix Ray", "Francis Miles",
    "Frank Reese", "Fred Barton", "Gary Leonard", "Gavin Sullivan",
    "Gerald Vaughn", "Gilbert Benson", "Gordon Ramsey", "Grant Doyle",
    "Gregory Hale", "Harold Arnold", "Harrison Long", "Harry Wheeler",
    "Henry Perkins", "Howard Lyons", "Hunter McCarthy", "Ian Newman",
    "Isaac Coleman", "Ivan Schwartz", "Jack Warren", "Jackson Tyler",
    "Jacob Harrison", "James Webster", "Jason Douglas", "Jeffrey Bates",
    "Jerome Holt", "Jerry Curtis", "Jimmy Nichols", "Joe Barrett",
    "Joel Lawson", "John Bryant", "Jonah McCoy", "Jordan Briggs",
    "Joseph Hammond", "Joshua Abbott", "Juan Morales", "Julian Chavez",
    "Justin Herrera", "Keith Hale", "Kelvin Romero", "Kenneth Castillo",
    "Kevin Brooks", "Kyle Hoffman", "Lance Ramos", "Larry Houston",
    "Lawrence Harper", "Leon Bishop", "Lewis Elliott", "Logan Potter",
    "Louis Barrett", "Lucas Sherman", "Luis Franklin", "Malcolm Bishop",
    "Marcus Norton", "Mark Spencer", "Mason Fletcher", "Matthew Perez",
    "Maurice King", "Maxwell Holland", "Melvin Barrett", "Michael Webb",
    "Miguel Wells", "Miles Higgins", "Nathan Andrews", "Nicholas Ford",
    "Noah Jennings", "Norman Ruiz", "Oscar Jacobs", "Owen Barber",
    "Patrick Lowe", "Paul Sutton", "Peter Hansen", "Philip Greene",
    "Quincy Cruz", "Ralph Alvarez", "Randall Silva", "Raymond Torres",
    "Ricardo Gonzales", "Richard Flores", "Robert Griffith", "Rodney Dean",
    "Roger Ortiz", "Ronald Rivera", "Russell Lane", "Ryan Francis",
    "Samuel Bishop", "Scott Beck", "Sean Burke", "Seth Austin",
    "Shawn Myers", "Spencer Hunt", "Stephen Byrd", "Steven Harper",
    "Stuart Hampton", "Terence Perry", "Terrence Burns", "Theodore Murphy",
    "Thomas Hudson", "Timothy Fields", "Travis Jacobs", "Trevor Holmes",
    "Tristan Barber", "Troy Clayton", "Tyler Figueroa", "Victor Grant",
    "Vincent Lowe", "Walter Hughes", "Wayne Gonzalez", "William Turner",
    "Xavier Wells", "Zachary Sanchez"
    ]

    for i in range(place):
        abonnement = None
        a = random.randint(1,2)
        if a == 1:
            abonnement = True
        else :
            abonnement = False
        voiture = Voiture(imatriculation, random.choice(marques), random.choice(nom_proprio), abonnement)
        if abonnement :
            parking.Parking.abonnement(voiture)
            
        liste_voiture.append(voiture)
    
    return liste_voiture

print(generer_voiture_aleatoire())





