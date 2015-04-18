__author__ = 'Laurenz'
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

class planet(object):
    """
    In der Klasse planet werden die Unterschiedlichen Planeten erstellt
    """

    def __init__(self):
        """
        Konstruktor initialisiert Attribute
        :return:
        """
        self.yplanet=0.0
        self.yplanet1=0.0
        self.rot=0.0

    def Planet_Erde(self,radius,x,y,z,angle1,txt):
        """
        Erstellung Planet Erde
        :param radius:  Radius des Planetens
        :param x:       x Koordinate
        :param y:       y Koordinate
        :param z:       z Koordinate
        :param angle:   Geschwindigkeit
        :param txt:     Textur
        :return:
        """

        glLoadIdentity() #Ersetzt die aktuelle Matrix durch die Einheitsmatrix
        self.yplanet=self.yplanet+angle1 #Geschw.
        glRotatef( self.yplanet, 0,1,0)
        glTranslate(x,y,z)
        glBindTexture(GL_TEXTURE_2D,txt)
        quadratic = gluNewQuadric() #Quadratische Textur
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)
        gluSphere(quadratic,radius, 32,32)  #Planet mit der Textur


    def Planet_Lava(self,radius,x,y,z,angle,txt):
        """
        Methode für den Planeten Mars (Lava)
        :param radius:   Radius des Planetens
        :param x:        x Koordinate
        :param y:        y Koordinate
        :param z:        z Koordinate
        :param angle:    Geschwindigkeit
        :param txt:      Textur
        :return:
        """

        glLoadIdentity()
        self.yplanet1=self.yplanet1+angle
        glRotate( self.yplanet1, 0,1,0)
        glTranslate(x,y,z)
        glBindTexture(GL_TEXTURE_2D,txt)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)
        gluSphere(quadratic,radius, 32,32)


    def DrawGLScene_Sonne(self,radius,x,y,z,angle,txt):
        """
        Methode für den Zentralstern
        :param radius:  Radius des Planetens
        :param x:       x Koordinate
        :param y:       y Koordinate
        :param z:       z Koordinate
        :param txt:     Textur
        :return:
        """

        glLoadIdentity()#Ersetzt die aktuelle Matrix durch die Einheitsmatrix
        glTranslatef(x, y, z)
        self.rot=self.rot+angle
        glRotate( self.rot, 0,1,0)
        glBindTexture(GL_TEXTURE_2D,txt)
        quadratic = gluNewQuadric()
        gluQuadricNormals(quadratic, GLU_SMOOTH)
        gluQuadricTexture(quadratic, GL_TRUE)
        gluSphere(quadratic,radius, 32,32)










