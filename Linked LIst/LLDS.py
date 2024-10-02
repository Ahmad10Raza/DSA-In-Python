class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Algorithm to add elements at beginning of the linked list
    # 1. Create a new node
    # 2. Make the next of the new node as head
    # 3. Move the head to point to the new node
    
    # Time complexity: O(1)
    # Space complexity: O(1)
    
    def insertAtBeginning(self, data):
        new_node = Node(data) # Create a new node
        new_node.next = self.head # Make the next of the new node as head
        self.head = new_node # Move the head to point to the new node
        
    # Algorithm to Insert a new node at the end of the linked list
    # 1. Create a new node
    # 2. If the linked list is empty, then make the new node as head
    # 3. Else, traverse the linked list till the last node
    # 4. Change the next of the last node to the new node 
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    # Algorithm for Inserting a new node after a given position
    # 1. Create a new node
    # 2. Traverse the linked list till the given position
    # 3. Change the next of the new node to the next of the current node
    # 4. Change the next of the current node to the new node
    
    # Time complexity: O(n)
    # Space complexity: O(1)
    
    def getLength(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count
    
    def insertAtIndex(self, index, data):
        if index < 0 or index > self.getLength():
            print("Invalid index")
            return
        if index == 0:
            self.insertAtBeginning(data)
            return
        count = 0
        new_node = Node(data)
        current_node = self.head
        while count < index - 1:
            current_node = current_node.next
            count += 1
        new_node.next = current_node.next # Change the next of the new node to the next of the current node
        current_node.next = new_node # Change the next of the current node to the new node
        
      
      
    # Function to delete a node at the beginning of the list

    # Input: LinkedList = 1->2->3->4->5
    # Output: LinkedList = 2->3->4->5
    
    # Algorithm to delete a node at the beginning of the linked list
    # 1. Move the head to the next of the current head
    
    def deleteAtBeginning(self):
        if self.head is None:
            print("Linked list is empty")
            return
        self.head = self.head.next
    
        
    # Function to delete a node at the end of the list

    # Input: LinkedList = 1->2->3->4->5
    # Output: LinkedList = 1->2->3->4
    
    # Algorithm to delete a node at the end of the linked list
    # 1. Traverse the linked list till the second last node
    # 2. Change the next of the second last node to None
    
    def deleteAtEnd(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
    
    
    # Function to delete a node at a given index
    
    # Input: LinkedList = 1->2->3->4->5
    # Output: LinkedList = 1->2->4->5
    
    # Algorithm to delete a node at a given index
    # 1. Traverse the linked list till the given index
    # 2. Change the next of the previous node to the next of the current node
    
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.getLength():
            print("Invalid index")
            return
        if index == 0:
            self.deleteAtBeginning()
            return
        current_node = self.head
        count = 0
        while count < index - 1:
            current_node = current_node.next
            count += 1
        current_node.next = current_node.next.next
        
        
    # Function to get data at a given index
    
    # Input: LinkedList = 1->2->3->4->5 , index = 2
    # Output: 3
    
    # Algorithm to get data at a given index
    # 1. Traverse the linked list till the given index
    # 2. Return the data of the current node
    
    def getDataAtIndex(self, index):
        if index < 0 or index >= self.getLength():
            print("Invalid index")
            return
        current_node = self.head
        count = 0
        while count < index:
            current_node = current_node.next
            count += 1
        return current_node.data
    
        
        
        

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBeginning(1)
    ll.insertAtBeginning(2)
    ll.insertAtBeginning(3)
    ll.print_list()
    
    # Usage of InertAtEnd
    ll.insertAtEnd(4)
    ll.insertAtEnd(5)
    ll.print_list()
   
   # Usage of InsertAtIndex
    ll.insertAtIndex(2, 6)
    ll.print_list()
    ll.insertAtIndex(0, 7)
    ll.print_list()
    ll.insertAtIndex(7, 8)
    ll.print_list()
    ll.insertAtIndex(10, 9)
    ll.print_list()