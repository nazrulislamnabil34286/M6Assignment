class Student:
    def __init__(self, name, roll, email, department):
        self.name = name
        self.roll = roll
        self.email = email
        self.department = department

    def to_csv(self):
        return f"{self.name},{self.roll},{self.email},{self.department}\n"

    @staticmethod
    def from_csv(line):
        data = line.strip().split(",")
        return Student(data[0], int(data[1]), data[2], data[3])
