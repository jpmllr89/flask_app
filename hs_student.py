from student import Student

class HighSchoolStudent(Student):

    _school_name = "Springfield High"

    def _get_school_name(self):
        return f"{self.get_name_capitalized()} from {super()._get_school_name()}"