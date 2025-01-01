class ConditionalExamples:
    def authenticate_user(self, username, password, user_db):
        """
        Authenticate user based on username and password.
        """
        if username not in user_db:
            return "User not found."
        elif user_db[username] != password:
            return "Incorrect password."
        else:
            return "Login successful!"

    def validate_registration_form(self, data):
        """
        Validate registration form input.
        """
        if not data.get("email"):
            return "Email is required."
        elif not data.get("password"):
            return "Password is required."
        elif len(data["password"]) < 8:
            return "Password must be at least 8 characters long."
        else:
            return "Registration successful."

    def process_payment(self, status):
        """
        Process payment based on status.
        """
        if status == "success":
            return "Payment completed successfully."
        elif status == "failed":
            return "Payment failed. Please try again."
        elif status == "pending":
            return "Payment is pending. Please wait for confirmation."
        else:
            return "Invalid payment status."

    def get_user_role(self, role):
        """
        Determine user privileges based on role (using match statement).
        """
        match role:
            case "admin":
                return "Admin privileges granted."
            case "editor":
                return "Editor access granted."
            case "viewer":
                return "View-only access granted."
            case _:
                return "Role not recognized."

    def ternary_example(self, user_role):
        """
        Demonstrate the use of a ternary operator.
        """
        return "Welcome, Admin!" if user_role == "admin" else "Welcome, User!"

    def surprise_me(self):
        """
        Return a random Taylor Swift surprise message.
        """
        import random
        surprises = [
            "Did you know? Taylor Swift wrote her entire album 'Speak Now' by herself!",
            "Surprise! Taylor Swift's 'Reputation' tour is one of the highest-grossing tours of all time.",
            "Fun fact: Taylor Swift holds the record for the most American Music Awards won by any artist!",
            "Here's a surprise: Taylor Swift secretly released two albums, 'Folklore' and 'Evermore,' in 2020!",
            "Taylor Swift was named after the legendary singer-songwriter James Taylor!"
        ]
        return random.choice(surprises)

# Example usage
if __name__ == "__main__":
    examples = ConditionalExamples()

    # 1. Authenticate user
    user_db = {"alice": "password123", "bob": "qwerty"}
    print(examples.authenticate_user("alice", "password123", user_db))

    # 2. Validate registration form
    form_data = {"email": "user@example.com", "password": "1234567"}
    print(examples.validate_registration_form(form_data))

    # 3. Process payment
    print(examples.process_payment("success"))

    # 4. Get user role
    print(examples.get_user_role("editor"))

    # 5. Ternary example
    print(examples.ternary_example("admin"))

    # 6. Surprise me
    print(examples.surprise_me())

      