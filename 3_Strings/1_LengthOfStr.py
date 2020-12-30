'''
String is an immutable once we can create data we can't modifiy the data.
String is most powerful data type in python and we can store the data as simple as
easy just we can single quotes or duoble quotes we can mention.
why string immutable/ How string is immutable?
-------------
Once we can store the data we cant modify the data.
for ex.,,
str = 'sarath'
address of str is 234
if we can add the data to str:
means str = 'sarath'+'kumar'
Right now we can check the address it will be give different address.

'''

str = "sarath"
print(len(str))

Dict = {"id" : 101, "name" : "sarath", "age" : 23}
print(len(Dict))
print(Dict)
print(Dict.get("id"))


# We can print First two and last two only

def string_both_ends(str):
    if len(str) < 2:
        return 'Empty String'
    return str[0:2] + str[-2:]
print(string_both_ends("sarath"))
print(string_both_ends("k"))



# restart can change the resta$t

def change_char(str):
    char =str[0]
    str = str.replace(char,"$")
    str = char + str[1:]
    return str
print(change_char("sarathsa"))


# swap from one to another
def swap(a,b):
    first_a = b[:2] + a[2:]
    second_b = a[:2] + b[2:]
    return first_a + " " +second_b
print(swap('abc','xyz'))
print(swap("sarath","bharath"))


# add string
def string(str):
    length = len(str)
    if length > 2:
        if(str[-3:] == "ing"):
            str += 'ly'
        else:
            str +='ing'
    return str
print(string('bathing'))
print(string('someth'))


# Another type of swap
x = 'sarath','bharath'
fi = x[1][:2] + x[0][2:]
print(fi)
se = x[0][:2] + x[1][2:]
print(fi,se)


# Longest word
def lon_wor(list):
    word_len =[]
    for data in list:
        word_len.append((data, len(data)))
    word_len.sort()
    print(word_len)
    return word_len[-1][0],word_len[-1][1]
res = lon_wor(['venkata ramana reddy',"sara","bharath"])
print("Longest word is:",res[0])
print("Length of word is:",res[1])


list1 = ['venkata ramana reddy',"sara","bharath"]
word_len= []
for data in list1:
    word_len.append(data)
word_len.sort()
print('Longest word in list1 is:',max(word_len))
print("Length of the list1 is:",len(max(word_len)))
print("-------------")



# remove the nth character
def remo_char(str, n):
    first_part = str[:n]
    last_part = str[n+1:]
    return first_part + last_part
print(remo_char("sarath",0))
print(remo_char("Python",1))



# change characters from first and last
def change_str(str):
    return str[-1:] + str[1:-1] + str[:1]
print(change_str("abcd"))


'''
sequence
indexing
slicing
adding
multiply

'''
