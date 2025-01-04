## [Python program to check whether the string is Symmetrical or Palindrome](https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar)


# Given a string. the task is to check if the string is symmetrical and
# palindrome or not. A string is said to be symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if one half of the string is the reverse of the other half or if a string appears the same when read forward or backward.


# ---
# Example

# Input: khokho

# Output:

# The entered string is symmetrical

# The entered string is not palindrome

# Input:amaama

# Output:

# The entered string is symmetrical

# The entered string is palindrome

# ---

# Approach:

# 1. Convert the given string into lowercase.
# 2. Check if the given string is symmetrical or not.
# 3. Check if the given string is a palindrome or not.
# 4. Print the output.

# ---

# Program

def split_string(string):
    length = len(string)
    if length % 2 == 0:
        return string[:length // 2], string[length // 2:]
    else:
        return string[:length // 2], string[length // 2 + 1:]

def check_symmetry(s):
    part_1, part_2 = split_string(s)
    return part_1 == part_2

def check_palindrome(s):
    part_1, part_2 = split_string(s)
    return part_1 == part_2[::-1]

# Usage
def main():
    s = input("Enter a string: ").lower()
    if check_symmetry(s):
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
    
    if check_palindrome(s):
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

        
# Driver code
if __name__ == "__main__":
    main()
