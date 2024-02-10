class Student:
    def __init__(self, name, Roll, fee) -> None:
        self.name = name
        self.Roll = Roll
        self.fee = fee

    def __repr__(self) -> str:
        return f'Student Name: {self.name}. Roll: {self.Roll}. Fee: {self.fee}'


class Teacher:
    def __init__(self, Name, Id, Subject) -> None:
        self.id = Id
        self.subject = Subject
        self.name = Name

    def __repr__(self) -> str:
        return f'Teacher Name: {self.name}. Id no: {self.id}. Subject: {self.subject}'


class Dhaladia_High_School:
    def __init__(self, name) -> None:
        self.name = name
        self.teacher_list = []
        self.student_list = []

    def add_std(self, name,fee):
        if fee < 1200:
            return f'Your money is not enough'
        else:
            roll = len(self.student_list) + 1
            text = Student(name, roll, 'Done')
            self.student_list.append(text)

    def add_teach(self, name, sub):
        id = len(self.teacher_list) + 1
        text = Teacher(name, id, sub)
        self.teacher_list.append(text)

    def __repr__(self) -> str:
        print("<--------Teacher list-------->")
        for tch in self.teacher_list:
            print(tch)
        print("<--------Student list-------->")
        for std in self.student_list:
            print(std)

        return "Ok complete you admission"


DHS = Dhaladia_High_School('DHS')
while True:
    test = input("Do you want to continue? (Yes-1/No-0): ").strip().lower()
    if test == "no":
        break
    elif test == "yes":
        st_tc = input("Do you want to add a Student (s) or a Teacher (t)?: ").strip().lower()
        if st_tc == "s":
            name = input("Enter the student's name: ")
            fee = int(input("Enter the fee: "))
            DHS.add_std(name, fee)
        elif st_tc == "t":
            name = input("Enter the teacher's name: ")
            sub = input("Enter the subject name: ")
            DHS.add_teach(name, sub)
        else:
            print("Invalid input. Please enter 's' or 't'.")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print("Final result is:", DHS)

