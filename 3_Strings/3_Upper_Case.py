# Atleast 2 upper cases in the first 4 characters
def upper(str):
    num_upper = 0
    for letter in str[:4]:
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str.upper()
    return str
print(upper("PyThon"))

# Remove new line
# using strip method

str = "Python Programming\n"
print(str)
print(str.rstrip())

# start with string or not
str = "Python Programming\n"
print(str.startswith("Py"))

# Dedent

import textwrap
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
print(text_without_Indentation)


import textwrap
sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
#wrapped += '\n\nSecond paragraph after a blank line.'
final_result = textwrap.indent(wrapped, '----->')
print()
print(final_result)
print()



# we can print first 2 decimal places in float
float = 3.14769
formated_float = "{:.1f}".format(float)
print(formated_float)

# float 2 decimals places with sign
x = 3.1415926
y = -12.9999
print("Formatted Number with sign: "+"{:+.2f}".format(x))
print("Original Number: ", y)
print("Formatted Number with sign: "+"{:+.2f}".format(y))
z = 12.2345
print("Formatted Number with sign:"+"{:+.0f}".format(z))


# intergers with zero on the left of specified width
x = 3
print("Formated number {:0>2d}".format(x))
print("Formated number {:*<3d}".format(x))

# Number with comma separator
x = 3000000
print("Formatted number with comma{:,}".format(x))

# Percenatge
x = 0.6325
print("Number with perc{:.2%}".format(x))

# center alligned
vi = 23
print("Formatted number{:^10}".format(vi))


# count substring in a string
str = "python is a general purpose language python widely used for web apps"
print(str.count("python"))

# reverse a string

def reverse(string):
    string = "".join(reversed(string))
    return string
print(reverse("sarath"))

# reverse words in a string
def rev_sent(sent):
    words = sent.split("/n/n")
    rev_sent = "".join(reversed(words))
    return rev_sent
print(rev_sent("Hi sarath"))
