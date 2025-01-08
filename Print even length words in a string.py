# [Print even length words in a string](https://www.geeksforgeeks.org/python-program-to-print-even-length-words-in-a-string/)

# Given a string. The task is to print all words with even length in the given string.

# **Examples:**

# Input: s = "This is a python language"

# Output: This is python language

# Input: s = "i am laxmi"

# Output: am

# def even_len_str(s):
#     words = s.split()
#     even_words = []
#     for word in words:
#         if len(word) % 2 == 0:
#             even_words.append(word) 
#     return " ".join(even_words)
# this is the most straigt forward way to get the even length words in a string



# def even_len_str(s):
#     return " ".join(word for word in s.split() if len(word) % 2 == 0)
# the most concise way to get the even length words in a string



# Watch out for this one (As it is the most complicated way to get the even length words in a string)
def even_len_str(s):
    words = s.split()
    even_words = list(filter(lambda x: (len(x)%2==0),words))
    return " ".join(even_words)

def main():
    s = input("Enter a string: ").lower()
    even_words = even_len_str(s)
    print("Even length words in the string are:", even_words)


if __name__ == "__main__":
    main()