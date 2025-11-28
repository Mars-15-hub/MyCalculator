import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt5 import uic
from PyQt5.QtWidgets import *
from controller.calculator_controller import CalculatorController

class CalculatorView(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(os.path.join(os.path.dirname(__file__), "UI", "calculator.ui"), self)
        self.controller = CalculatorController()
        
        # Basic calculator buttons
        self.zero = self.findChild(QPushButton, "zero_btn")
        self.one = self.findChild(QPushButton, "one_btn")
        self.two = self.findChild(QPushButton, "two_btn")
        self.three = self.findChild(QPushButton, "three_btn")
        self.four = self.findChild(QPushButton, "four_btn")
        self.five = self.findChild(QPushButton, "five_btn")
        self.six = self.findChild(QPushButton, "six_btn")
        self.seven = self.findChild(QPushButton, "seven_btn")
        self.eight = self.findChild(QPushButton, "eight_btn")
        self.nine = self.findChild(QPushButton, "nine_btn")
        self.point = self.findChild(QPushButton, "point_btn")
        self.leftbracket = self.findChild(QPushButton, "leftbracket_btn")
        self.rightbracket = self.findChild(QPushButton, "rightbracket_btn")
        self.percent = self.findChild(QPushButton, "percent_btn")
        self.plus = self.findChild(QPushButton, "plus_btn")
        self.minus = self.findChild(QPushButton, "minus_btn")
        self.times = self.findChild(QPushButton, "times_btn")
        self.divide = self.findChild(QPushButton, "divide_btn")
        self.equals = self.findChild(QPushButton, "equals_btn")
        self.backspace_btn = self.findChild(QPushButton, "backspace_btn")
        self.clear_btn = self.findChild(QPushButton, "clear_btn")
        self.negate = self.findChild(QPushButton, "negate_btn")
        
        self.user_input = self.findChild(QLineEdit, "userInput")
        
        self.equals_clicked = 0
        self.res = ''
        
        self.zero.clicked.connect(self.add_zero)
        self.one.clicked.connect(self.add_one)
        self.two.clicked.connect(self.add_two)
        self.three.clicked.connect(self.add_three)
        self.four.clicked.connect(self.add_four)
        self.five.clicked.connect(self.add_five)
        self.six.clicked.connect(self.add_six)
        self.seven.clicked.connect(self.add_seven)
        self.eight.clicked.connect(self.add_eight)
        self.nine.clicked.connect(self.add_nine)
        
        self.plus.clicked.connect(self.add_plus)
        self.minus.clicked.connect(self.add_minus)
        self.times.clicked.connect(self.add_times)
        self.divide.clicked.connect(self.add_divide)
        self.percent.clicked.connect(self.add_percent)
        self.point.clicked.connect(self.add_point)
        
        self.leftbracket.clicked.connect(self.left_bracket)
        self.rightbracket.clicked.connect(self.right_bracket)
        
        self.backspace_btn.clicked.connect(self.backspace)
        self.clear_btn.clicked.connect(self.clear_input)
        
        self.equals.clicked.connect(self.result_view)
        
        self.negate.clicked.connect(self.add_negate)
        
    def add_zero(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("0")
            elif self.res != '':
                self.user_input.setText("0")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("0")
        
    def add_one(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("1")
            elif self.res != '':
                self.user_input.setText("1")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("1")
        
    def add_two(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("2")
            elif self.res != '':
                self.user_input.setText("2")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("2")
    
    def add_three(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("3")
            elif self.res != '':
                self.user_input.setText("3")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("3")
    
    def add_four(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("4")
            elif self.res != '':
                self.user_input.setText("4")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("4")
    
    def add_five(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("5")
            elif self.res != '':
                self.user_input.setText("5")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("5")
    
    def add_six(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("6")
            elif self.res != '':
                self.user_input.setText("6")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("6")
        
    def add_seven(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("7")
            elif self.res != '':
                self.user_input.setText("7")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("7")
        
    def add_eight(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("8")
            elif self.res != '':
                self.user_input.setText("8")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("8")
        
    def add_nine(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == "0":
                self.user_input.setText("9")
            elif self.res != '':
                self.user_input.setText("9")
                self.equals_clicked = 0
                self.res = ''
            else:
                self.user_input.insert("9")
        
    def add_plus(self):
        if len(self.user_input.text()) < 14 and self.user_input.text() != '':
            self.user_input.insert("+")
        
        
    def add_minus(self):
        if len(self.user_input.text()) < 14 and self.user_input.text() != '':
                self.user_input.insert("−")
        
    
    def add_times(self):
        if len(self.user_input.text()) < 14 and self.user_input.text() != '':
            
                self.user_input.insert("×")
        

        # add the last digit that was previously added, to the answer when the user presses equals to again
        # count the times number of equals to is clicked
    def add_divide(self):
        if len(self.user_input.text()) < 14 and self.user_input.text() != '':
            
                self.user_input.insert("÷")
        
        
    def add_percent(self):
        if len(self.user_input.text()) < 14 and self.user_input.text() != '':
            self.user_input.insert("%")
        
    def add_point(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == '':
                self.user_input.insert("0.")
            else:
                self.user_input.insert(".")
            
    def add_negate(self):
        if len(self.user_input.text()) < 14:
            if self.user_input.text() == '':
                self.user_input.insert("(−")
            else:
                index = 0
                input = self.user_input.text()
                input_substr = ''
                boolean = False
                for i in range(len(input)-1, 0, -1):
                    if input[i] == '+' or input[i] == '−' or input[i] == '÷' or input[i] == '×':
                        index = i
                        boolean = True
                        break
                    
                    elif input[i] == '%':
                        self.user_input.insert("×(−")
                        break
                
                if boolean:
                    input_substr = input[index+1:]
                    new_substr = input[0:index+1] + "(−" + input_substr
                    self.user_input.setText(new_substr)
                
                
            
        
    def backspace(self):
        input_list = list(self.user_input.text())
        if input_list != []:
            input_list.pop(-1)
            user_text = ''.join(input_list)
            self.user_input.setText(user_text)
        self.equals_clicked = 0
        
    def left_bracket(self):
        if len(self.user_input.text()) < 14:
            self.user_input.insert("(")
                
    def right_bracket(self):
        if len(self.user_input.text()) < 14:
            self.user_input.insert(")")
        
    def clear_input(self):
        self.user_input.clear()
        self.equals_clicked = 0
    
    
        
    def result_view(self):
        expression = self.user_input.text()
        
        #work on this
        self.equals_clicked += 1
        index = 0
        new_res = ''
        carry_on = ''
        boolean = False
        for i in range(len(expression)-1, 0, -1):
            if expression[i] == '+' or expression[i] == '−' or expression[i] == '÷' or expression[i] == '×':
                index = i
                boolean = True
                break
        if boolean:
            carry_on = expression[index:]
            new_res = self.res + carry_on
            
                        
        
        if expression != '':
            if self.equals_clicked > 1:
                self.user_input.setText(self.controller.result_controller(new_res))
            else:
                self.res = self.controller.result_controller(expression)
                self.user_input.setText(self.res)
            
        
        
        
        
