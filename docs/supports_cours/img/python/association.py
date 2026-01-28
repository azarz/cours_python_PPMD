class Couleur:

    def __init__(self, nom):
	    self.nom = nom
	    self.rectangles = []

class Rectangle:

    def __init__(self, couleur, longueur=1, largeur=1):
        self.longueur = longueur
        self.largeur = largeur
        self.surface = self.longueur*self.largeur
        self.couleur = couleur
        couleur.rectangles.append(self)

    def getCouleur(self):
        return self.couleur.nom
		

couleur = Couleur('jaune')
couleur.nom
>> 'jaune'
rectangle = Rectangle(couleur)
rectangle.getCouleur()
>> 'jaune'
couleur.rectangles
>> [<__main__.Rectangle object at 0x00000000037D3128>]
