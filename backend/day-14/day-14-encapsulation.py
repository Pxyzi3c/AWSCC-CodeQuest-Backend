from datetime import datetime
filePath = 'backend/day-14/student_records.txt'

class Student:
    def __init__(self, name: str, birth_yr: int, birth_mo: int, birth_day: int):
        self.name = name
        self._birthdate = self._to_unixtime(birth_yr, birth_mo, birth_day)
    
    def _to_unixtime(self, yr, mo, day):
        return datetime(yr, mo, day).timestamp()
    
    @property
    def birthdate(self):
        return datetime.fromtimestamp(self._birthdate).strftime("%B %d, %Y")

def submitStudRecord(studDetails):
    with open(filePath, 'a') as file:
        for key, value in studDetails.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")

def start():
    while True:
        name = input("Enter student name: ")
        year = int(input("Enter birth year [YYYY]: "))
        month = int(input("Enter birth month [MM]: "))
        day = int(input("Enter birth day [DD]: "))

        student = Student(name, year, month, day)
        submitStudRecord({"Name": student.name, "Birthdate": student.birthdate})

        breaker = input("Continue [y/n] ?").lower()

        if breaker == 'n':
            break
start()