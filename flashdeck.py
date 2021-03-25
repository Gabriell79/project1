import unittest

"""
Assigment #2: Flashdeck
"""

class Flashcard:
    """Node class:Flashcard"""
    def __init__(self,data0):
        self.data = data0 
        self.next = None

    def getData(self):
        """Returns Data"""
        return self.data

    def getNext(self):
        """Returns Next"""
        return self.next

    def setData(self, data1):
        """Set Data"""
        self.data = data1

    def setNext(self,next1):
        """Set Next"""
        self.next = next1

class Flashdeck:
    """Unordered List:Flashdeck"""
    """constructor"""    
    def __init__(self):
        self.head = None

    """if the list is empty, it will return True, false if it isn't"""
    def isEmpty(self):
        return self.head == None 

    """Add an item to the beginning of the list"""
    def add(self,item):
        T =Flashcard(item)
        T.setNext(self.head)
        self.head = T

    """Get the size of the list in Integer"""
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    
    """Remove and return the last value, it can change if the posi gets a value"""
    def pop(self, posi=None):

        if posi == None:
            posi = self.size() - 1

        if posi < self.size() and posi >= 0:
            current = self.head
            previous = None
            index = 0

            while index < posi:
                previous = current
                current = current.getNext()
                index += 1

            if previous == None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())
            return current.getData()

        else:
            print("not a valid position in the current list to pop from ")
            return None
    """Get the position of an item in a list"""
    def index(self, data):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
                index += 1
        if found:
            return index
        else:
            return -1



def main(): 
    """Assigning the empty list to a variable"""
    deck = Flashdeck()
    """Adding all the items to the list"""
    deck.add("It is very useful for designing algorithms to evaluate and translate expressions.")
    deck.add('S')
    deck.add("Which one can assist you in the construction of timing simulations?")
    deck.add('Q')
    deck.add("They are a collection of items where each item holds a relative position.")
    deck.add('L')
    
    """Showing all the flashcards, one by one, until you get them right."""
    while not deck.isEmpty():
        
        hint = deck.pop()
        ans1 = deck.pop()
        print(hint)
        ans=input("Enter 'S' for Stack, 'Q' for Queue, or 'L' for List:")
        ans=ans.upper()
        if ans == ans1:
           print("Good job!")
            
        else:    
            print("Wrong answer, try again.")
            deck.add(hint)
            deck.add(ans1)
        
    else:
        print("Well done, you finish all your flashcard succsesfully")

    

if __name__ == "__main__":
    main()