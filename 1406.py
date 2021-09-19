# from sys import stdin, stdout
# from itertools import islice
# from copy import deepcopy

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# string = stdin.readline().strip()
# head = Node(string[0])
# left_node = head
# for char in islice(string, 1, None):
#     node = Node(char)
#     node.left = left_node
#     left_node.right = node
#     left_node = node
# tail = left_node
# cursor = deepcopy(tail)

# m = int(stdin.readline())
# for command in (stdin.readline().strip() for _ in range(m)):
#     if command == 'L':
#         if cursor != head:
#             cursor = cursor.left
#     elif command == 'D':
#         if cursor != tail:
#             cursor = cursor.right
#     elif command == 'B':
#         if cursor == head:
#             cursor.right.left = None
#             cursor = cursor.right
#             head = cursor
#         elif cursor == tail:
#             cursor.left.right = None
#             cursor = cursor.left
#         else:
#             cursor.left.right = cursor.right.left
#     else:
#         char = command[2]
#         node = Node(char)
#         if cursor == head:
#             node.right = cursor
#             cursor.left = node
#         elif cursor == tail:
#             node.left = cursor
#             cursor.right = node

#         node.left = cursor
#         node.right = cursor.right
#         cursor = node

# current = head
# while True:
#     stdout.write(current.value)

#     if current.right is None:
#         break

from itertools import islice, repeat
from sys import stdin, stdout

class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Cursor():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def backward(self):
        if self.left is not None:
            self.right = self.left
            self.left = self.left.left
    
    def forward(self):
        if cursor.right is not None:
            cursor.left = cursor.right
            cursor.right = cursor.right.right

string = stdin.readline().strip()
head = Node(string[0])
left = head
for char in islice(string, 1, None):
    node = Node(char)
    node.left = left
    left.right = node
    left = node

cursor = Cursor(left, None)

m = int(stdin.readline())
for query in (stdin.readline().strip() for _ in range(m)):
    if query == 'L':
        cursor.backward()
    elif query == 'D':
        cursor.forward()
    elif query == 'B':
        if cursor.left is not None:
            if cursor.left == head:
                cursor.right.left = None
                cursor.left = None
                head = cursor.right
            else:
                if cursor.right is not None:
                    cursor.right.left = cursor.left.left
                cursor.left.left.right = cursor.right
                cursor.left = cursor.left.left
    else:
        char = query[2]
        node = Node(char)
        if cursor.left is None:
            head = node
        else:
            node.left = cursor.left
            cursor.left.right = node
        node.right = cursor.right
        if cursor.right is not None:
            cursor.right.left = node
        cursor.left = node

current = head
while True:
    stdout.write(current.value)
    
    if current.right is None:
        break
    current = current.right
    
stdout.write('\n')
stdout.flush()