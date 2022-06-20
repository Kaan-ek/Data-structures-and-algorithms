class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.heigth = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
        print('Bottom reached.\n')

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.heigth += 1
        return True

    def pop(self):
        if self.top == None:
            return False
        temp = self.top.next
        self.top.next = None
        self.top = temp
        self.heigth -= 1

my_stack = Stack(2)
my_stack.print_stack()

my_stack.push(1)
my_stack.push(0)
my_stack.push(-1)
my_stack.push(-2)
my_stack.print_stack()

my_stack.pop()
my_stack.pop()
my_stack.print_stack()