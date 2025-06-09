class GroupFullError(Exception):

    def __init__(self, message="Cannot add student: group is full"):
        super().__init__(message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, Age: {self.age}, Gender: {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


    def __eq__(self, other):
        return isinstance(other,Student) and self.record_book == other.record_book

    def __hash__(self):
        return hash(self.record_book)


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullError()
        self.group.add(student)


    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None


    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)


    def __str__(self):
        all_students = '\n'.join(str(st) for st in self.group)
        return f'Number:{self.number}\n {all_students} '



st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

for i in range (1, 12):
    student = Student('Male', 20+i, f'Name{i}', f'Last{i}', f'RB{i}')
    try:
        gr.add_student(student)
    except GroupFullError as e:
        print(f"Error add student{student.first_name} {student.last_name}: {e}")
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!



