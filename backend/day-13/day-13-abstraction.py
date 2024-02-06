class Calculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num
        
        return _sum

def start():
    numbers = []
    while True:
        user_input = input("Enter a number [press Enter to exit]: ")
        if user_input:
            numbers.append(int(user_input))
        else:
            calculate_sum = Calculator().sum(numbers)
            print(f"Here's the numbers inputted: {numbers}")
            print(f"Sum: {calculate_sum}")
            break

start()