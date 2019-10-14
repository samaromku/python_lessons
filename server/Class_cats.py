class Cat:

    def __init__(self, name, age, color, sex, breed):
        self.name = name
        self.age = age
        self.color = color
        self.sex = sex
        self.breed = breed

    def get_cats_parameters(self):
        return vars(self)


cat1 = Cat("Kora", 4, "blue", "female", "british")
cat2 = Cat("Kala", 2, "grey", "female", "british")
cat3 = Cat("Leo", 1, "tabby", "male", "british")


def print_all_cats_parameters():
    print(cat1.get_cats_parameters())
    print(cat2.get_cats_parameters())
    print(cat3.get_cats_parameters())


def print_all_cats():
    print(vars(cat1))
    print(vars(cat2))
    print(vars(cat3))


print("print_all_cats")
print_all_cats()
print("print_all_cats_parameters")
print_all_cats_parameters()
