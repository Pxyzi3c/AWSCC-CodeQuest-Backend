class Calculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num
        
        return _sum

class ComplexCalculator(Calculator):
    def average(self, numlist: list):
        return self.sum(numlist) / len(numlist)
    
    def power(self, base: int, exponent: int):
        return base ** exponent

def start():
    numbers = []
    complexCal = ComplexCalculator()
    while True:
        try:
            user_input = input("Enter a number [press Enter to exit]: ")
            if user_input:
                numbers.append(int(user_input))
            else:
                calculateSum = complexCal.sum(numbers)
                calculateAverage = complexCal.average(numbers)
                calculatPower = complexCal.power(2, 3)
                print(f"Here's the numbers inputted: {numbers}")
                print(f"Sum: {calculateSum}")
                print(f"Average: {calculateAverage}")
                print(f"Power: {calculatPower}")
                break
        except KeyboardInterrupt:
            print("\nCancelled!")
            break

start()