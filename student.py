students = []


class Student:
    university_name = "XAMK"

    def __init__(self, name, student_id=123):
        self.name = name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_university_name(self):
        return self.university_name
