def get_clean_input(prompt):
    while True:
        value = input(prompt).strip()
        
        # Check if empty (Requirement: "Validation of at least an empty name")
        if not value:
            print("Error: This field cannot be empty.")
            continue
            
        # Check for special characters (space is allowed, so we replace it temporarily)
        # .isalnum() checks if it is Alpha-Numeric (A-Z or 0-9)
        if not value.replace(" ", "").isalnum():
            print("Error: Special characters (.,@#!) are not allowed. Use only letters and numbers.")
            continue
            
        return value