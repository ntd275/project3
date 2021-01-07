from class_ import Class
class Course:
    def __init__(self, id, n_classes):
        self.id = id
        self.n_classes = n_classes
        self.init_classes()
    def init_classes(self):
        MAX_N_PLACES = 50
        self.classes = []
        for i in range(self.n_classes):
            self.classes.append(Class(i, MAX_N_PLACES, self.n_classes))
    
# c = Course(1, [1, 2, 3])
# print(c._id)