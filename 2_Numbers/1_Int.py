'''
Fundamental data types are:
------------
Int
Float
Complex
Boolean
None
'''
x = '234'
print(int(x))
print(complex(x))

y = None
if y:
    print("none value")
else:
    print("no none value")

x = 1,2,3,4,5,6,7,8,9
count = 0
for i in x:
    count += i
print(count)

# or
numbers = 1,2,2,3,3
def sum(numbers):
    tot = 0
    for i in numbers:
        tot += i
    return tot
print(sum(numbers))


z = 1.1,1.2,1.3
count = 0
for val in z:
    count += 1
print(count)


x = '233'
print(type(x))
val = int(x)
print(type(val))


x = True + False
print(x)

