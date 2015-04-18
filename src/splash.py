__author__ = 'Laurenz'

import tkinter
import time


class splash(object):
    """
    Die Klasse ist für den Screen Zuständig
    """

    def __init__(self, root, file, wait):
        """
        Der Konstruktor initialisiert die Attribute
        :param root: Libary
        :param file: Das Foto das als Splashscreen verwendet wird
        :param wait: Zeit die der Splashscreen angezeigt wird
        :return:
        """
        self.__root = root
        self.__file = file
        self.__wait = wait + time.clock()

    def __enter__(self):
        """
        Einstellungen beim Starten der Applikation
        :return:
        """
        #Behindert das eig Programm
        self.__root.withdraw()

        # Komponenten
        window = tkinter.Toplevel(self.__root)
        canvas = tkinter.Canvas(window)
        splash = tkinter.PhotoImage(master=window, file=self.__file)

        # Bildeinstellungen
        scrW = window.winfo_screenwidth()
        scrH = window.winfo_screenheight()
        # größe
        imgW = splash.width()
        imgH = splash.height()
        # Position
        Xpos = (scrW - imgW) // 2
        Ypos = (scrH - imgH) // 2

        # Configure the window showing the logo.
        window.overrideredirect(True)
        window.geometry('+{}+{}'.format(Xpos, Ypos))
        # Setup canvas on which image is drawn.
        canvas.configure(width=imgW, height=imgH, highlightthickness=0)
        canvas.grid()
        # Show the splash screen on the monitor.
        canvas.create_image(imgW // 2, imgH // 2, image=splash)
        window.update()
        # Save the variables for later cleanup.
        self.__window = window
        self.__canvas = canvas
        self.__splash = splash

    def __exit__(self):
        """
        Wenn der Timer endet , wird Fenster neu erstellt
        :return:
        """

        now = time.clock()#Timer
        if now < self.__wait:
            time.sleep(self.__wait - now)
        del self.__splash
        self.__canvas.destroy()
        self.__window.destroy()
        # Übergang zum eig Programm
        self.__root.update_idletasks()
        self.__root.deiconify()