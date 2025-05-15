#  Why Use super()?
# When you want a child class (aka subclass) to use the functionality from a parent class (aka superclass), but add more logic, super() allows you to reuse and extend the base behavior without duplicating code.

class User:
    def log_in(self):
        self.logged_in = True

class Student(User):
    def log_in(self):
        super().log_in()  # Reuses User's method
        self.in_class = True  # Adds student-specific logic

#  Q: Why does __init__() use super() the most?
# A: The __init__() method is commonly used to initialize attributes when an object is created. Since both parent and child classes may have their own setup needs, super() ensures:

# The parent’s initialization logic runs first (or at least runs),

# Code isn't repeated,

# Initialization is layered cleanly (e.g., name in User, grade in Student).

# Without super():
# Not DRY
class Student(User):
    def __init__(self, name, grade):
        self.name = name  # Already handled in User
        self.grade = grade

class Student(User):
    def __init__(self, name, grade):
        super().__init__(name)  # Call User's __init__
        self.grade = grade

# Inheritance lets you share functionality.

# super() lets you extend functionality cleanly.

# Use it especially in __init__() to avoid repeating initialization logic.