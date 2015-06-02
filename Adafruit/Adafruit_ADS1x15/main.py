import sys
from gui import *

def runApp():
    gui = Gui()
    gui.sendPost()
    #sys.exit(app.exec_())


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    runApp()

