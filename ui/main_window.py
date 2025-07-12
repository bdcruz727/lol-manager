from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QComboBox, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer
from scripts.simulation import simulate_match
from scripts.team import get_team_roster
from scripts.team import get_team_rating

team_names = ["T1", "Gen.G"]

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LCK Franchise Sim")
        self.setFixedSize(1280, 720)

        # Title label
        self.label = QLabel("LCK Franchise Simulator")
        self.label.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignCenter)  # ✅ This centers the text

        # Team selectors
        self.team1_box = QComboBox()
        self.team1_box.setFixedSize(200, 40)

        #Team 1 Player Layout
        self.team1_players = [QLabel() for _ in range(5)]
        self.team1_overall_label = QLabel()
        self.team1_overall_label.setStyleSheet("font-size: 18px; font-weight: bold;")


        #Team 2 Player Layout
        self.team2_box = QComboBox()
        self.team2_players = [QLabel() for _ in range(5)]
        self.team2_overall_label = QLabel()
        self.team2_overall_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.team2_box.setFixedSize(200, 40)
        
        self.team1_box.addItems(team_names)
        self.team1_box.setCurrentIndex(0)
        self.team2_box.addItems(team_names)
        self.team2_box.setCurrentIndex(1)

        self.team1_box.currentTextChanged.connect(self.update_roster)
        self.team2_box.currentTextChanged.connect(self.update_roster)
        

        team1_label = QLabel("Team 1")
        team1_label.setStyleSheet("font-size: 32px; font-weight: bold;")
        team2_label = QLabel("Team 2")
        team2_label.setStyleSheet("font-size: 32px; font-weight: bold;")

        # Layout for team selectors side-by-side
        team_selector_layout = QHBoxLayout()
        
        left_layout = QVBoxLayout()
        left_layout.addWidget(team1_label)
        left_layout.addWidget(self.team1_box)
        for label in self.team1_players:
            label.setStyleSheet("font-size: 16px;")
            left_layout.addWidget(label)
        left_layout.addWidget(self.team1_overall_label)
        

        right_layout = QVBoxLayout()
        right_layout.addWidget(team2_label)
        right_layout.addWidget(self.team2_box)
        for label in self.team2_players:
            label.setStyleSheet("font-size: 16px;")
            right_layout.addWidget(label)
        right_layout.addWidget(self.team2_overall_label)

        team_selector_layout.addLayout(left_layout)
        team_selector_layout.addStretch()
        team_selector_layout.addLayout(right_layout)

        # Simulate button
        self.sim_button = QPushButton("Simulate Match")
        self.sim_button.clicked.connect(self.handle_simulation)
        self.sim_button.setFixedSize(200,40)
      

        # Main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addLayout(team_selector_layout)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.sim_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)
        self.update_roster()
    
    def handle_simulation(self):
        team1 = self.team1_box.currentText()
        team2 = self.team2_box.currentText()
        if team1 == team2:
            self.sim_button.setText("Please select different teams!")
            QTimer.singleShot(2000, lambda: self.sim_button.setText("Simulate Match"))
            QTimer.singleShot(2000, lambda: self.sim_button.clicked.connect(self.handle_simulation))
            return
        
        self.sim_button.setEnabled(False)
        self.sim_button.setText("Simulating...")
        QTimer.singleShot(2000, lambda:simulate_match(team1, team2, self))
        QTimer.singleShot(2000, lambda: self.sim_button.setText("Simulation Complete!"))
        QTimer.singleShot(4000, lambda: self.sim_button.setText("Simulate Match"))
        QTimer.singleShot(4000, lambda: self.sim_button.setEnabled(True))
        
    def update_roster(self):
        team1 = self.team1_box.currentText()
        team2 = self.team2_box.currentText()

        team1_roster = get_team_roster(team1)
        team2_roster = get_team_roster(team2)

        team1_rating = get_team_rating(team1)
        team2_rating = get_team_rating(team2)

        for i in range(5):
            self.team1_players[i].setText(team1_roster[i])
            self.team2_players[i].setText(team2_roster[i])
        
        self.team1_overall_label.setText(f"{team1} Overall: {team1_rating}")
        self.team2_overall_label.setText(f"{team2} Overall: {team2_rating}")


    