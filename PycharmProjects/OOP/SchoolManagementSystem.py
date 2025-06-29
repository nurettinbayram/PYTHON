from abc import ABC, abstractmethod

# ------------------ Abstract Classes ------------------
class Person(ABC):
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def info(self):
        print(f"{self.name} {self.lastname} is a {self.__class__.__name__}")

# ------------------ Interfaces ------------------
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

# ------------------ Concrete Classes ------------------
class ExamStudent(Person, ExamTaker):
    def takeExam(self):
        print(f"{self.name} is taking the exam.")

class ProjectStudent(Person, ProjectMaker):
    def makeProject(self):
        print(f"{self.name} is making a project.")

class FullStudent(Person, ExamTaker, ProjectMaker):
    def takeExam(self):
        print(f"{self.name} is taking the exam.")

    def makeProject(self):
        print(f"{self.name} is making a project.")


class LanguageTeacherImpl(Person, LanguageTeacher):
    def teachLanguage(self):
        print(f"{self.name} is teaching language.")

class SportsTeacherImpl(Person, SportsTeacher):
    def teachSport(self):
        print(f"{self.name} is teaching sport.")

# ------------------ Testing ------------------
people = [
    LanguageTeacherImpl("Bulent", "Yildiz"),
    SportsTeacherImpl("Murat", "Sari"),
    LanguageTeacherImpl("Nejdet", "Can"),
    ExamStudent("Ali", "Kaya"),
    ProjectStudent("Ayşe", "Demir"),
    FullStudent("Mehmet", "Yıldız")
]

abilities = {
    LanguageTeacher: [lambda obj: obj.teachLanguage()],
    SportsTeacher: [lambda obj: obj.teachSport()],
    ExamTaker: [lambda obj: obj.takeExam()],
    ProjectMaker: [lambda obj: obj.makeProject()]
}

for person in people:
    print(f"-------- {person.name} {person.lastname} --------")
    person.info()
    for interface, actions in abilities.items():
        if isinstance(person, interface):
            for action in actions:
                action(person)
    print()
