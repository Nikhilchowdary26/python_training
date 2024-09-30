from sys import getsizeof
from pprint import pprint

point={
    "a":1,
    "b":2
}
point['a']=10
point['c']=100
print(type(point))
print(point.get('c'))
del point['a']
print(point)
# for key in point : 
#     print(key,point[key])

# for x in point.items() : 
#     print(x)

for key,value in point.items() :
    print(key,value)

values=(x*2 for x in range(10))
for x in values:
    print(x)
print("Gen :",getsizeof(values))
values1=[x*2 for x in range(10)]
print("List :",getsizeof(values1))

sentence="Hi My name is Nikhil"

char_frequency={}
for x in sentence:
    if x in char_frequency:
        char_frequency[x] += 1
    else:
        char_frequency[x]=1
pprint(char_frequency,width=1)
final_list=sorted(char_frequency.items(),key=lambda kv:kv[1],reverse=True)
for x in final_list:
    print("The highest character used ",x)
    break
