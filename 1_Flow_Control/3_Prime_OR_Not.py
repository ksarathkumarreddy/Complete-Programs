num = int(input("Enter a number:"))
for i in range(2,num):
    if num % 2 == 0:
        print("not a prime number")
        break
else:
    print("prime number")



Lower = 1
Upper = 100
print("Prime number between",Lower,'and ',Upper,'are:')
for num in range(Lower,Upper+1):
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num,'',sep=',',end='')


# Multiples of 4 from 1 to 100
for i in range(1,100):
    if i % 4 == 0:
        print(i,'',sep=',',end='')


# Python program to check if year is a leap year or not

year = int(input("Enter a year:"))

# To get year (integer input) from the user
# year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{} is a leap year".format(year))
       else:
           print("{} is not a leap year".format(year))
   else:
       print("{} is a leap year".format(year))
else:
   print("{} is not a leap year".format(year))
