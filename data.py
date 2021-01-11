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
    def __init__(self, *args):
        if (len(args) == 0):
            self.courses = [Course(i, N_CLASSES_PER_COURSES)
                            for i in range(N_COURSES)]
            self.students = []
            ordered_lists = []
            for i in range(1, N_STUDENTS+1):
                course_ids = random.sample(
                    range(0, N_COURSES), N_COURSES_PER_STUDENTS)
                ordered_list = []
                for course_id in course_ids:
                    n_classes = self.courses[course_id].n_classes
                    class_ids = random.sample(range(n_classes), n_classes)
                    ordered_list.append(CourseClassOrder(course_id, class_ids))
                    for j, class_id in enumerate(class_ids):
                        self.courses[course_id].classes[class_id].ordered_student_ids[j].append(
                            i)
                self.students.append(Student(i, ordered_list))
        else:
            dataset = "data/"+args[0]
            with open(dataset+'/course.txt', 'r') as f:
                self.courses = []
                n_courses = int(f.readline())
                for i in range(n_courses):
                    n_classes, max_n_places = [
                        int(i) for i in f.readline().strip().split()]
                    self.courses.append(Course(i, n_classes, max_n_places))
            with open(dataset+'/student.txt', 'r') as f:
                n_students = int(f.readline())
                self.students = [Student(i) for i in range(1, n_students+1)]
                while True:
                    line = [int(i) for i in f.readline().strip().split()]
                    if (len(line) == 0):
                        break
                    student_id = line[0]
                    course_id = line[1]
                    class_ids = line[2:]
                    # print(student_id, course_id, class_ids)
                    self.students[student_id-1].add_order(course_id, class_ids)
                    # self.students[student_id-1].print_ordered_list()
                    # input()
                    for i, class_id in enumerate(class_ids):
                        self.courses[course_id].classes[class_id].ordered_student_ids[i].append(
                            student_id)


def load_courses():
    return [Course(i, N_CLASSES_PER_COURSES) for i in range(N_COURSES)]


d = Data('dataset0')
