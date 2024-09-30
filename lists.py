firstList=['Banana',1,'Apple','Mango']
print(len(firstList))
print(firstList[-1])
print(firstList[0:2])
print(firstList[0:])
print(firstList[::3])

numbers=[1,2,20,12,34,55]
numbers.append(55)
numbers.insert(0,10)
# numbers.pop()
# print(numbers.count(55))
print(sorted(numbers,reverse=True))
# numbers.remove(55)
# numbers.sort(reverse=True)
print(numbers)
del numbers[0:1]
# numbers.clear()
print(numbers)

# multiplied=1
# for x in enumerate(numbers) :
#     multiplied=multiplied*2
#     print(x[0],x[1])
# print(multiplied)
# print("********************************************")

first,*other,second=numbers
print(first)
print(second)
print(*other)

items=[
    ('key1',9),
    ('key2',1),
    ('key3',4)
]
# def sort_items(item):
#     return item[1]

#lambda expression
#--------------------
#lambda arguments : expression
items.sort(key=lambda item:item[1])
print(items)

# item_values=[]
# for item in items:
#     item_values.append(item[1])
# print(item_values)

# item_values=list(map(lambda item:item[1],items))
item_values=[item[1] for item in items]
print(item_values)

# item_filter=list(filter(lambda item:item[1]>1,items))
item_filter=[item for item in items if item[1]>1]
print(item_filter)

a=[1,2,3]
b=['a','b','c']

zip_values=list(zip([1.2,1.3,1.4],b))
print(zip_values)