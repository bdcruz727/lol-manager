from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LCK Franchise Sim")
        self.resize(1280, 720)

        self.label = QLabel("Welcome to the League Simulator")
        self.sim_button = QPushButton("Simulate Match")
        self.sim_button.clicked.connect(self.simulate_match)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.sim_button)
        self.setLayout(layout)

    def simulate_match(self):
        self.label.setText("Blue Team defeats Red Team!")