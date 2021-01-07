class Class:
    def __init__(self, id, max_places, n_classes):
        self.id = id
        self.max_places = max_places
        self.n_places = 0
        self.places = []
        self.ordered_students = [[] for i in range(n_classes)]