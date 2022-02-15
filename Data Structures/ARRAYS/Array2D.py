'''
Author: Muhammad Usama

Implimentation of 2-D Array in Python.
'''

# Array 2-D is made up of Array class.
from Array import Array
class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)
    
    
    # returns the number of rows.
    def numOfRows(self):
        return (len(self._theRows))
    
    
    # returns the number of columns.
    def numOfCols(self):
        return (len(self._theRows[0]))
    
    
    # set all the values of a 2-D array to the specified value in the clear method.
    def clear(self, value):
        for row in self._theRows:
            row.clear(value)
    
    
    # get item from a 2-D array using print(obj[r][c])
    def __getitem__(self, ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numOfRows() \
            and col >= 0 and col < self.numOfCols(), \
                "Array subscript out of range."
        return (self._theRows[row][col])
    
    
    # set a value to the 2-D array using obj[r][c] = value
    def __setitem__(self, ndxTuple, value):
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numOfRows() \
            and col >= 0 and col < self.numOfCols(), \
                "Array subscript out of range."
        self._theRows[row][col] = value



# Driver Code/Main Section.
'''
array2D = Array2D(3, 3)
print(array2D.numOfRows()) # returns the num of rows.
print(array2D.numOfCols()) # returns the num of cols.
array2D[0,0] = 1 # set the items.
array2D[0,1] = 2
array2D[0,2] = 3
array2D[1,0] = 4
array2D[1,1] = 5
array2D[1,2] = 6
array2D[2,0] = 7
array2D[2,1] = 8
array2D[2,2] = 9
print()
print("The 2-D Array is:")
print(array2D[0,0], array2D[0,1], array2D[0,2])
print(array2D[1,0], array2D[1,1], array2D[1,2])
print(array2D[2,0], array2D[2,1], array2D[2,2])
print()
array2D.clear(0)
print("The 2-D Array after clear the value to 0 is:")
print(array2D[0,0], array2D[0,1], array2D[0,2])
print(array2D[1,0], array2D[1,1], array2D[1,2])
print(array2D[2,0], array2D[2,1], array2D[2,2])
'''