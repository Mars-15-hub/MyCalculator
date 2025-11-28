import os
import sys
from model.calculator_model import CalculatorModel

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
class CalculatorController:
    def __init__(self):
        self.model = CalculatorModel()
    
    def result_controller(self, expression):
        return self.model.result_model(expression)
    
    
    
    
