from class_ import Class
class Course:
    def __init__(self, id, n_classes, max_n_places=6):
        self.id = id
        self.n_classes = n_classes
        self.max_n_places=max_n_places
        self.init_classes()
    def init_classes(self):
        self.classes = []
        for i in range(self.n_classes):
            self.classes.append(Class(i, self.max_n_places, self.n_classes))
    
# c = Course(1, [1, 2, 3])
# print(c._id)