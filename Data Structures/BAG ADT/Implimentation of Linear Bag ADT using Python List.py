'''
Author: Muhammad Usama
'''

# creating a bag iterator to perform iterative functionality on the instance of a bag class.
class _BagIterator:
    def __init__(self, theList):
        self._bagItems = theList
        self.curItem = 0
    
    
#     The iter method simply returns a reference to the objectitself and is always implemented to
# do so.
    def __iter__(self):
        return self
    
    
    # This method is called to return the next item of the bag which is a container.
    def __next__(self):
        if(self.curItem < len(self._bagItems)):
            item = self._bagItems[self.curItem]
            self.curItem += 1
            return item
        else:
            raise StopIteration



class Bag:
    # Initializes Bag using Python List.
    def __init__(self):
        self._theListOfItems = list() 
        # list(): this is a constructor which initializes an empty list.
        
    
    # This is the way you change the built-in Length Function in python and it simply returns the
    # length of bag which is made up of python list. 
    def __len__(self):
        return len(self._theListOfItems)
    
    
    # This is the way you change the built-in Contains Feature/Function in python and it simply
    # checks if an item is in the bag or not and returns the answer in Bool value. 
    def __contains__(self, item):
        return item in self._theListOfItems
    
    
    # This method is used to add item in the bag.
    def add(self, item):
        self._theListOfItems.append(item)
    
        
    # This method is used to remove an item from a particular index.
    def remove(self, item):
        assert item in self._theListOfItems, "The item you want to remove must be in the bag."
        Index = self._theListOfItems.index(item)
        return self._theListOfItems.pop(Index)
    
    
    # This item gets an item from a bag with the help of index.
    def getItemfromBag(self, indx):
        return self._theListOfItems[indx]
    
    
    # This method is used to print the bag and show it in a console screen.
    def printBag(self):
        print(self._theListOfItems)
        
    # This method is add to iterate all the items of the bag using for loop.
    def __iter__(self):
        return _BagIterator(self._theListOfItems)
    

# Driver Code/ Main Section
BAG = Bag() # initializes the bag.
print(len(BAG)) # returns the length of a bag.
BAG.add(1) # add item to the bag
BAG.add(2)
BAG.add(3)
BAG.add(4)
BAG.add(5)
print(len(BAG)) # returns the latest length of a bag.
print(BAG.__len__()) # returns the latest length of a bag.
BAG.printBag() # print the bag and show in a console screen.
BAG.remove(2) # remove an item from bag.
BAG.printBag() # print the bag and show in a console screen.
print(BAG.getItemfromBag(2)) # get item from bag with the help of index.
print(BAG.__contains__(3)) # returns true or false according to the result.
print(2 in BAG) # returns true or false according to condition.
for item in BAG: # iterator all the items of the bag.
    print(item)

    
        
    