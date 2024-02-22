class School:

    def __init__(self, name, address) -> None:
        self.teachers = {}
        self.name = name
        self.address = address
        # composition
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        class_name = student.classroom.name
        if class_name in self.classrooms:
            self.classrooms[class_name].add_student(student)
        else:
            print(f'No classroom named {class_name}')

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_map.get(grade, 0.00)

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        output = '-------All Classrooms--------\n'
        for key, value in self.classrooms.items():
            output += f'{key}\n'

        output += '-------Students-----\n'
        one = self.classrooms.get('One')
        if one:
            for student in one.students:
                output += f'{student.name}\n'

        output += '------Subjects------\n'
        if one:
            for subject in one.subjects:
                output += f'{subject.name} - {subject.teacher.name}\n'

        output += '------Student exam marks-------\n'
        if one:
            for student in one.students:
                for subject, mark in student.marks.items():
                    output += f'{student.name} - {subject}: {mark} - {student.subject_grades[subject]}\n'
                output += '----Student end------\n'

        return output


class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        serial_id = f'{self.name} - {len(self.students)+1}'
        student.id = serial_id
        self.students.append(student)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)

        for student in self.students:
            student.calculate_final_grade()

    def __str__(self) -> str:
        return f'{self.name} - {len(self.students)}'

    def get_top_students(self):
        pass


class Subject:
    def __init__(self, name, teacher) -> None:
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 30

    def exam(self, students):
        for student in students:
            mark = self.teacher.evaluate_exam()
            student.marks[self.name] = mark
            student.subject_grades[self.name] = School.calculate_grade(mark)


