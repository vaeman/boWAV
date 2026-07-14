from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from backend.query_db import list_artists
from backend.models import Backend
import os
import sys
from backend.models import Backend

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()

    backend = Backend()
    engine.rootContext().setContextProperty("backend", backend)

    engine.load(os.path.join(BASE_DIR, "ui/main.qml"))
    sys.exit(app.exec())

if __name__ == "__main__":
    main()