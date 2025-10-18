class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_end(self, data):
        new = Node(data)
        if self.head == None:
            self.head = new
            return
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = new

    def add_middle(self, position, data):
        new = Node(data)
        temp = self.head
        index = 0
        while temp != None and index < position - 1:
            temp = temp.next
            index += 1
        if temp == None:
            return
        new.next = temp.next
        temp.next = new

    def show(self):
        temp = self.head
        while temp != None:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Kullanım
ll = LinkedList()
ll.add_end(10)
ll.add_end(20)
ll.add_end(40)
ll.add_middle(1, 30)  # 1. pozisyona 30 ekle
ll.show()


stack = []

def push(x):
    stack.append(x)

def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        return None

def peek():
    if len(stack) > 0:
        return stack[-1]
    else:
        return None

def show():
        print(stack)

# En az 15 işlem
push(10)
push(20)
push(30)
push(40)
push(50)
push(60)
push(70)
push(80)
push(90)
push(100)
pop()
pop()
push(110)
push(120)
peek()
push(130)
show()
