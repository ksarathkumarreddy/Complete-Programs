# Remove the odd places in the given string
def odd_string(str):
    res = ''
    for i in range(len(str)):
        if i % 2 == 0:
            res = res + str[i]
    return res
print(odd_string("sarath"))
print(odd_string("vishu"))
# or
str = 'sarath'
var = len(str)
for i in range(var):
    if i % 2 == 0:
        res = str[i]
        print(res,sep='',end='')


# How many times the occurence of each word in given sentence

def word_count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(word_count("python is an high level lang python is an object oriented"))


def count(str):
    counts = dict()
    words = str.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
print(count("hello everyone "))



# take input and give output as lower case or upper case
'''
input = input("Enter your name:")
print("My name is ",input.upper())
print("My name is ",input.lower())
'''

# comma separeted in sequence
char = input("enter your")
items=[n for n in char.split('-')]
items.sort()
print('-'.join(items))


# insert string in the middle
def ins_str(str, word):
	return str[:2] + word + str[2:]

print(ins_str('[[]]', 'Python'))
print(ins_str('<<>>',"sarath"))

# last two letters multiply
def str(str):
    sub_str = str[-2:]
    return sub_str * 4
print(str("sarath"))



# first three characters if length of string less than 3 return original string
def first_three(str):
    var = len(str)
    if var <= 3:
        print(str)
    else:
        print(str[:3])
first_three("sar")
first_three("python")


# To get last part of string

str1 = 'https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/',1)[0])
print(str1.rsplit('-',1)[0])


# reverse  function if it's length is multiple of 4
def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print(reverse_string('abcd'))
print(reverse_string('pythonpy'))


def reverse(string):
    string = "".join(reversed(string))
    return string
#print("The reversed string(using reversed) is : ", end="")
print(reverse("sarath"))

