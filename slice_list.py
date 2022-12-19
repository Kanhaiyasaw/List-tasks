# # slice List
# lst = [1, 2, 5, 6]
# print(lst[1:])


# # Square of 1 to 30
# # get First and last 5 Item
# lst = []
# for i in range(1, 30):
#     lst.append(i**2)
# print(lst)
# print("First Five Item: ", lst[:5])
# print("Last Five Item: ", lst[-5:])

"""
Tuple Two Methods 1. count()
                  2. index()
"""

# # Count method in tuple
# vehicle = ('car', 'bike', 'cycle', 'bike')
# count_item = vehicle.count('bike')
# print(count_item)

# # index method in tuple
# vehicle = ('car', 'bike', 'cycle', 'bike')
# index_item = vehicle.index('bike')
# print(index_item)

"""
Write a Python program to sum all the items and multiplies all the items in a list.
"""
# sum Of the all item
# lst = [20, 30, 10, 15]
# total = 0
# i = 0
# while i < len(lst):
#     total = total + lst[i]
#     i += 1
# print(total)


# Multiplies The item
# lst = [20, 30, 10, 15]
# total = 1
# i = 0
# while i < len(lst):
#     total = total * lst[i]
#     i += 1
# print(total)

"""
Write a Python program to get the largest and smallest number from a list.
"""
# lst = [10, 20, 15, 5, 50, 45]
# print(max(lst))
# print(min(lst))


"""
Write a Python program to generate all sublist of a list
"""
# lst = [10, [10, 20], 25, [15, 25, 32]]
# print(lst)
# print(lst[1])


"""
Write a Python program to sum all the items in a list.
"""
# sum Of the all item
# lst = [20, 30, 10, 15]
# total = 0
# i = 0
# while i < len(lst):
#     total = total + lst[i]
#     i += 1
# print(total)


"""
Write a Python program to multiply all the items in a list.
"""
# lst = [20, 30, 10, 15]
# total = 1
# i = 0
# while i < len(lst):
#     total = total * lst[i]
#     i += 1
# print(total)


"""
Write a Python program to get the largest number from a list.
"""
# lst = [10, 20, 15, 5, 50, 45]
# print(max(lst))


"""
Write a Python program to get the smallest number from a list.
"""
# lst = [10, 20, 15, 5, 50, 45]
# print(min(lst))


"""
Write a Python program to count the number of strings where the string length is 2 or more and the first and last 
character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221'] 
Expected Result : 2 
"""
# lst = ['abc', 'xyz', 'aba', '1221']
# for i in lst:
#     if len(i) >= 2 and i[0] == i[len(i)-1]:
#         print(i)


"""
Write a Python program to get a list, sorted in increasing order by the 
last element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
"""
# lst = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# lst.sort()
# print(lst)


"""
Write a Python program to remove duplicates from a list.
"""
# lst = [1, 2, 5, 9, 1, 2, 3]
# lst_another = set(lst)
# print(list(lst_another))


"""
Write a Python program to check a list is empty or not.
"""

# lst = [20, 50, 12, 15]
# if len(lst) == 0:
#     print("List is Empty.")
# else:
#     print("List is not empty")


"""
Write a Python program to clone or copy a list.
"""
# lst = [1, 2, 3]
# lst_another = lst.copy()  # Copy the value
# print("After copied: ", lst_another)


"""
Write a Python program to find the list of words that are longer than n from a given list of words.
"""
# n = int(input("Enter the length : "))
# lst = ['Car', 'Bike', 'Motorcycle']
# for i in lst:
#     if len(i) >= n:
#         print(i)


"""
Write a Python function that takes two lists and returns True if they have at least one common member.
"""
# def compare_list_item(l1=[],
#                       l2=[]
#                       ):
#     for i in l1:
#         if i in l2:
#             print("True")
#         else:
#             print("false")
#         break
#
#
# compare_list_item([20, 30, 40],
#                   [10, 5, 25]
#                   )


"""
Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
"""
# lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# lst.remove(lst[5])
# lst.remove(lst[4])
# lst.remove(lst[0])
# print(lst)


"""
Write a Python program to generate a 3*4*6 3D array whose each element is *.
"""
# array = [[['*' for col in range(6)] for col in range(4)] for row in range(3)]
# print(array)


"""
Write a Python program to print the numbers of a specified list after removing even numbers from it.
"""
# lst = [12, 15, 10, 18, 11, 20]
# for i in range(2, 30, 2):
#     if i in lst:
#         lst.remove(i)
# print(lst)


"""
Write a Python program to shuffle and print a specified list
"""
# import random
# lst = ['red', 'yellow', 'Blue', 'Black', 'white']
# random.shuffle(lst)
# print(lst)


"""
Write a Python program to generate and print a list of first and last 5 elements where the values
are square of numbers between 1 and 30 (both included).
"""
# lst = []
# for i in range(1, 30):
#     lst.append(i**2)
# print(lst)
# print("First Five Item: ", lst[:5])
# print("Last Five Item: ", lst[-5:])


"""
Write a Python program to generate and print a list except for the first 5 elements, where the 
values are square of numbers between 1 and 30 (both included).
"""
# lst = []
# for i in range(1, 30):
#     lst.append(i**2)
# print(lst)
# print("First Five Item: ", lst[:5])


"""
Write a Python program to generate all permutations of a list in Python.
"""
"""
Write a Python program to get the difference between the two lists.
"""
# lst1 = [1, 3, 5, 6, 10]
# lst2 = [1, 3, 5, 6, 10]
# lst3 = [3, 6, 8, 8, 22]
# if lst1 == lst2:
#     print('True lst1 == lst2')
# else:
#     print("False")
# if lst2 <= lst3:
#     print("True lst2 <= lst3")
# else:
#     print("False")


