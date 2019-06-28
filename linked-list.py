# Linked List

class Node:

    def __init__(self, elem):
        # Node will contain one element and point to the next one
        self.elem = elem
        self.next = None


class LinkedList:
    
    COUNT = 0

    def __init__(self):
        self.head = None
        self.tail = None
        self.COUNT = 0

    def add(self, item):
        # assign the first item to a Node which will be the head
        if self.head is None:
            self.COUNT += 1
            self.head = Node(item)
            # initially also set the head to be the tail
            self.tail = self.head

        else:
            self.COUNT += 1
            # assign the next item to the next Node following the tail
            self.tail.next = Node(item)
            # and make this item the new tail
            self.tail = self.tail.next

    def delete(self, item):
        if self.head is None:
            return "The list is empty"
        # If the elem in the first Node is the item, return it and set the next node to be the new head
        elif self.head.elem is item:
            self.COUNT -= 1
            self.head = self.head.next
            return "Head removed "+str(item)
        else:
            current_element = self.head
            # Start of loop. Check if the next element is not None and is not the item
            while current_element.next is not None and current_element.next.elem is not item:
                current_element = self.head.next
            if current_element.next is None:
                return "Item is not in the list"
            else:
                self.COUNT -= 1
                # return the item and set the node to skip the node
                current_element.next = current_element.next.next
                return item
            
    def length(self):
        return "Length: "+str(self.COUNT)

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False
