class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email, age):
        """Add a new user to the system."""
        if username in self.users:
            raise ValueError(f"User {username} already exists")

        if age < 0 or age > 150:
            raise ValueError("Invalid age")

        self.users[username] = {"email": email, "age": age, "active": True}
        return True

    def get_user(self, username):
        """Retrieve user information."""
        return self.users.get(username)

    def update_user_email(self, username, new_email):
        """Update a user's email address."""
        if username not in self.users:
            raise ValueError(f"User {username} not found")

        self.users[username]["email"] = new_email
        return True

    def deactivate_user(self, username):
        """Deactivate a user account."""
        if username not in self.users:
            raise ValueError(f"User {username} not found")

        self.users[username]["active"] = False
        return True

    def get_active_users(self):
        """Return list of all active users."""
        return [username for username, data in self.users.items() if data["active"]]


# How to introduce the bug:
# Change line 7 in statistics.py from:
# pythonactive_users = self.user_manager.get_active_users()
# to:
# pythonactive_users = list(self.user_manager.users.keys())
