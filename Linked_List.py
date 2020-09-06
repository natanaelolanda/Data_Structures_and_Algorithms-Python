class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        string = ''
        current = self.head
        while current:
            string += str(current.value)
            string += ', ' if current.next else '' 
            current = current.next
        return '<' + string + '>'

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

        
element1 = Element("a")
element2 = Element("b")
element3 = Element(4)
element4 = Element(47)

linkedList = LinkedList(element1)

linkedList.append(element2)
linkedList.append(element3)
linkedList.append(element4)

print(linkedList)
