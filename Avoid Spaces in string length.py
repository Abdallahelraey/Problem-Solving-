# [Avoid Spaces in string length](https://www.geeksforgeeks.org/python-avoid-spaces-in-string-length/)

# **Example**

# Given a String, compute all the characters, except spaces.

# Input : test_str = ‘geeksforgeeks 33 best’ 

# Output : 19 

# Explanation : Total characters are 19. 


# Input : test_str = ‘geeksforgeeks best’ 

# Output : 17 

# Explanation : Total characters are 17 except spaces.



# def str_char_len(s: str):
#     char_len = 0
#     for i in s:
#         if i!=' ':  # check if character is not a space
#             char_len += 1
#     return char_len
# This function was the simplest way to calculate the number of characters in a string without spaces


# def str_char_len(s: str):
#     for char in s:
#         if char == " ":
#             continue 
#         char_len += 1
#     return char_len
# Another way to impliment the same thing using loops


# def str_char_len(s: str):
#     char_len = len(s.replace(" ", ""))
#     return char_len
# This function is the most straigt forward way to calculate the number of characters in a string without spaces
    

def str_char_len(s: str):
    return sum(1 for char in s if char != " ") 
# This function is not complicated but confusing if you are not familiar with python generator expression syntax You can refer to `list_comperhension & generator expression.ipynb` in hte materials directoty to learn more about that...


def main():
    s = input("Enter a string: ").lower()
    char_len = str_char_len(s)
    print("Number of characters in the string is:", char_len)

if __name__ == "__main__":
    main()
    