import sys
import os

# Add the absolute path of the SoulSync directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from PyQt5.QtWidgets import QApplication
from view.calculator_view import CalculatorView



def main():
    """Entry point of the application, initializing the login window."""

    app = QApplication(sys.argv)
    window = CalculatorView()

    window.exec_()


if __name__ == '__main__':
    main()