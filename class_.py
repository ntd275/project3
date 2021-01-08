class Class:
    def __init__(self, id, max_places, n_classes):
        self.id = id
        self.max_places = max_places
        self.n_places = 0
        self.places = [0]*max_places
        self.ordered_student_ids = [[] for i in range(n_classes)]
    def set_place(self, student_id):
        self.places[self.n_places] = student_id
        self.n_places += 1
    def is_available(self):
        return self.n_places < self.max_places