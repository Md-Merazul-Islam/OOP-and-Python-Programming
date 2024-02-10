class Student:
    def __init__(self,name,id,free) -> None:
        self.name = name
        self.id = id
        self.free = free
    def __repr__(self) -> str:
        return f'Student : {self.name}, Id : {self.id}. Free : {self.free}.'
    

class Teacher :
    def __init__(self,Name, Id,subject) -> None:
        self.name = Name
        self.id = Id
        self.subject = subject
    def __repr__(self) -> str:
        return f'Teacher name : {self.name}, Id : {self.id}, Subject : {self.subject}'
    
class school:
    def __init__(self,name) -> None:
        self.name=name
        self.teachers_list = []
        self.student_list = []
    def add_teacher (self,name,subject):
        ubdate_id = len(self.teachers_list)+ 67000
        teacher = Teacher(name,ubdate_id,subject)
        self.teachers_list.append(teacher)
    def enroll_student (self,name,fee):
        if(fee < 6500):
            return f'Not enough fee'
        else :
            ubdate_id = len(self.student_list)+1
            student = Student(name,ubdate_id,'C')
            self.student_list.append(student)
            return f'{name} is enrolled with id {id},extra money {fee-6500}'
    def __repr__(self) -> str:
        print('Welcome ot',self.name)
        print('--------------Our Tearchers list--------------')
        for tech in self.teachers_list:
            print(tech)
            
        print('Our studen list ------------')
        for std in self.student_list:
            print(std)
        return 'All done '        


phitron = school('Phitron')
phitron.add_teacher('Md Rahat','Cp')
phitron.add_teacher('Sifat','DS')
phitron.add_teacher('Nayem ','Algo')
phitron.add_teacher('Rifat ','Xp')

phitron.enroll_student('meraz',93472097)
phitron.enroll_student('saim',5000)
phitron.enroll_student('rakib',6500)

print(phitron)