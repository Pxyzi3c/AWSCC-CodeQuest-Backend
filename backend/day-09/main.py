from math_operations import calculate_area

print("CIRCLE CALCULATOR:")
radius = int(input("Enter radius: "))

print(f"Area of the Circle: {round(calculate_area(radius), 2)}")