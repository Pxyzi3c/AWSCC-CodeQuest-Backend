first_number, second_number, third_number, sum = 0, 0, 0, 0;

numbers = {
    'first number': first_number,
    'second number': second_number,
    'third number': third_number,
}

for key, value in numbers.items():
    value = input(f"Enter the {key}: ")
    sum += int(value);

print(f"Sum: {sum}");