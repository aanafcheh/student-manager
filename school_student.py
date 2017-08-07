from student import *


class SchoolStudent(Student):
    school_name = "Mirza"

    def get_university_name(self):
        return "This is just a school student."

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + "-school"
