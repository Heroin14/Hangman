from PyQt4 import QtCore, QtGui
import sys
from hangman import *

class Game(QtGui.QWidget):
    def __init__(self):
        super(Game, self).__init__()
        self.UIstart()
    def UIstart(self):
        self.setWindowTitle("Hangman")
        self.setWindowIcon(QtGui.QIcon("hangmanicon.png"))
        self.show()



def main():
    app= QtGui.QApplication(sys.argv)
    game= Game()

    sys.exit(app.exec_())



if __name__=='__main__':
    main()
