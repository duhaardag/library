from person import Person

class Patron(Person):
    def __init__(self, name, age, gender, patron_id):
        super().__init__(name, age, gender) 
        self.id = patron_id