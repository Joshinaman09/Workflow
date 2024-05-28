print("New File Added:")

# Function to get and print user details
def print_user_details():
    # Prompt the user for their name
    name = input("Enter your name: ")

    # Prompt the user for their age
    age = input("Enter your age: ")

    # Prompt the user for their date of birth
    dob = input("Enter your date of birth (DD/MM/YYYY): ")

    # Print the user details
    print("\nUser Details:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Date of Birth: {dob}")

# Call the function to execute the code
print_user_details()
