"""
Write a Python script for below List Functions. 1) append
                                                2) extend
                                                3) insert
                                                4) remove
                                                5) pop

"""


# performing append operation on the list
def append_operation():
    lst = []
    user_input = input("Enter the values which you want to append in the list: ")
    lst.append(user_input)  # append method is store the value on the last of list
    print(lst)


# performing extend operation on the list
def extend_operation():
    lst1 = ['2', '10']
    lst2 = ['11', '25']
    print("List1: ", lst1)
    print("List2: ", lst2)
    lst1.extend(lst2)  # extend method is store the value on the last of list
    print("List After extend : ", lst1)


# performing insert operation on the list
def insert_operation():
    lst = ['10', '60', '25']
    print(lst)
    print("Enter the values and position which you want to insert in specific position on the list")
    user_input = input("Value: ")
    pos = int(input("Position: "))
    lst.insert(pos, user_input)  # insert method is store the value on specific index on list
    print(lst)


# performing remove operation on the list
def remove_operation():
    lst = ['10', '60', '25']
    print(lst)
    user_input = input("Enter the value which you want to remove  on the list")
    lst.remove(user_input)  # append method is store the value on the last of list
    print(lst)


# performing pop operation on the list
def pop_operation():
    lst = ['10', '60', '25']
    print(lst)
    lst.pop()  # pop method is remove the value on the last of list
    print(lst)


# Some choose option On that
print("Enter your Choice which you want to perform operation on list ")
print("1. append")
print("2. extend")
print("3. insert")
print("4. remove")
print("5. pop")
choice = input("Enter you Choice what you want to perform(1 to 5): ")
if choice == '1':
    append_operation()
elif choice == '2':
    extend_operation()
elif choice == '3':
    insert_operation()
elif choice == '4':
    remove_operation()
elif choice == '5':
    pop_operation()
else:
    print("Your Choice is out of options....")
