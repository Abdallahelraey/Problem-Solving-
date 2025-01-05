
# # [Find Length of String in Python](https://www.geeksforgeeks.org/find-length-of-a-string-in-python-4-ways/)

# The first intutive and efficient way is to  go with python `len()` Functiton:


def str_len(s):
    return len(s)


def main():
    s = input("Enter a string: ").lower()
    length = str_len(s)
    print("Length of the string is:", length)
main()

# Then you can make  it complicated even more:


def str_len(s):
    len = 0
    for i in s:
        len+=1
    return len


def main():
    s = input("Enter a string: ").lower()
    length = str_len(s)
    print("Length of the string is:", length)
main()


# What about makeing it super Complicated!!


# The `count()` method in Python returns the number of times a specified substring appears in a string. 
# 
# It is commonly used in string analysis to quickly check how often certain characters or words appear.
# 
# We can tweak the usage of the `count()` method to return the length of the string as follows: `count("")`
# but the littel caviate here is that counting hte spaces between characters is always one more thatn the len of te characters in e string so you have to subtract ti form one.


def str_len(s):
    len = s.count("") - 1
    return len


def main():
    s = input("Enter a string: ").lower()
    length = str_len(s)
    print("Length of the string is:", length)
main()


# Because I'm free now lets impliment the functionality of python `count()` function:


def Ocuurences(str, Char):
    count = 0
    for i in str:
        if i == Char:
            count += 1
    return count


def main():
    str = input("Enter a string: ").lower()
    Char = input("Enter a Character: ").lower()
    count = Ocuurences(str, Char)
    print(f"The number of occurences of this {Char} is: {count}")
main()

# Finally to show more options that you probabily will never use IRL: 
# 
# lets se how can we find hte len of a string using python `enumerate()` function that is typically used to loop over an iterable and keep track of both the index and the value of elements within that iterable.

def str_len(s):
    len = 0
    for i, a in enumerate(s):
        len+=1
    return len


def main():
    s = input("Enter a string: ").lower()
    length = str_len(s)
    print("Length of the string is:", length)
main()

