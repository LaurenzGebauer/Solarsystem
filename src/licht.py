__author__ = 'Laurenz'
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class licht(object):

    def light(self):
        """
        Klasse licht , ist für die Licht einstellungen der Planeten zuständig
        :return:
        """
        amb = (0.2, 0.2, 0.2, 1)
        diff = (1.0, 1.0, 1.0,1)
        spec = (0.5, 0.5, 0.5, 1)

        glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, amb)
        glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, spec)
        glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 15)

        glLightfv(GL_LIGHT0, GL_AMBIENT, amb)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, diff)
        glLightfv(GL_LIGHT0, GL_SPECULAR, spec)

        glLightfv(GL_LIGHT0, GL_POSITION, (0, 0.3, 1, 1))#Licht Postition
        glEnable(GL_LIGHT0)#aktiviert Licht
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK, GL_DIFFUSE)#bestimmt Materialeigenschaften
        glEnable(GL_NORMALIZE)
        glShadeModel(GL_SMOOTH)#Farbverlauf Eckpunkte