"""
Write a Python program access the index of a list.
"""
# lst = [10, 50, 30, 15, 40]
# print(lst)
# user_input = int(input("value index which you want to know: "))
# ind = lst.index(user_input)  # return index of that value
# print("Index Is :", ind)


"""
Write a Python program to convert a list of characters into a string.
"""
# lst = ['a', 'b', 'c']
# print(lst)
# store_string = str(lst)
# print(type(store_string))
# print(store_string)


"""
Write a Python program to find the index of an item in a specified list.
"""
# lst = [10, 50, 30, 15, 40]
# print(lst)
# user_input = int(input("value index which you want to know: "))
# ind = lst.index(user_input)  # return index of that value
# print("Index Is :", ind)

"""
Write a Python program to flatten a shallow list.
"""
# list1 = [1, 2, 5, 9]
# list2 = [4, 3, 8, 7]
# list1.extend(list2)
# print(list1)


"""
Write a Python program to append a list to the second list.
"""
# list1 = [1, 2, 5, 9]
# list2 = [4, 3, 8, 7]
# list1.extend(list2)
# print(list1)


"""
Write a Python program to select an item randomly from a list.
"""
# import random
# lst = ['red', 'yellow', 'Blue', 'Black', 'white']
# print(lst[random.randrange(len(lst))])


"""
Write a python program to check whether two lists are circularly identical.
"""

"""
Write a Python program to find the second smallest number in a list.
"""
# list1 = [12, 22, 5, 9]
# print(list1)
# list1.sort()
# print("Second Smallest NUmber: ", list1[1])


"""
Write a Python program to find the second largest number in a list.
"""
# list1 = [12, 22, 5, 9]
# list1.sort()
# print(list1)
# print("Second Smallest NUmber: ", list1[-2])


"""
Write a Python program to get unique values from a list.
"""
# lst = [10, 50, 10, 20, 50, 20, 15]
# print(list(set(lst)))


"""
Write a Python program to get the frequency of the elements in a list.
"""
# lst = [10, 15, 20, 15, 10, 10, 20]
# print(lst.count(10))


"""
Write a Python program to count the number of elements in a list within a specified range.
"""
# lst = [10, 15, 20, 15, 10, 10, 20]
# clone = []
# for i in range(5):
#     clone.append(lst[i])
# print(clone.count(10))


"""
Write a Python program to check whether a list contains a sublist.
"""
# lst = [10, 5, 20, 50]
# lst2 = [5]
# flag = False
# for i in lst2:
#     if i in lst:
#         flag = True
#     else:
#         flag = False
#         break
# if flag:
#     print("True")
# else:
#     print("False")


"""
Write a Python program to generate all sublists of a list.
"""
# lst = [10, 5, 20, 50]
# lst2 = [5, 11]
# list_another = []
# for i in lst2:
#     if i in lst:
#         list_another.append(i)
#     else:
#         continue
#
# print(list_another)

"""
Write a Python program using Sieve of Eratosthenes method for computing primes upto a specified number. 
Note: In mathematics, the sieve of Eratosthenes, (Ancient Greek: κόσκινον Ἐρατοσθένους, kóskinon Eratosthénous) 
one of a number of prime number sieves, is a simple, ancient algorithm for finding all prime numbers up to any 
given limit.
"""

"""
Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
Sample list : ['p', 'q']
n =5
Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
"""
# lst = ['p', 'q','r']
# x = 5
# sample_list = []
# lst1 = lst*x
# lst2 = []
# for i in range(1, x+1):
#     for j in lst:
#         lst2.append(i)
# for i in range(len(lst)*x):
#     sample_list.append(lst1[i] + str(lst2[i]))

# print(sample_list)


"""
Write a Python program to get variable unique identification number or string.
"""
# lst1 = [2, 4, 6, 8, 1, 2, 5, 8]
# lst2 = ['red', 'blue', 'black', 'red', 'blue']
#
# unique_lst1 = list(set(lst1))
# unique_lst2 = list(set(lst2))
#
# print(lst1)
# print(lst2)

# lst = [0, 3, 4, 6]
# for i, c in enumerate('Krishna'):
#     for j in range(len(lst)):
#         if lst[j] == i:
#             print(c, end=" ")


"""
Write a Python program to find common items from two lists.
"""
# lst1 = [15, 20, 30, 55, 12]
# lst2 = [12, 18, 20, 50, 30]
# for i in lst1:
#     if i in lst2:
#         print(i, end=" ")

"""
Write a Python program to change the position of every n-th value with the (n+1)th in a list.
Sample list: [0,1,2,3,4,5]
Expected Output: [1, 0, 3, 2, 5, 4]
"""
# lst = ['0', "1", "2", "3", "4", "5"]
# emt = []
# for i in range(0, len(lst), 2):
#     lst[i], lst[i + 1] = lst[i + 1], lst[i]
# print(lst)


"""
Write a Python program to convert a list of multiple integers into a single integer. Go to the editor
Sample list: [11, 33, 50]
Expected Output: 113350
"""
# lst = ["11", "33", "50"]
# for i in lst:
#     print(i, end="")


"""
Write a Python program to split a list based on first character of word.
"""
# from itertools import groupby
# from operator import itemgetter
#
# word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
#      'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
#
# for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
#     print(letter)
#     for word in words:
#         print(word)