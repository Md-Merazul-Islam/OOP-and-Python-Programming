import random
from persons import*
from school import*
def main():
    school = School("Dhaladia High School", "Dhaladia")
    one = ClassRoom('One')
    school.add_classroom(one)
    two = ClassRoom('Two')
    school.add_classroom(two)
    three = ClassRoom('Three')
    school.add_classroom(three)

    # Add students
    meraz = Student("Meraz", one)
    school.student_admission(meraz)
    rakib = Student("Rakib", one)
    school.student_admission(rakib)
    antor = Student("Antor", one)
    school.student_admission(antor)

    # Subjects
    phy_teacher = Teacher('Topon')
    phy = Subject('Physics', phy_teacher)
    one.add_subject(phy)
    chy_teacher = Teacher('Masud')
    chy = Subject('Chemistry', chy_teacher)
    one.add_subject(chy)
    math_teacher = Teacher('Faruk')
    math = Subject('Mathematics', math_teacher)
    one.add_subject(math)

    one.take_semester_final()

    print(school)


if __name__ == '__main__':
    main()
