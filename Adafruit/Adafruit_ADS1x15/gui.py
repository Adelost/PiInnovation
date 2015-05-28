from PySide import QtGui, QtCore
from PySide.QtGui import *
import htmlmodule
import ssl

class RestartGuiException(Exception):
    pass


class Gui(QMainWindow):
    settings = QtCore.QSettings("Ericsson", "Connected PostBox GUI")
    emailRecipients = "example@example.com"
    serverUrl = "https://postbox-piinnovation.rhcloud.com/PostboxServer/api/v1/notification/notify"

    def __init__(self):
        super(Gui, self).__init__()
        self.recipientsWidget = None
        self.serverWidget = None

        w = QWidget()
        self.layout = QVBoxLayout(self)
        w.setLayout(self.layout)
        self.setCentralWidget(w)

        self.intiUi()

        # m = QMenuBar()
        # self.setMenuBar(w)

        self.setWindowTitle('Connected PostBox GUI')
        self.setGeometry(300, 300, 320, 450)
        self.resize(self.minimumSizeHint())
        self.show()

    def createButton(self, label):
        w = QPushButton(label, self)
        self.layout.addWidget(w)
        return w

    def add(self, widget):
        l = self.layout
        if isinstance(widget, QLayout):
            l.addLayout(widget)
        else:
            l.addWidget(widget)
        return widget

    def intiUi(self):
        # Mail
        self.add(QLabel("Recipient emails (separate with new line):"))
        w = QPlainTextEdit()
        text = getAttribute("emailRecipients", self, self.settings)
        w.setPlainText(text)
        self.add(w)
        self.recipientsWidget = w

        def callbackSetRecipients():
            text = callbackSetRecipients.edit.toPlainText()
            setAttribute("emailRecipients", callbackSetRecipients.outer, text, callbackSetRecipients.outer.settings)

        c = callbackSetRecipients
        c.outer = self
        c.edit = w
        w.textChanged.connect(c)

        h = QHBoxLayout()
        h.addWidget(self.createButton("Send Mail"))
        self.add(h)

        # Post
        self.add(QLabel("Server address:"))
        w = QLineEdit()
        text = getAttribute("serverUrl", self, self.settings)
        w.setText(text)
        self.add(w)
        self.serverWidget = w

        def callbackSetServer(text):
            setAttribute("serverUrl", callbackSetServer.outer, text, callbackSetServer.outer.settings)

        c = callbackSetServer
        c.outer = self
        w.textChanged.connect(c)

        w = self.createButton("Send POST")
        w.clicked.connect(self.sendPost)
        self.add(w)

        # Reset button
        w = self.createButton("Reset Settings")
        w.clicked.connect(self.resetSettings)

    def resetSettings(self):
        self.settings.clear()
        self.close()
        # raise RestartGuiException

    def getRecipients(self):
        text = self.recipientsWidget.toPlainText()
        l = stringToList(text)
        return l

    def getServerUrl(self):
        text = self.serverWidget.text()
        return text

    def sendPost(self):
        recipients = self.getRecipients()
        serverUrl = self.getServerUrl()

        htmlmodule.sendRecipientsAsPost(recipients, serverUrl)

    def sendEmail(self):
        recipients = self.getRecipients()

        emailer.sendRecipientsAsPost(recipients, serverUrl)


def setAttribute(fieldName, object, value, settings):
    setattr(object, fieldName, value)
    settings.setValue(fieldName, value)


def stringToList(string):
    l = string.split("\n")
    return l


def getAttribute(fieldName, object, settings):
    """Loads the attribute from settings or uses default one."""
    # settings.setValue(fieldName, 0)
    state = settings.value(fieldName)
    if state is not None:
        setattr(object, fieldName, state)
    else:
        state = getattr(object, fieldName)
    return state
