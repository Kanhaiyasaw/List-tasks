"""
1. Write a Python program to calculate the length of a string.
"""
# name = "kanhaiya"
# print(len(name))

"""
2. Write a Python program to count the number of characters (character frequency) in a string.
Sample String : google.com'
Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
"""
# url = "google.com"
# dictionary = {}
# for i, j in enumerate(url):
#     dictionary[j] = i
# print(dictionary)


"""
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
If the string length is less than 2, return instead of the empty string.
Sample String : 'w3resource'
Expected Result : 'w3ce'
Sample String : 'w3'
Expected Result : 'w3w3'
Sample String : ' w'
Expected Result : Empty String
"""
# name = "Kanhaiya"
#
# for i, j in enumerate(name):
#     if len(name) < 2 :
#         print("empty String")
#     elif i > 1:


"""
4. Write a Python program to get a string from a given string where all occurrences of 
its first char have been changed to '$', except the first char itself. 
Sample String : 'restart'
Expected Result : 'resta$t'
"""
name = "restart"
suspect_char = name[:1]
for i in name:
    if i == suspect_char:
        print(i)
        continue

    # temp = name.replace(suspect_char, "$")

"""
Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
If the given string already ends with 'ing' then add 'ly' instead. 
If the string length of the given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
"""
# name = "ac"
# check = name[-3:]
# if len(name) == 3:
#     print(name + "ing")
# elif check == "ing":
#     print(name + "ly")
# else:
#     print("Empty String")

"""

"""
