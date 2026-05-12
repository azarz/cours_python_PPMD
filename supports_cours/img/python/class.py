class Rectangle:

    def __init__(self, longueur=1, largeur=1):
        self.longueur = longueur
        self.largeur = largeur
        self.surface = self.longueur*self.largeur
		
    def getLongueur(self):
        return self.longueur
		
    def setLongueur(self, longueur):
        self.longueur = longueur


    def doubler(self):
        self.longueur = 2*self.longueur
        self.largeur = 2*self.largeur
		

rectangle = Rectangle()
rectangle.getLongueur()
>> 1
rectangle.largeur
>> 1
rectangle.setLongueur(2)
rectangle.longueur
>> 2
rectangle = Rectangle(3,2)
rectangle.doubler()
rectangle.largeur
>> 6



