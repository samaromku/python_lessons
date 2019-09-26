class MyClass:
    variable = "blah"

    def function(self):
        return "This is a message inside the class." + str(self)


myObject = MyClass()


class UserFirstLastNames:
    def __init__(self, first_name):
        self.first_name = first_name

    first_name = ""
    lest_name = ""


user = UserFirstLastNames("first_name")
user.first_name = "Andrey"
user.last_name = "Savchenko"

anotherUser = UserFirstLastNames("second_name")
anotherUser.first_name = "Andrey"


class UserWithFirstLastAgeSex:
    first_name = ""
    last_name = ""
    age = 0
    sex = ""

    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex


userWithConstructor = UserWithFirstLastAgeSex("Borja", "Martin", 30, "male")


def doSomethingWithUserData(user: UserWithFirstLastAgeSex):
    print(vars(user))


doSomethingWithUserData(userWithConstructor)
doSomethingWithUserData(user)
