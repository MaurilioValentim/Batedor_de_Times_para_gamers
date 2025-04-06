from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QLabel
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt
import sys

class SorteadorDeEquipes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sorteador de Equipes - Gamer Edition")
        self.setGeometry(100, 100, 1360, 768)  # Tamanho inicial da janela
        self.setStyleSheet("background-color: #1e1e1e;")  # Cor do fundo da janela
        self.initUI()

    def initUI(self):
        # Botão que exibe o frame
        self.btn_exibir = QPushButton("Clique Aqui!", self)
        self.btn_exibir.setGeometry(10, 10, 150, 50)
        self.btn_exibir.setStyleSheet("""
            QPushButton {
                background-color: #5d5dfa;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #4646c4;
            }
        """)
        self.btn_exibir.clicked.connect(self.exibir_frame)

        # Label inicial
        self.label_resultado = QLabel("", self)
        self.label_resultado.setStyleSheet("color: #ffffff; font-size: 18px;")
        self.label_resultado.setGeometry(10, 70, 300, 40)

    def exibir_frame(self):
        # Frame dinâmico
        self.frame = QFrame(self)
        self.frame.setGeometry(200, 20, 1000, 700)  # Tamanho e posição do frame
        self.frame.setStyleSheet("""
            QFrame {
                background-color: #2b2b2b;
                border: 2px solid #5d5dfa;
                border-radius: 15px;
            }
        """)
        self.frame.show()

        # Texto dentro do frame
        label_frame = QLabel("Bem-vindo ao frame dinâmico!", self.frame)
        label_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_frame.setGeometry(50, 50, 800, 100)
        label_frame.setStyleSheet("color: #ffffff; font-size: 24px; font-weight: bold;")

        # Botão dentro do frame
        btn_frame = QPushButton("Fechar", self.frame)
        btn_frame.setGeometry(400, 600, 100, 50)
        btn_frame.setStyleSheet("""
            QPushButton {
                background-color: #fa5d5d;
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #c44646;
            }
        """)
        btn_frame.clicked.connect(self.fechar_frame)

    def fechar_frame(self):
        self.frame.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SorteadorDeEquipes()
    window.show()
    sys.exit(app.exec())
