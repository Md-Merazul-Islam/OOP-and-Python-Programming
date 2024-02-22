
from school import*
import random
class Person:
    def __init__(self, name) -> None:
        self.name = name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        marks = random.randint(0, 100)
        return marks

    def __repr__(self) -> str:
        return f'{self.name}'


class Student(Person):
    def __init__(self, name, classroom) -> None:
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grades = {}
        self.grade = None

    def calculate_final_grade(self):
        total_points = sum(School.grade_to_value(grade) for grade in self.subject_grades.values())
        points_avg = total_points / len(self.subject_grades)
        self.grade = School.value_to_grade(points_avg)
        print(f'{self.name} final grade: {self.grade} with points average: {points_avg}')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value