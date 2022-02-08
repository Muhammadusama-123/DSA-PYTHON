'''
Author: Muhammad Usama
'''

import ctypes # This liabrary is used to add C-Language functionality in your file.

# This class is used to traverse all the items of the array.
class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curIndex = 0 # sets cur index to 0 because for loop starts from 0.
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if(self._curIndex < len(self._arrayRef)):
            item = self._arrayRef[self._curIndex]
            self._curIndex += 1
            return item
        else:
            raise StopIteration
        
        

class Array:
    def __init__(self, size):
        assert size > 0, "The size of the array must be greater than 0"
        self._size = size
        PythonArray = ctypes.py_object * size
        # array is stored in the _elements property.
        self._elements = PythonArray()
        self.clear(None)
        
    # This method returns the length of an array.
    def __len__(self):
        return self._size
    
    # This method is used to get an item from the specified index.
    def __getitem__(self, index):
        assert index >= 0, "Array index is out of range."
        return (self._elements[index])
    
    # This method is used to set an item to the specified index.
    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Array subscript out of range."
        self._elements[index] = value
        
    # This method is used to clear an array from the specified value.
    def clear(self, value):
        for i in range(len(self)):
            self._elements[i] = value
    
    # This method is used for traversing an array.
    def __iter__(self):
        return _ArrayIterator(self._elements)
    
    
    
# Driver Code/Main Section.
array1D = Array(5) # initialize the array of length is equal to 5.
array1D[0] = 2 # sets item to the array.
array1D[1] = 4
array1D[2] = 6
array1D[3] = 8
array1D[4] = 10
print(array1D[3]) # get item from 3rd index.
print(len(array1D)) # returns the length of the array1D object.
array1D.clear(0) # This method sets all the values of an array to the value you passed into
# this method which is in this case is 0.
print("The elements after iteration are:")
for item in array1D: # This script is used for traversing an array.
    print(item)
        
    
    