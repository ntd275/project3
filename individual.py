from course import Course
from student import Student
from data import load_courses
import random
EMPTY_PLACE_PENALTY = 10
class Individual:
    def __init__(self, data):
        self.courses = load_courses()
        self._data = data
        for i, course in enumerate(data.courses):
            for j, class_ in enumerate(course.classes):
                for k, student_ids in enumerate(class_.ordered_student_ids):
                    for student_id in random.sample(student_ids, len(student_ids)):
                        if self.can_set_place(i, j, student_id):
                            self.courses[i].classes[j].set_place(student_id)
        self._is_cost_changed = True
    def get_cost(self):
        if self._is_cost_changed:
            self._cost = self.calculate_cost()
            self._is_cost_changed = False
        return self._cost
    def calculate_cost(self):
        cost = 0
        for i, course in enumerate(self.courses):
            for j, class_ in enumerate(course.classes):
                if class_.n_places > 0:
                    cost += class_.max_places - class_.n_places
                    for k, student_id in enumerate(class_.places[:class_.n_places]):
                        for m, student_ids in enumerate(self._data.courses[i].classes[j].ordered_student_ids):
                            if student_id in student_ids:
                                cost += m
                                break
        return cost
    def can_set_place(self, course_id, class_id, student_id):
        if not self.courses[course_id].classes[class_id].is_available():
            return False
        else:
            for class_ in self.courses[course_id].classes:
                if student_id in class_.places:
                    return False
            return True