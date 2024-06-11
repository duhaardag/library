from person import Person

class Librarian(Person):
    def __init__(self, name, age, gender, librarian_id):
        super().__init__(name, age, gender) 
        self.id = librarian_id
