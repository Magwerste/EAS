# Import the necessary libraries for file handling
import pickle
import os

# Function to load user data from a pickle file
def load_user_data():
    # Check if the file with user data exists
    if os.path.exists("user_data.pkl"):
        # If it does, open and load the data
        with open("user_data.pkl", "rb") as file:
            user_data = pickle.load(file)
    else:
        # If no file is found, start with an empty dictionary for user data
        user_data = {}
    return user_data

# Function to save user data to a pickle file
def save_user_data(user_data):
    # Open the file and save the user data
    with open("user_data.pkl", "wb") as file:
        pickle.dump(user_data, file)

# Function to create a username based on user details
def create_username(first_name, last_name, dob):
    # Combine the first three letters of the first and last names with the first four digits of the date of birth
    username = (first_name[:3] + last_name[:3] + dob[0:4]).lower()
    return username

# Function to create a password for new customers
def create_password():
    # Display password criteria to the user
    print("Password Criteria:")
    print("- At least one uppercase letter")
    print("- At least one lowercase letter")
    print("- At least one number")
    print("- Should be 6 to 12 characters long")

    # Prompt the user to enter a password and check if it meets the criteria
    while True:
        password = input("Enter your password: ")
        if (
            any(c.isupper() for c in password)
            and any(c.islower() for c in password)
            and any(c.isdigit() for c in password)
            and 6 <= len(password) <= 12
        ):
            return password
        else:
            print("Invalid password. Make sure it meets the criteria.")

# Function to handle existing customer login
def existing_customer_login(user_data):
    # Prompt the user to enter their username in lowercase (case-insensitive)
    username = input("Enter your username: ").lower()

    # Check if the entered username exists in the user data
    if username in user_data:
        password_attempts = 0
        # Allow up to 3 attempts to enter the correct password
        while password_attempts < 3:
            password = input("Enter your password: ")
            # Check if the entered password matches the stored password
            if user_data[username]["password"] == password:
                print("\nLogin successful!")
                return
            else:
                print("Incorrect password. Try again.")
                password_attempts += 1
        # Deny access after three incorrect password attempts
        print("Too many incorrect password attempts. Access denied.")
    else:
        # Deny access if the username is not found
        print("Invalid username. Access denied.")

# Function to handle new customer registration
def new_customer_registration(user_data):
    # Prompt the user to enter their details, convert to lowercase
    first_name = input("Enter your first name: ").lower()  
    last_name = input("Enter your last name: ").lower() 
    DoB = input("Enter your date of birth (DD/MM/YYYY): ")
    # Create a username based on the entered details
    username = create_username(first_name, last_name, DoB)

    # Check if the username already exists
    if username not in user_data:
        # If not, prompt the user to create a password
        password = create_password()
        # Store the new user data in the dictionary
        user_data[username] = {"password": password}
        # Save the updated user data to the file
        save_user_data(user_data)
        # Display a successful registration message with the created username
        # Chose to display the created username to the user in the intended format (as they would be unaware of how the username will be created)
        # Intentionall did not display their password due to security reasons
        print(f"Registration successful! Your username is: {username}")
    else:
        # Deny registration if the username already exists
        print("Username already exists. Please choose a different username.")

# Main menu function
def main_menu():
    # Load existing user data from the file
    user_data = load_user_data()

    # Main program loop
    while True:
        # Display the main menu options
        print("\nMain Menu:")
        print("1. Login")
        print("2. Register")
        print("3. Exit")

        # Prompt the user to choose an option
        choice = input("Enter your choice (1/2/3): ")

        # Perform actions based on the user's choice
        if choice == "1":
            existing_customer_login(user_data)
        elif choice == "2":
            new_customer_registration(user_data)
        elif choice == "3":
            # Exit the program if the user chooses option 3
            print("Exiting the program. Goodbye!")
            break
        else:
            # Inform the user if an invalid choice is entered
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the main menu function if the script is executed directly
if __name__ == "__main__":
    main_menu()
