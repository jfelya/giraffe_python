class Student:

    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def honor(self):
        if self.gpa > 3.5:
            return True
        else:
            return False


estudiante = Student("Fly", "Informatica", 3.6, True)
print(estudiante.honor())


class Chef:

    def make_dish(self):
        print("The chef is making some steak")


class ChineseChef(Chef):
    # Inheriting

    # Overwriting existing method
    def make_dish(self):
        print("The chinese chef is making some steak")

    def make_fried_rice(self):
        print("The chef is making some fried rice")


qing = ChineseChef()
qing.make_dish()
qing.make_fried_rice()
