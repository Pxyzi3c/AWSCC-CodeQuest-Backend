first_number = 0
second_number = 0 
third_number = 0
sum = 0

numbers = {
    'first number': first_number,
    'second number': second_number,
    'third number': third_number,
}

for key, value in numbers.items():
    value = input(f"Enter the {key}: ")
    sum += int(value);

print(f"Sum: {sum}");