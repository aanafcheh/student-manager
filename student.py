students = []


class Student:
    university_name = "XAMK"

    def __init__(self, first_name, last_name, student_id=123):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student" + self.first_name

    def get_name_capitalize(self):
        return self.first_name.capitalize()

    def get_university_name(self):
        return self.university_name