import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel)
from PySide6.QtCore import Qt, QTimer


# Main window: UI and user interaction
class CountdownApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown Timer")
        self.setFixedSize(230, 250)
        self.remaining_seconds = 60
        self.timer = QTimer()
        self.create_widgets()
        self.setup_layout()
        self.setup_connections()
    
    def format_time(self, seconds):
        minutes = seconds // 60 
        seconds_part = seconds % 60
        formatted_time = f"{minutes:02d}:{seconds_part:02d}"
        return formatted_time
    
    def update_countdown(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            formatted_time = self.format_time(self.remaining_seconds)
            self.time_label.setText(formatted_time)

            if self.remaining_seconds == 0:
                self.timer.stop()
                self.welcome_label.setText("Time is up!")
                self.start_button.setEnabled(True)
                self.stop_button.setEnabled(False)
        
    def start_countdown(self):
        if self.timer.isActive():
            return

        if self.remaining_seconds == 0:
            self.remaining_seconds = 60
            formatted_time = self.format_time(self.remaining_seconds)
            self.time_label.setText(formatted_time)
            self.welcome_label.setText("Welcome to my app")

        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.timer.start(1000)

    
    def stop_countdown(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    
    # Create UI widgets
    def create_widgets(self):
        self.welcome_label = QLabel("Welcome to my app")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.time_label = QLabel(self.format_time(self.remaining_seconds))
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 36px")
        self.start_button = QPushButton(text="Start")
        self.start_button.setFixedWidth(120)
        self.stop_button = QPushButton(text="Stop")
        self.stop_button.setEnabled(False)
        self.stop_button.setFixedWidth(120)
        
    # Arrange widgets on the window
    def setup_layout(self):
        main_layout = QVBoxLayout()
        buttons_layout = QVBoxLayout()
        main_layout.addWidget(self.welcome_label)
        main_layout.addWidget(self.time_label)
        main_layout.addSpacing(25)
        main_layout.setAlignment(Qt.AlignCenter)
        main_layout.setSpacing(5)
        buttons_layout.addWidget(self.start_button, alignment=Qt.AlignCenter)
        buttons_layout.addWidget(self.stop_button, alignment=Qt.AlignCenter)
        buttons_layout.setSpacing(0)
        main_layout.addLayout(buttons_layout)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)


    # Connect buttons to functions
    def setup_connections(self):
        self.timer.timeout.connect(self.update_countdown)
        self.start_button.clicked.connect(self.start_countdown)
        self.stop_button.clicked.connect(self.stop_countdown)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CountdownApp()
    window.show()

    sys.exit(app.exec())
