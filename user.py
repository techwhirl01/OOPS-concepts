class User:
    def __init__(self, name):
        self.name = name

    def show_details(self):
        return f"User: {self.name}"
