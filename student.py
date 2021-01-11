from course_class import CourseClassOrder


class Student:
    def __init__(self, id, ordered_list=None):
        self.id = id
        self.ordered_list = ordered_list or []

    def add_order(self, course_id, class_ids):
        self.ordered_list.append(CourseClassOrder(course_id, class_ids))

    def print_ordered_list(self):
        for cco in self.ordered_list:
            print(" ", self.id, cco.course_id, cco.class_ids)
