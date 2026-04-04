#This class represents the individual.
# We use a constructor and the __str__ method 
# (the Python equivalent of toString()).
#its the model of the insured person, with attributes for name, surname, age, and phone number.
class Insured:
    def __init__(self, name, surname, age, phone):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    def __str__(self):
        # Format: Name Surname (Age) Phone
        return f"{self.name:<10} {self.surname:<10} {self.age:<5} {self.phone}"