import Office
class Faculty_Member:
    def __init__(self, office: Office, name: str="", email: str=""):
        self.Name   = name
        self.Office = office
        self.Email  = email

    def update(self,attribute: str, x: str):
        attr = getattr(self, attribute)
        self.attr = x


class Professor(Faculty_Member):
    def __init__(self):
        pass

class Teacher_Assistant(Faculty_Member):
    def __init__(self):
        pass