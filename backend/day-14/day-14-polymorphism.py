# Learnings from this: [INHERITANCE LIMIT] Methods defined in a class with double underscore (__) are considered private, making it inaccesible to even its subclasses.

class Calculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num
        
        return _sum
    
    def _digits(self, number: int):
        digit = 0

        while number != 0:
            digit += 1
            number//=10
        
        return digit
    
    def product(self, numlist: list):
        _product = 1
        _limit = 3

        for num in numlist:
            if self._digits(num) > _limit:
                raise ValueError(f"[{num}] Input digits must not be greater than {_limit}!")
            _product *= num

        return _product        

class ComplexCalculator(Calculator):
    def average(self, numlist: list):
        return self.sum(numlist) / len(numlist)
    
    def power(self, base: int, exponent: int):
        return base ** exponent
    
    def product(self, numlist: list):
        _product = 1
        _limit = 4

        for num in numlist:
            if self._digits(num) > _limit:
                raise ValueError(f"[{num}] Input digits must not be greater than {_limit}!")
            _product *= num

        return _product;

def start():
    numbers = []
    complexCal = ComplexCalculator()
    while True:
        try:
            user_input = input("Enter a number [press Enter to exit]: ")
            if user_input:
                numbers.append(int(user_input))
            else:
                calculateProd = complexCal.product(numbers)
                print(f"Here's the numbers inputted: {numbers}")
                print(f"Product: {calculateProd}")
                break
        except KeyboardInterrupt:
            print("\nCancelled!")
            break

start()