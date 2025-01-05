
# # [Reverse Words in a Given String](https://www.geeksforgeeks.org/reverse-words-given-string-python/)


# Example:
# 
# **Input** : str =" geeks quiz practice code"
# 
# **Output** : str = code practice quiz geeks  
# 
# **Input** : str = "my name is laxmi"
# 
# **output** : str= laxmi is name my 


# The best efficeient way to do this is to use python built in slicing functions:


# A Short Summary of how slicing functions work in python:
# 
# Python string slicing is a powerful feature that allows us to extract substrings from strings. The syntax for string slicing is as follows:
# 
# 
# **General Syntax**: `[start:stop:step]`
# 
# **start**: The index where the slice begins (inclusive).
# 
# **stop**: The index where the slice ends (exclusive).
# 
# **step**: The1 interval between elements to be included in the slice
# 
# When both start and stop are omitted, it implies selecting the entire sequence.
# 
# `-1` as step: A negative step value indicates that the sequence should be traversed in reverse order.
# 


def reversed(s):
    reversed_str = s[::-1]
    return reversed_str
    

def main():
    s = input("Enter a string: ").lower()
    reversed_str = reversed(s)
    print("Reversed string is:", reversed_str)
    
main()


# But what about reason this function from first principles:


# 1. Frist we have to input a string
# 2. Then we convert the string to individual characters
# 3. Then we reverse those characters
# 4. Finally we convert  those characters back to string and print the result.


# 1. Taking a string from the user is been taken care of by the input function
# 2. Converting string to individual characters is done by looping over each character in the string and appending it to a list
# 4. Reversing the list is done by slicing the list in reverse order:
#     1. We can reverse the list by iterating over each character in the list (From the End back to beginning) and then appending each character individually to a new list of characters 
# 3. Converting list back to string is done by joining all the characters in the list with a space in between using the join function


# def to_list(s):
#     return list(s)
# Of course We would not go with the intutive option, we would go with the more complex one


# def to_list(s):
#     str_list = [char for char in s]
#     return str_list
# This also feel kind of straigt forward, we would go with the more complex one

def to_list(s):
    str_list = []
    for char in s:
        str_list.append(char)    
    return str_list
# This feels complicated enough for now



# def reversed(str_list):
#     reversed_str = "".join(str_list.pop() for i in range(len(str_list)))
#     return reversed_str
# This also feel kind of straigt forward, we would go with the more complex one

def reversed(str_list):
    reverse_list_str = []
    for i in range(len(str_list)):
        reverse_list_str.append(str_list.pop())
    return reverse_list_str


def to_string(reverse_list_str):
    return "".join(reverse_list_str)
# This feels complicated enough for now


def main():
    s = input("Enter a string: ").lower()
    str_list = to_list(s)
    print(str_list)
    reverse_list_str = reversed(str_list)
    print(reverse_list_str)
    reversed_str = to_string(reverse_list_str)
    print("Reversed string is:", reversed_str)
    
main()


# What about doing the same thing but for a whole scentence:



# def split(s):
#     return s.split()  
# Of course We would not go with the intutive option, we would go with the more complex one


def split(s):
    words = []
    word = []
    for i in s:
        if i == " ":
            words.append("".join(word))
            word = []
        else:
            word.append(i)
    if word:  
        words.append("".join(word)) 
    return words


def reversed(str_list):
    reverse_list_str = []
    for i in range(len(str_list)):
        reverse_list_str.append(str_list.pop())
    return reverse_list_str


def to_string(reverse_list_str):
    return " ".join(reverse_list_str)
# This feels complicated enough for now


def main():
    s = input("Enter a string: ").lower()
    str_list = split(s)
    print(str_list)
    reverse_list_str = reversed(str_list)
    print(reverse_list_str)
    reversed_str = to_string(reverse_list_str)
    print("Reversed string is:", reversed_str)
    
main()








