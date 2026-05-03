class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class ListaCircular:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node=Node(data)
        self.head=new_node
        new_node.next=self.head

    def insert_at_first(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_end(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        
        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head is None:
            print("Empty list")
            return

        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(back to head)")
    
    def search(self, value):
        if self.head is None:
            return False

        current = self.head
        while True:
            if current.data == value:
                return True

            current = current.next
            if current == self.head:
                break

        return False

    





