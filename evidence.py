from insured import Insured
#The Logic 
#This class handles the "In-memory collection." Notice it doesn't use input() or print()— it only manages data.

class Evidence:
    def __init__(self):
        self.insured_list = []

    def add_insured(self, name, surname, age, phone):
        new_person = Insured(name, surname, age, phone)
        self.insured_list.append(new_person)

    def get_all(self):
        return self.insured_list

    def find_insured(self, name, surname):
        results = []
        for person in self.insured_list:
            if person.name.lower() == name.lower() and person.surname.lower() == surname.lower():
                results.append(person)
        return results