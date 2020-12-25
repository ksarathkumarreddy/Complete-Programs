ch = input("Enter a alphabet:")
if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
    print(ch,"is a vowel")
else:
    print(ch,"is a consonant")


# Students grade based on marks

marks = int(input("Enter marks:"))
if marks >= 90 and marks <=100:
    print('A+ Grade')
elif marks >= 80 and marks <= 90:
    print("A grade")
elif marks >= 70 and marks <= 80:
    print("B grade")
elif marks >= 50 and marks <= 70:
    print("C grade")
else:
    print("FAIL")

# Retrieve all eve number by using list comprehension

even_num = [i for i in range(1,100) if i % 2 ==0]
print(even_num)

# Retrieve all odd numbers
odd_num = [i for i in range(1,100) if i % 2 !=0]
print(odd_num)

