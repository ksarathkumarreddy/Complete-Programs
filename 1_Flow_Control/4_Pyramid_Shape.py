
def pyramid(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end='')
        print("\r")

n = 5
pyramid(n)




#  Count even and odd numbers
list = [1,2,3,4,5,6,7,8,9,11,12]
even_count = 0
odd_count = 0
count = 0
for x in list:
    if x % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Number of even count is:",even_count)
print("Number of odd count is:",odd_count)


# Print all number 0 to 6 except 3 and 6.
for i in range(0,6):
    if i == 3:
        continue
    elif i == 6:
        continue
    else:
        print(i)


# OR
for x in range(6):
    if (x == 3 or x == 6):
        continue
    print(x,end=' ')
print('\n')


# Fizz and Buzz where 3 and 5 as wellas both 3,5

for val in range(1,50):
    if(val % 3 == 0 and val % 5 == 0):
        print("FizzBuzz")
        continue
    elif(val % 3 == 0):
        print("Fizz")
        continue
    elif(val % 5 == 0):
        print("Buzz")
        continue
    else:
        print(val)


li = ['geeks','for','geeks']
for i in range(len(li)):
    print(i)
    #print(li[i])

li1 = ['sa','bh','va','ra','vi','sr','sa','bh','va','ra','vi','sr']
for i in range(len(li1)):
    print(li1[i])

# 100 to 400 where each number is an even number like 200,202
list =[]
for i in range(100,400):
    s = str(i)
    if(int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        list.append(s)
print(','.join(list))


# Pattern for T
res_str=""
for row in range(0,7):
    for column in range(0,7):
        if (column == 3 or (row == 0 and column > 0 and column <6)):
            res_str=res_str+"*"
        else:
            res_str=res_str+" "
    res_str=res_str+"\n"
print(res_str)

# 5th table multiplication

n = int(input("Input a number:"))
for i in range(1,11):
    print(n,"x",i,'=',n*i)



# Enter number of rows
n = int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print()