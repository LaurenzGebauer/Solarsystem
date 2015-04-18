__author__ = 'Laurenz'
from solar.planet import *

class geschw():
    """
    In der Klasse geschw() wird die Geschwindigkeits der Rotationen der Planeten bei Tastatur betätigung übernommen und geändert
    """
    def __init__(self):
        """
        Konstruktor
        :return:
        """
        planet.__init__(self)

    def stopp(self):
        """
        Stopp die Animation
        :return:
        """
        planet.DrawGLScene_Sonne(self,0.2,0.0,0.0,0.0,0.0,self.sonne)# durchmesser,x,y,z,geschwindigkeit,textur
        planet.Planet_Erde(self, 0.1, 0.8, 0.0, 0.0,0.0, self.erde)
        planet.Planet_Erde(self, 0.03, 1, 0.0, 0.0,0,self.mond)
        planet.Planet_Lava(self, 0.1, 1.5, -0.3, 0.5, 0.0, self.lava)

    def schneller(self):
        """
        Mach die Animation schneller
        :return:
        """
        planet.DrawGLScene_Sonne(self,0.2,0.0,0.0,0.0,0.01+self.geschwindigkeit,self.sonne)
        planet.Planet_Erde(self, 0.1, 0.8, 0.0, 0.0,0.03+self.geschwindigkeit, self.erde)
        planet.Planet_Erde(self, 0.03, 1, 0.0, 0.0,0+self.geschwindigkeit,self.mond)
        planet.Planet_Lava(self, 0.1, 1.5, -0.3, 0.5, 0.02+self.geschwindigkeit, self.lava)

    def langsam(self):
        """
        Macht die Animation langsamer
        :return:
        """
        planet.DrawGLScene_Sonne(self,0.2,0.0,0.0,0.0,0.01-self.geschwindigkeit,self.sonne)
        planet.Planet_Erde(self, 0.1, 0.8, 0.0, 0.0,0.03-self.geschwindigkeit, self.erde)
        planet.Planet_Erde(self, 0.03, 1, 0.0, 0.0,0-self.geschwindigkeit,self.mond)
        planet.Planet_Lava(self, 0.1, 1.5, -0.3, 0.5, 0.02-self.geschwindigkeit, self.lava)

