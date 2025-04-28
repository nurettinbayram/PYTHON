from abc import ABC, abstractmethod



class Person(ABC):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname


class ExamTaker(ABC):
    @abstractmethod
    def takeExam(self):
        pass


class ProjectMaker(ABC):
    @abstractmethod
    def makeProject(self):
        pass


class LanguageTeacher(ABC):
    @abstractmethod
    def teachLanguage(self):
        pass


class SportsTeacher(ABC):
    @abstractmethod
    def teachSport(self):
        pass


class Student(Person, ExamTaker, ProjectMaker):
    def takeExam(self):
        print(f"{self.name} can take exam")

    def makeProject(self):
        print(f"{self.name} can make project")

    def __init__(self, name, lastname):
        super().__init__(name, lastname)


class Teacher(Person, LanguageTeacher or SportsTeacher):
    def __init__(self, name, lastname):
        super().__init__(name, lastname)
    def teachSport(self):
        print(f"{self.name} can teach sport")
    def teachLanguage(self):
        print(f"{self.name} can teach language ")


# ------------------TESTING--------------------------

# student = Student("nurettin", "bayram")
# teacher = Teacher("bulent", "yildiz")
#
# student.takeExam()
# student.makeProject()
# teacher.teachSport()
# teacher.teachLanguage()

teachers = [Teacher("bulent", "yildiz"), Teacher("murat", "sari"),
            Teacher("nejdet", "can")]
students = [Student("nurettin", "bayram"), Student("okan", "akyildiz"),
            Student("kral", "kan")]

abilities = {
    LanguageTeacher : [lambda obj : obj.teachLanguage()],
    SportsTeacher : [lambda obj : obj.sportTeacher()],
    ExamTaker : [lambda obj : obj.takeExam()],
    ProjectMaker : [lambda obj : obj.makeProject()]
}

for teacher in teachers:
    for interface, actions in abilities.items():
        if isinstance(teacher, interface):
            for action in actions:
                action(teacher)
