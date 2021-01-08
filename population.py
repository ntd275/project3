import prettytable
from individual import Individual

class Population:
    def __init__(self, size, data):
        self.individuals = [Individual(data) for i in range(size)]
    
    def print(self):
        for i, individual in enumerate(self.individuals):
            print("---------------")
            print("Cost of Individual", i, ":", individual.get_cost())
            individual_table = prettytable.PrettyTable(['Course', 'Class','Students'])
            for course in individual.courses:
                for class_ in course.classes:
                    individual_table.add_row([course.id, class_.id, sorted(class_.places)])
            print(individual_table)