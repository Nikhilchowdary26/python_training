from array import array

# point=(1) ->The python compiler understoods that as a integer not a tuple
point=(1,) #Now it takes as a tuple
print(type(point))

a=1
b=2
print("Before swapping")
print("A :",a)
print("B :" ,b)
print("_______________________")
# z=a
# a=b
# b=z
a,b=b,a
print("After swapping")
print("A :",a)
print("B :",b)

#Arrays
numbers=array("f",[1.2,1.1,1.3])
print(numbers)
numbers.append(1.4)
print("added 1.4",numbers)
numbers.pop()
print("Pop",numbers)
numbers.insert(0,1.0)
print("After Insert",numbers)
numbers.remove(1.0)
print("After removing 1.0" ,numbers)
numbers.reverse()
print("After reverse",numbers)