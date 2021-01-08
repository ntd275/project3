import prettytable
from ga import GeneticAlgorithm
from data import Data
from population import Population
POPULATION_SIZE = 5
# g = GeneticAlgorithm()

# g.Run()
data = Data()
chosen_courses_table = prettytable.PrettyTable(["Student", "Course", "Classes"])
for student in data.students:
    # print("Chosen courses of student", student.id)
    for course in student.ordered_list:
        chosen_courses_table.add_row([student.id, course.course_id, course.class_ids])
        # print("Course", course.course_id)
        # print(course.class_ids)
print(chosen_courses_table)

students_chose_class_table = prettytable.PrettyTable(['Course', 'Class', 'Order','Students'])
for course in data.courses:
    # print("-----------------")
    # print("Classes of course", course.id)
    for class_ in course.classes:
        # print("Students chose class", class_.id)
        for i in range(len(class_.ordered_student_ids)):
            # print(i, class_.ordered_students[i])
            students_chose_class_table.add_row([course.id, class_.id, i, class_.ordered_student_ids[i]])
print(students_chose_class_table)

population = Population(POPULATION_SIZE, data)
population.print()

