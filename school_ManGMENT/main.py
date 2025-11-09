class DataBase:
    def __init__(self):
        self.students = {}
        self.Teachers = {}
        self.Admin = {}
        self.permissions = {}
class Admin(DataBase):
    pass
class Teachers(Admin):
    pass
class students(Teachers):
    pass
if __name__ == "__main__":
    pass