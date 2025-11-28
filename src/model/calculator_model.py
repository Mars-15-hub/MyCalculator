import math
class CalculatorModel:
    
    def result_model(self, expression):
        if '÷' in expression:
            expression = expression.replace('÷', '/')
        if '×' in expression:
            expression = expression.replace('×', '*')
        if '−' in expression:
            expression = expression.replace('−', '-')
        if '%' in expression:
            expression = expression.replace('%', '*(1/100)')
            
        
        res = eval(expression)
        
        if res % 1 == 0:
            return str(int(res))
        return str(round(res, 12))
        
        #except Exception:
        #    return ''
    


