class Person:
    def __init__(self, username, password, location):
        self.username = username
        self.password = password
        self.location = location

# To initiate a subclass...
class Hiree(Person): # this is the way
    pass