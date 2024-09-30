from timeit import timeit

name=str(input("Enter your name : "))
name_list = list(name)
print(name_list)
numbers = list(range(10))
numbers_list = [str(x) for x in numbers]
print(numbers_list)
try:
    isPresent = False
    for x in numbers_list:
        for y in name_list:
            print(x, y)
            if x == y:
                isPresent = True
                break
            else:
                continue
    if not isPresent:
        print('Hi', name)
except ValueError as error:
    print("You have entered a invalid name")
finally:
    print("Finally")

try:
    age=int(input("Age: "))
    print("Your age is", age)
except ValueError as exception:
    print("You have entered invalid age")
    print(exception)

# def calculate_age(age):
#     if age >= 100 or age <= 0:
#         raise ValueError("Age cannot be less than and equal to 0 or greater than and equal to 100")
#     else:
#         print("Your age is ")
# age=int(input("Age :"))
# try :
#     calculate_age(12)
# except ValueError as error:
#     print(error)

code1 = """
def calculate_age(age):
    if age >= 100 or age <= 0:
        raise ValueError("Age cannot be less than and equal to 0 or greater than and equal to 100")
try :
    calculate_age(12)
except ValueError as error:
    pass
"""

code2 = """
def calculate_age(age):
    if age >= 100 or age <= 0:
        return None

calAge=calculate_age(12)
if calAge==None:
    pass
"""
print("Second code :", timeit(code2, number=10000))
print("First code :", timeit(code1, number=10000))
