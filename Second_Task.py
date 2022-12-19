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
# name = "restart"
# rest_str = name[1:]
# suspect_char = name[:1]
# for i in suspect_char:
#     if i == suspect_char:
#         print(suspect_char+rest_str.replace(suspect_char, "$"))

"""
5. Write a Python program to get a single string from two given strings, separated by a space and swap the 
first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz'
"""
# s1 = 'abc'
# s2 = 'xyz'
# s3 = s1.replace(s1[0], s2[0]).replace(s1[1], s2[1])
# s4 = s2.replace(s2[0], s1[0]).replace(s2[1], s1[1])
# lst = [s3, s4]
# new_string = ' '.join(lst)
# print(new_string)


"""
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
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
7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, 
if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
Sample String : 'The lyrics is not that poor!'
'The lyrics is poor!'
Expected Result : 'The lyrics is good!'
'The lyrics is poor!'
"""
# s1 = 'The lyrics is not that poor!'
# s2 = 'The lyrics is poor!'
# no = s1.find('not')
# poor = s1.find('poor')
# if poor > no > 0 and poor > 0:
#     s1 = s1.replace(s1[no:poor+4], 'good')
#
# print(s1)
# print(s2)

"""
8. Write a Python function that takes a list of words and returns the longest word and the length of the longest one. 
Sample Output:
Longest word: Exercises
Length of the longest word: 9
"""
# def return_length(lst=[]):
#     num = 0
#     for i in lst:
#         if len(i) > num:
#             num = len(i)
#
#     print("Longest String: " + str(num))
#
#
# return_length(['kanhaiya', 'bajrang', 'rahul'])

"""
9. Write a Python program to remove the nth index character from a nonempty string.
"""
# n = 4
# s1 = 'kanhaiya'
# new_string = ''
# for i in range(len(s1)):
#     if i != n:
#         new_string += s1[i]
# print(new_string)


"""
10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
"""
# s1 = 'Return'
# print(s1[-1:] + s1[1:-1] + s1[:1])

"""
11. Write a Python program to remove the characters which have odd index values of a given string.
"""
# s1 = "Kanhaiya"
# li = []
# for i in range(1, len(s1), 2):
#     li.append(i)
# for i, j in enumerate(s1):
#     for k in li:
#         if i == k:
#             s1.replace(j, '')
#             print(j, end="")


"""
12. Write a Python program to count the occurrences of each word in a given sentence.
"""
# s1 = 'how are you buddy, you are great!'
# print(s1.count('are'))

"""
13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
"""
# s1 = input("Enter the word: ")
# print(s1.upper(), s1.lower())

"""
14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words
in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
"""
# s1 = 'red, white, black, red, green, black'
# lst = s1.split(',')
# lst = sorted(list(set(lst)))
# s1 = ','.join(lst)
# print(s1)


"""
15. Write a Python function to create the HTML string with tags around the word(s).
Sample function and result :
add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
"""
# def add_tags(tag, word):
#     return "<%s>%s</%s>" % (tag, word, tag)
#
#
# print(add_tags('i', 'Python'))
# print(add_tags('b', 'Python Tutorial'))

"""
16. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
"""
def insert_string_middle(tag, word):
    return tag[:2] + word + tag[2:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))