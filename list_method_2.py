"""
Write a Python script for below List Functions. 1) clear
                                                2) index
                                                3) count
                                                4) sort
                                                5) reverse
                                                6) copy
"""
# public variable
lst = ['10', '20', '10', '30', '20']


# performing clear operation on the list
def clear_operation():
    print(lst)
    lst.clear()  # list will be empty
    print(lst)


# performing index operation on the list
def index_operation():
    print(lst)
    user_input = input("value index which you want to know: ")
    ind = lst.index(user_input)  # return index of that value
    print(ind)


# performing count operation on the list
def count_operation():
    print(lst)
    user_input = input("value which you want to count: ")
    co = lst.count(user_input)  # return the number of item in the list
    print(co)


# performing remove operation on the list
def sort_operation():
    number = [20, 15, 5]
    print(number)
    number.sort()
    print("Sorted: ", number)


# performing pop operation on the list
def reverse_operation():
    print(lst)
    lst.reverse()
    print("Reverse order: ", lst)


def copy_operation():
    print(lst)
    lst_another = lst.copy()  # Copy the value
    print("After copied: ", lst_another)


# Some choose option On that
print("Enter your Choice which you want to perform operation on list ")
print("1. clear")
print("2. index")
print("3. count")
print("4. sort")
print("5. reverse")
print("6. copy")
choice = input("Enter you Choice what you want to perform(1 to 6): ")
if choice == '1':
    clear_operation()
elif choice == '2':
    index_operation()
elif choice == '3':
    count_operation()
elif choice == '4':
    sort_operation()
elif choice == '5':
    reverse_operation()
elif choice == '6':
    copy_operation()
else:
    print("Your Choice is out of options....")
