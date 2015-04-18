__author__ = 'Laurenz'
from solar.planet import *
from solar.textur import *
from solar.licht import *
from solar.geschw import *
from solar.splash import *


class sonnensystem():
    """
    Sonnensystem ist der Controller der Klasse hier werden alle wichtigen Methoden aufgerufen.
    """
    def __init__(self):
        """
        Konstruktor initialisiert Attribute
        :return:
        """
        self.sonne = None
        self.erde = None
        self.mond = None
        self.light=True
        self.bol=True
        self.stateT=True
        self.stateL=True
        self.schnell=True
        self.geschwindigkeit=0.001
        self.langsam=True
        self.stop=True

        planet.__init__(self)
        textur.__init__(self)
        licht.__init__(self)
        geschw.__init__(self)


    def InitGL(self, Width, Height):
        """
        Hier werden die Texturen den Attributen zugewiesen
        :param Width:Breite des Fensters
        :param Height:Hoehe des Fensters
        :return:
        """
        self.sonne = textur.LoadTextures("./sonne.jpg") #Texturen werden geladen
        self.erde = textur.LoadTextures("./erde.jpg")
        self.mond = textur.LoadTextures("./mond.jpg")
        self.lava = textur.LoadTextures("./lava.jpg")

        glClearColor(0.0, 0.0,0.0, 0.0) #Setzt farbe fürs Zerücksetzten
        glEnable(GL_DEPTH_TEST)
        licht.light(self)



    def screen(self):
        """
        Die Methode gibt alle Planeten aus und ruft die camUpdate Methode auf
        :return:
        """
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity() #Setzt Matrix zurück
        sonnensystem.camUpdate(self)#Aufruf Für Kamera perspektive
        glPushMatrix() #Clean

        if self.schnell is False: #Überwacht Geschw.
            geschw.schneller(self)

        elif self.langsam is False:
            geschw.langsam(self)

        elif self.stop is False:
            geschw.stopp(self)

        elif self.stop is True:
            planet.DrawGLScene_Sonne(self,0.2,0.0,0.0,0.0,0.01,self.sonne)
            planet.Planet_Erde(self, 0.1, 0.8, 0.0, 0.0,0.03, self.erde)
            planet.Planet_Erde(self, 0.03, 1, 0.0, 0.0,0,self.mond)
            planet.Planet_Lava(self, 0.06, 1.5, -0.3, 0.5, 0.015, self.lava)

        glPopMatrix()
        glutSwapBuffers()

    def camUpdate(self):
        """
        Methode zum Ändern der Perpektive
        :return:
        """
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, float(640) / float(480), 0.1, 100.0) #Perspektive

        if self.bol is False: #Unterschiedliche Perspektive
            gluLookAt(0,5,1,0, 0, 0,0,1, 0)

        elif self.bol is True:
            gluLookAt(0,0,4,0, 0, 0,0,1, 0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def keyPressed(self,key, x, y):
        """
        Tasten Listener
        :param key: Taste
        :param x:
        :param y:
        :return:
        """

        #Cam
        if key == b'c':
            if self.bol is True:
                self.bol= False
            elif self.bol is False:
                self.bol= True
                self.stateC=True

        #Schneller
        if key == b'm':
           self.schnell=False
           self.geschwindigkeit=self.geschwindigkeit+0.01

        #Langsamer
        if key == b'n':
           self.langsam=False
           self.geschwindigkeit=self.geschwindigkeit-0.01

        #Stop
        if key == b' ':
            if self.stop is True:
                self.stop=False
                self.schnell=True
                self.langsam=True
            elif self.stop is False:
                self.stop=True
                self.schnell=False
                self.langsam=False

    def mouse(self,button, state, x, y):
        """
        Maus Überwachung
        :param button: Maustaste
        :param state: Status
        :param x:
        :param y:
        :return:
        """

        #Linke Maus - Licht an
        if self.stateL is True:
            if (button==GLUT_LEFT_BUTTON):
                if state == GLUT_DOWN:
                    glEnable(GL_LIGHTING)
                    self.stateL=False

        #Linke Maus - Licht aus
        elif self.stateL is False:
            if (button==GLUT_LEFT_BUTTON):
                if state == GLUT_DOWN:
                    glDisable(GL_LIGHTING)
                    self.stateL=True

        #Rechte Maus - Texture Einschalten
        if self.stateT is True:
            if (button==GLUT_RIGHT_BUTTON):
                if state == GLUT_DOWN:
                    glEnable(GL_TEXTURE_2D)
                    self.stateT=False

        #Rechte Maus - Textur ausschalten
        elif self.stateT is False:
            if (button==GLUT_RIGHT_BUTTON):
                if state == GLUT_DOWN:
                    glDisable(GL_TEXTURE_2D)
                    self.stateT=True

    def main(self):
        """
        Main Methode ruft alle Methoden auf
        :return:
        """
        root=tkinter.Tk()  #Splashscreen
        sp=splash(root, 'galaxy.gif',1) #Splah Klasse , root, texture , timer
        sp.__enter__()
        sp.__exit__()

        root.iconify()
        root.deiconify()
        root.destroy()

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(860, 540) #Fenstergröße
        window = glutCreateWindow(b'test')
        glutIdleFunc(self.screen)
        glutKeyboardFunc(self.keyPressed)
        glutMouseFunc(self.mouse)
        self.InitGL(640, 480) #Fenstergröße
        glutMainLoop()

t = sonnensystem()
t.main()



