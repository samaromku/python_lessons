class MyClass:
    variable = "blah"

    def function(self):
        return "This is a message inside the class." + str(self)


myObject = MyClass()

print myObject.function()



class User:
    first_name = ""
    lest_name = ""
    age = 0
    sex = ""


user = User()
user.first_name = "Andrey"
user.last_name = "Savchenko"
user.age = 28
user.sex = "male"

print vars(user)

class UserWithConstructor:
    first_name = ""
    last_name = ""
    age = 0
    sex = ""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex


userWithConstructor = UserWithConstructor("Borja", "Martin", 30, "male")
print vars(userWithConstructor)
