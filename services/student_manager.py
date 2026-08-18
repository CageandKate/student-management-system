from models.student import Student
from utils import file_utils



class StudentManager:
    def __init__(self):
        data = file_utils.load_students()

        self.students = []

        for item in data:
            student = Student.from_dict(item)
            self.students.append(student)



    def save_students(self):
        students_dict = [
            student.to_dict()
            for student in self.students
        ]
        file_utils.save_students(students_dict)

    def find_student_by_id(self,student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def add_student(self,student_id,name,age,score):

        if self.find_student_by_id(student_id) is not None:
            return "duplicate_id"
        if not name.strip():
            return "invalid_name"  
        if not Student.is_valid_age(age):
            return "invalid_age"
        if not Student.is_valid_score(score):
            return "invalid_score"      
        student = Student(student_id, name, age, score)
        self.students.append(student)
        self.save_students()
        return "success"


    def show_students(self):
        if not self.students:
            return False
        for student in self.students:
            print(student)
        return True


    def update_score(self,student_id,score):
        student = self.find_student_by_id(student_id)
        if student is  None:
            return "not_found"
        
        if not student.update_score(score):
            return "invalid_score"

        self.save_students()
        return "success"

    def delete_student(self,student_id):
        student = self.find_student_by_id(student_id)
        if student is  None:   
            return False 
        
        self.students.remove(student) 
        self.save_students()   
        return True