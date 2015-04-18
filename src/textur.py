__author__ = 'Laurenz'
from PIL.Image import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class textur(object):

    def LoadTextures(pic):
        """
        Vearbeitung der Texutren
        :param pic: Der Namde der gewünschten Textur
        :return:  verarb. textur
        """

        image = open(pic)   #Sonnentextzur öffnen
        ix_s =image.size[0]
        iy_s =image.size[1]
        image=image.convert("RGBA").tostring("raw", "RGBA")
        textures = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D,textures)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix_s, iy_s, GL_RGBA, GL_UNSIGNED_BYTE, image)
        glEnable(GL_TEXTURE_2D)
        return textures
