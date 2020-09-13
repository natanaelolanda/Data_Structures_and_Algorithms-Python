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
    
    def get_position(self, position):
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None
    
    def get_length(self):
        counter = 0
        current = self.head
        while current:
            counter += 1
            current = current.next
        return counter

    def insert(self, new_element, position):
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element

    def delete(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        
  
        
element1 = Element("a")
element2 = Element("b")
element3 = Element(4)
element4 = Element(47)
element5 = Element("oi")

ll = LinkedList(element1)

ll.append(element2)
ll.append(element3)
ll.append(element4)
ll.append(element5)

print(ll)
#print(ll.get_position(4).value)
print(ll.get_length())
ll.insert(Element('fr'), 3)
print(ll)
ll.delete(4)
print(ll)
