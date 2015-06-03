from PySide import QtGui, QtCore
from PySide.QtGui import *
import htmlmodule
import emailer
from subprocess import call


class RestartGuiException(Exception):
    pass


class Gui(QMainWindow):
    settings = QtCore.QSettings("Ericsson", "Connected PostBox GUI")
    emailRecipients = "example@example.com"
    shouldSendEmail = True
    shouldSendAppNotifications = True
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
        # h.addWidget(self.createButton("Send Mail"))
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
        w.hide()

        # Reset button
        w = self.createButton("Reset Settings")
        w.clicked.connect(self.resetSettings)
        w.hide()

        # Create toggle box
        self.createToggleBox("Notify with email", "shouldSendEmail")
        self.createToggleBox("Notify with app", "shouldSendAppNotifications")

        # Send notification button
        w = self.createButton("Send Notification")
        w.clicked.connect(self.sendPost)

        # Run button
        w = self.createButton("Run PostBox")
        w.clicked.connect(self.runPostBox)

    def runPostBox(self):
        # self.close()
        print("Run postbox!")
        call(["./maraiDiff.sh", ""])
        # raise RestartGuiException

    def createToggleBox(self, label, fieldName):
        def callback(state):
            setAttribute(fieldName, callback.outer, state, callback.outer.settings)

        c = callback
        c.outer = self
        c.fieldName = fieldName

        w = QCheckBox(label, self)
        state = getBoolAttribute(fieldName, self, self.settings)

        w.setChecked(state)
        w.toggled.connect(c)
        self.add(w)
        pass

    def resetSettings(self):
        self.settings.clear()
        self.close()
        # raise RestartGuiException

    def getRecipients(self):
        text = self.recipientsWidget.toPlainText()
        l = stringToList(text)
        return l

    def getServerUrl(self):
        text = self.serverWidget.text() + "/PostboxServer/api/v1/notification/notify"
        return text

    def sendPost(self):
        if self.shouldSendEmail:
            self.sendEmail()
        if self.shouldSendAppNotifications:
            self.sendAppNotification()

    def sendAppNotification(self):
        print("Sending app notification...")
        recipients = self.getRecipients()
        serverUrl = self.getServerUrl()

        htmlmodule.sendRecipientsAsPost(recipients, serverUrl)

    def sendEmail(self):
        print("Sending email notification...")
        recipients = self.getRecipients()
        emailer.sendToAll(recipients)


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


def getBoolAttribute(fieldName, object, settings):
    """Somehow booleans is stored as strings by default so special
    care is needed to convert string back to boolean."""
    # settings.setValue(fieldName, 0)
    state = getBoolFromString(settings.value(fieldName))
    if state is not None:
        setattr(object, fieldName, state)
    else:
        state = getattr(object, fieldName)
    return state


def getBoolFromString(string):
    if string == "true":
        return True
    return False