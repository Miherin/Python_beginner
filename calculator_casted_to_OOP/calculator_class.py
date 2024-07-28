class Calculator:

    def __init__(self):
        
        self.operation = {
            "+":self.summing,
            "-":self.subtracting,
            "/":self.divinding,
            "*":self.multipling    
        }
        
    def run_calculator(self):
        self.ask_first_number = int(input("Type one number: "))
        self.ask_operation_symbol = input("Type an operation symbol '+', '-', '*', '/': ")
        self.ask_second_number = int(input("Type other number: "))
        self.calculator(self.ask_first_number, self.ask_operation_symbol, self.ask_second_number)
        self.total = float(self.calculator(self.ask_first_number, self.ask_second_number, self.ask_operation_symbol))
        print(f"The total of the operation {self.ask_first_number} {self.ask_operation_symbol} {self.ask_second_number} = {self.total}")

    def calculator(self, first_input, second_input, symbol):
        for entry in self.operation:
            if entry == symbol:
                return self.operation[entry](first_input, second_input)                
    

    def summing(self, first_number, second_number):
        return first_number + second_number

    def subtracting(self, first_number, second_number):
        return first_number - second_number

    def divinding(self, first_number, second_number):
        return first_number / second_number

    def multipling(self, first_number, second_number):
        return first_number * second_number
    
calculator = Calculator()