import re

class CalculatorEngine():
    def __init__(self):
        self.expression = ''
        self.operators = ('+', '-', 'x', '/')


    def add_input(self, value):
        self.expression += value


    def clear(self):
        self.expression = ''
    

    def erase(self): 
        self.expression = self.expression[:-1]


    def parse_expression(self):
        expression = self.get_expression
        split_expression = expression.re.split()

    def calculate(self):
        try:
            new_expression = self.expression.replace('x', '*')
            solution = eval(new_expression)
            solution = round(solution, 6)
            self.expression = str(solution)
        except:
            self.expression = 'ERROR!'


    def get_expression(self):
        return self.expression
    

    def remove_error(self):
        if self.expression  == 'ERROR!':
            self.clear()
    

    def add_zero(self, input):
        if self.expression == '' and input == '.':
            self.add_input('0')
    

    def validate_operator(self, input):
        if self.expression and self.expression[-1] in self.operators and input in self.operators:
            self.erase()
