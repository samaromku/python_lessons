x = 1.0
if x == 1:
    print("Hello world!1")
    print("test my homo")

word = "test word"
if isinstance(word, str):
    print("is string")

myList = [12, "test", 1, "hui"]
print(myList[0])
print(myList[1])
print(myList[2])
print(myList[3])

print("test hui %s" % x)

thirdX = 10 ** 5
print(thirdX)

lotsofhellos = "hello " * 10
print(lotsofhellos)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

arrayOfEvenElements = [2] * 25
print(arrayOfEvenElements)

print("%s test %s" % (1, 2))

data = ("John", "Doe", 53.44)
format_string = "Hello"

print(format_string + " %s %s Your current balance is $%f" % data)
print(data[2])

if 2 == 10 or True == True:
    print(True)

if "2" in ("3", "2"):
    print("contains")

x = 5
if x == 3:
    print("2==3")
    pass
elif x == 10:
    print("2==10")
    pass
else:
    print("non is true")
    pass

x = "test"
y = 15

print(x is y)

first_array = [1]

if first_array:
    print("2")

second_number = None

if not second_number:
    print("6")

first_array = [1, 1, 1]
second_array = [1, 2]

if first_array and first_array[0] == 1:
    print("5")
