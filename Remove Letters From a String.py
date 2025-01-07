# # [Remove Letters From a String](https://www.geeksforgeeks.org/ways-to-remove-ith-character-from-string-in-python/)


# Removing letters or specific characters from a string in Python can be done in several ways.
# 
# 
# But Python strings are immutable, so removal operations cannot be performed in-place. Instead, they require creating a new string, which uses additional memory.


# ----
# 📚 Before you continue, I would like to recommend refering to the `( Mutable and immutable)(Primative and Non-primitive).ipynb` tutorial first before you continue with this one.


# ---
# The immutability of Python strings directly relates to how you remove characters from them:
# 
# * **Immutability:** Strings in Python are immutable, meaning they cannot be changed after they are created. When you "remove" a character, you're not actually modifying the original string.
# * **Creating a New String:** To remove a character, you create a new string that excludes the desired character(s). This is because the original string cannot be altered.
# * **Memory Implications:** Creating a new string requires allocating new memory to store the modified version. This is why string manipulation in Python often involves creating multiple intermediate strings, which can have memory implications, especially with large strings.
# 
# **Example:**
# 
# ```python
# original_string = "hello world"
# new_string = original_string.replace("l", "") 
# 
# # original_string remains unchanged: "hello world"
# # new_string is a new string: "heo word" 
# ```
# 
# In this example, `replace()` doesn't modify `original_string`. Instead, it creates a new string (`new_string`) where all occurrences of "l" are removed.
# 
# **Key takeaway** The immutability of strings in Python influences how string manipulation operations are performed, requiring the creation of new strings rather than modifying existing ones in-place.
# 


# The following code is to remove a character from a string in the most simple way possible

# def rem_char(s, char):
#     new_str = s.replace(char, "")
#     return new_str

# But as always, we need to go with the more complex one

# def rem_char(s, char):
#     new_str = ""
#     for i in s:
#         if i!= char:
#             new_str += i
#     return new_str

# Thinking also about convertign it to LIST if you are planning to have more of one manpulation is a good idea
# def rem_char(s, char):
#     new_str = []
#     for i in s:
#         if i!= char:
#             new_str.append(i)
#     return "".join(new_str)

# Talking about LISTS, we can also use the list comprehension to make it comprehensionally complicated
# def rem_char(s, char):
#     new_str = [i for i in s if i!= char] 
#     return "".join(new_str)


# Talking about list comprehension, we can also use lambda to make our comprehensional complication functional

rem_char = lambda s, char: ''.join(i for i in s if i != char)
# If feel like this is not complicated enough you can refer to `what_is_the_lamda_function.ipynb` in the Materials directory to find out more about closures and enclosing scopes.

def main():
    s = input("Enter a string: ").lower()
    char = input("Enter a character to remove: ").lower()
    new_str = rem_char(s, char)
    print("New string is:", new_str)
    
main()