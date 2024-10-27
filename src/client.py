class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

def create_user(username, email):
    if not isinstance(username, str):
        return "Username must be a string"
    if not isinstance(email, str):
        return "Email must be a string"
    
    if '@' not in email:
        return "Email is invalid"

    user = User(username, email)
    return "User created: {}".format(user.username)

def main():
    create_user("john_doe", "john@example.com")
    create_user(123, "invalid_email")
    create_user("jane_doe", "jane@example.com")

if __name__ == "__main__":
    main()
