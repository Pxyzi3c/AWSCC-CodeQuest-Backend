class Student:
    def __init__(self, name: str, age: int, is_enrolled: bool, classes: list, offenses: list):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses
    
    def addClass(self, newClass):
        self.classes.append(newClass)

student1 = Student("Harvy Jones Pontillas", 23, True, [], [])

student1.addClass("Science")
print(student1.classes)