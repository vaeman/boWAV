from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

app = QGuiApplication([])

engine = QQmlApplicationEngine()
engine.load("ui/main.qml")

app.exec()