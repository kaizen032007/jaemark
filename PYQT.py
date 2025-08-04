import sys
import random
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QVBoxLayout, QHBoxLayout, QScrollArea, QFrame, QMessageBox,
    QSpacerItem, QSizePolicy
)
from PyQt5.QtGui import QPixmap, QFont, QColor
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Perpetual Help College of Manila")
        self.setGeometry(300, 300, 500, 200)
        self._build_ui()

    def _build_ui(self):
        # Main container
        container = QWidget()
        self.setCentralWidget(container)
        main_layout = QHBoxLayout(container)

        # ── Sidebar ──────────────────────────────────────────────────────────
        sidebar = QFrame()
        sidebar.setStyleSheet("background: gold;")
        sidebar.setFixedWidth(250)
        sb_layout = QVBoxLayout(sidebar)
        sb_layout.setContentsMargins(10, 10, 10, 10)
        sb_layout.setSpacing(10)

        for name, callback in [
            ("Registration", self.on_registration),
            ("Admissions", self.on_admissions),
            ("About Us", self.on_about),
            ("Reservations", self.on_reservations),
        ]:
            btn = QPushButton(name)
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("background: royalblue; color: gold; font-weight: bold;")
            btn.clicked.connect(callback)
            sb_layout.addWidget(btn)

        sb_layout.addStretch()
        contact = QLabel("Contact us\nPhone: 09123456789\nEmail: PerpetualHelp@Upshl.edu.ph")
        contact.setStyleSheet("color: gold; background: royalblue; padding: 10px;")
        sb_layout.addWidget(contact)

        main_layout.addWidget(sidebar)

        # ── Content Area ─────────────────────────────────────────────────────
        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        # Header
        header = QFrame()
        header.setStyleSheet("background: royalblue;")
        header.setFixedHeight(100)
        h_layout = QHBoxLayout(header)
        logo = QLabel("PERPETUAL HELP COLLEGE OF MANILA")
        logo.setStyleSheet("color: gold;")
        logo.setFont(QFont("Arial", 24, QFont.Bold))
        h_layout.addWidget(logo)
        h_layout.addStretch()
        self.clock = QLabel()
        self.clock.setStyleSheet("background: gold; color: red;")
        self.clock.setFont(QFont("Arial", 24, QFont.Bold))
        h_layout.addWidget(self.clock)
        content_layout.addWidget(header)
        self._start_clock()

        # Scrollable middle
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        mid = QWidget()
        mid_layout = QVBoxLayout(mid)
        mid_layout.setAlignment(Qt.AlignTop)

        # Placeholder images
        for img_path, x, y in [
            ("schoolbuilding.png", 0, 0),
            ("sampleperps1.png", 0, 0),
            ("sampleperps3.png", 0, 0),
        ]:
            lbl = QLabel()
            try:
                pix = QPixmap(img_path).scaledToWidth(600, Qt.SmoothTransformation)
                lbl.setPixmap(pix)
            except:
                lbl.setText(f"[Missing {img_path}]")
            lbl.setContentsMargins(5,5,5,5)
            mid_layout.addWidget(lbl)

        scroll.setWidget(mid)
        content_layout.addWidget(scroll)

        # Bottom bar
        bottom = QFrame()
        bottom.setStyleSheet("background: royalblue;")
        bottom.setFixedHeight(200)
        b_layout = QHBoxLayout(bottom)
        b_layout.setContentsMargins(20, 10, 20, 10)
        b_layout.setSpacing(40)

        programs = [
            "NURSING", "COMPUTER SCIENCE", "INFORMATION TECHNOLOGY",
            "PHYSICAL THERAPY", "RADIOLOGY TECHNOLOGY",
            "BUSINESS ADMINISTRATION", "MEDICAL TECHNOLOGY",
            "CYBERSECURITY", "ARCHITECTURE", "MARINE TRANSPORTATION"
        ]
        for idx, prog in enumerate(programs, 1):
            frame = QVBoxLayout()
            lbl = QLabel(f"{idx}. {prog}")
            lbl.setStyleSheet("color: blue; background: gold;")
            lbl.setFont(QFont("Arial", 12, QFont.Bold))
            btn = QPushButton("CHECK TUITION")
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("background: white; color: blue;")
            frame.addWidget(lbl)
            frame.addWidget(btn)
            b_layout.addLayout(frame)

        content_layout.addWidget(bottom)

        main_layout.addWidget(content)

    def _start_clock(self):
        from PyQt5.QtCore import QTimer, QTime
        timer = QTimer(self)
        timer.timeout.connect(lambda: self.clock.setText(QTime.currentTime().toString("hh:mm:ss AP")))
        timer.start(1000)

    # ── Stub callbacks ───────────────────────────────────────────────────────
    def on_registration(self):
        QMessageBox.information(self, "Registration", "Open Registration Window")

    def on_admissions(self):
        QMessageBox.information(self, "Admissions", "Open Admissions Window")

    def on_about(self):
        QMessageBox.information(self, "About Us", "Open About Us Window")

    def on_reservations(self):
        QMessageBox.information(self, "Reservations", "Open Reservations Window")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
