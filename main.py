import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LoL Esports Sim with PyQt6")
        self.resize(800,600)

        self.label = QLabel("Click to simulate a match")
        self.button = QPushButton("Simulate Match")
        self.button.clicked.connect(self.simulate_match)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def simulate_match(self):
        self.label.setText("Blue Team Defeats Red Team!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())