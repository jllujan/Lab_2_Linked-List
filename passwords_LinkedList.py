class Node (object):
    password = ""
    count = -1
    next = None

    # Constructor for a Node
    def __init__(self, password, count, next):
        self.password = password
        self.count = count
        self.next = next


# Linked List class.
class LinkedList:

    #Constructor for a Linked List
    def __init__(self):
        self.head = None
        return

    #Add a Node to a linked list
    def add(self, value):
        if self.head is None:
            self.head = Node(value, 1, None)
            return

        current = self.head

        #If head is not None, it will be added at the end of the list.
        while current is not None:
            #Check if password is already present on the list
            if current.password == value:
                current.count = current.count + 1
                return
            if current.next is None:
                current.next = Node(value, 1, None)
                return
            current = current.next

    # Print the whole linked list and the number of times each password is repeated
    def print(self):
        temp = self.head

        while temp is not None:
            print(temp.password + " " + str(temp.count))

            temp = temp.next

        return

    # Returns the length of the linked list
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count = count + 1
            current = current.next

        return count


# Function that reads a .txt file and creates a linked list out of it.
def solution_a(file_name):
        pw_list = LinkedList()

        # Open file and read first line
        file = open(file_name, "r")
        line = file.readline()

        # Loop will go trough every line in the file
        while line:
            # Creates an array that holds the username and the password
            user_and_password = line.split()

            # Check if there is a password and adds it.
            if len(user_and_password) > 1:
                pw_list.add(user_and_password[1])
            line = file.readline()

        # Returns Linked List
        return pw_list.head


# Function that creates a dictionary out of a .txt file.
def solution_b(file_name):
    pw_dict = {}

    # Open file and read first line.
    file = open(file_name, "r")
    line = file.readline()

    # Loop will go through file until there are no lines left.
    while line:
        # Creates an array to hold username and password.
        user_and_password = line.split()

        # Checks if a password exists
        if len(user_and_password) > 1:
            # Checks if password is already present in dictionary
            if user_and_password[1] in pw_dict:
                pw_dict[user_and_password[1]] = pw_dict[user_and_password[1]] + 1
            else:
                pw_dict[user_and_password[1]] = 1
        line = file.readline()

    # Returns dictionary
    return pw_dict


# Function that sorts linked list using Bubble Sort Algorithm
def bubble_sort(pw_list):

    # Loop will go through the whole linked list.
    for i in range(pw_list.length()):
        j = 0
        current = pw_list.head
        prev = pw_list.head
        # Loop will only check for items that have not been sorted already.
        while j < pw_list.length() - i and current.next is not None:
            # Case for when comparing head and head.next
            if prev is current:
                if current.count < current.next.count:
                    temp = current.next
                    current.next = current.next.next
                    temp.next = current
                    current = temp
                    prev = current
                current = current.next

            # Case for when comparing any node and node.next
            if current.count < current.next.count:
                temp = current.next
                current.next = current.next.next
                temp.next = current
                prev.next = temp
                current = temp

            current = current.next
            prev = prev.next
            j = j + 1

    # Return sorted linked list
    return pw_list


# Function that returns the middle element in a linked list
def middle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        if fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        fast = fast.next
    return slow

# Function merges and sorts two lists. Part of the merge sort algorithm
def merge_and_sort(list1, list2):
    sorted_list = Node("", 0, None)
    temp_head = sorted_list

    # checks if any list is empty
    if list1 is None:
        sorted_list.next = list2
    if list2 is None:
        sorted_list.next = list1

    # Merges lists according to their value (sorting them).
    while list1 is not None or list2 is not None:
        if list1 is None:
            sorted_list.next = list2
            list2 = list2.next
        elif list2 is None:
            sorted_list.next = list1
            list1 = list1.next
        else:
            if list1.count <= list2.count:
                sorted_list.next = list1
                list1 = list1.next
            sorted_list.next = list2
            list2 = list2.next
        sorted_list = sorted_list.next
    sorted_list = temp_head.next

    return sorted_list

# Function that uses recursion to sort a linked list following the merge sort algorithm.
def merge_sort(head):
    # Base cases
    if head is None:
        return None
    if head.next is None:
        return head
    else:
        # Finds middle element
        mid = middle(head)
        # Sets the head for second list
        after_middle = mid.next
        mid.next = None

        # Recursive call to divide lists until each list is a single element
        left = merge_sort(head)
        right = merge_sort(after_middle)

        # Merge each pair of lists
        sorted_list = merge_and_sort(left, right)
        return sorted_list


# Testing Solution A
pw_list = solution_a("test1.txt")
current = pw_list

print()
print(" *** PRINTING LINKED LIST *** ")
print()
# Loop prints list gotten from solution A
while current is not None:
    print(current.password + " " + str(current.count))
    current = current.next


# Testing Solution B
pw_dict = solution_b("test1.txt")

print()
print(" *** PRINTING DICTIONARY *** ")
print()

# Loop prints dictionary gotten from solution B
for k, v in pw_dict.items():
    print(k, v)