import sys
import itertools

major,minor,macro=sys.version.split()[0].split('.')
version=float(f"{major}.{minor}")
# print(sys.version)
if(version > 3.5) :
    print("Thanks Namaste".encode())
else :
    print("Mingey")
print("HelloWorld")
print("*" * 10)
y='''n
m
k'''
print(y)
a=input("x: ")
print(int(a)+3)


print("1st for loop starting")
def isZero(n) :
    print("Function isZero started")
    if n == 0 : 
        print("The value is 0 so we can not print") 
        return True
    else: print(f"({n})")


for x in itertools.count():
    if x >= 100 :
        print("You had printed numbers upto 100")
        break
    elif x == 0:
        returnedValue=isZero(x)
        print(returnedValue)
        if returnedValue == True :
            continue
        else:
            break
    else :
        print(x)
print('1st for loop completed')


for n in range(3) :
    for y in range(3) :
        print(f"({n},{y})")

def fizz_Buzz(input) :
    if(input % 3 == 0):
        return "Fizz"
    elif(input % 5 == 0):
        return "Buzz"
    elif(input % 3 ==0 and input % 5 == 0):
        return "FizzBuzz"
    else:
        return input

print(fizz_Buzz(7))

print(dir(int))