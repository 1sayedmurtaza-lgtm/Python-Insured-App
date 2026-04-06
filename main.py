from secrets import choice

from evidence import Evidence
from utils import get_clean_input
#The App / UI (main.py)
#This is the only file that communicates with the user. It uses input() to get data and print() to show results. It creates an instance of the Evidence class to manage the insured records. The main function contains a loop that displays a menu, processes user choices, and interacts with the Evidence class accordingly.

def main():
    database = Evidence()
    
    while True:
        print("\n------------------------------")
        print("Evidence pojistenych (Insurance Records)")
        print("------------------------------")
        print("Select action:")
        print("1 - Add new insured")
        print("2 - List all insured")
        print("3 - Search for insured")
        print("4 - End")
        
        choice = input("\nChoice: ")

        # Inside your main loop for Choice 1:
        if choice == "1":
           name = get_clean_input("Enter name: ")
           surname = get_clean_input("Enter surname: ")
           phone = get_clean_input("Enter phone number: ")
           age = get_clean_input("Enter age: ")
    
           database.add_insured(name, surname, age, phone)
           print("\nData saved successfully!")

        elif choice == "2":
            records = database.get_all()
            print("\nList of all insured:")
            for person in records:
                print(person)
            input("\nPress any key to continue...")

        elif choice == "3":
            name = input("Enter name to search: ")
            surname = input("Enter surname to search: ")
            results = database.find_insured(name, surname)
            
            if results:
                for person in results:
                    print(person)
            else:
                print("No records found.")
            input("\nPress any key to continue...")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()