from course import Course
from student import Student
from course_class import CourseClassOrder
import random
# def cources_from_file(file):
#     #TODO
#     return [Cource()]

# def student_from_file(file):
#     #TODO
#     return [Student()]
N_COURSES = 5
N_CLASSES_PER_COURSES = 3
N_STUDENTS = 50
N_COURSES_PER_STUDENTS = 2
class Data:
    def __init__(self):
        # generate courses and ordered_lists to test
        # will be loaded from file
        self.courses = [Course(i, N_CLASSES_PER_COURSES) for i in range(N_COURSES)]
        self.students = []
        ordered_lists = []
        for i in range(1, N_STUDENTS+1):
            course_ids = random.sample(range(0, N_COURSES), N_COURSES_PER_STUDENTS)
            ordered_list = []
            for course_id in course_ids:
                n_classes = self.courses[course_id].n_classes
                class_ids = random.sample(range(n_classes), n_classes)
                ordered_list.append(CourseClassOrder(course_id, class_ids))
                for j, class_id in enumerate(class_ids):
                    self.courses[course_id].classes[class_id].ordered_student_ids[j].append(i)
            self.students.append(Student(i, ordered_list))

def load_courses():
    return [Course(i, N_CLASSES_PER_COURSES) for i in range(N_COURSES)]