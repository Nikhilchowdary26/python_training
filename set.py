numbers=[1,1,2,2,3,4]
uniques=set(numbers)
print(uniques)
second={1,2,44}
second.add(3)
second.add(100)
print(second)
second.pop()
second.pop()
print(len(second))
print(second)

a={1,2,3}
b={1,100}

print(a|b) #Union(|) it will combine two sets{} and removes duplicates and print new set
print(a&b) #Intersection(&) it will compare two sets and returns commone values
print(a-b) #difference(-) it will compare two sets and return wlements which are not common.
print(a^b) #symmetric_difference(^) it will compare two sets and return the elements which are not in
#either both sets or firt set or second set

print(a[0])