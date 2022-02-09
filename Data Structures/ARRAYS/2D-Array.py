'''
Author: Muhammad Usama

Implimentation of 2-D Array in Python.
'''

from Array import Array
class Array2D:
    def __init__(self, numRows, numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)
    
    def numOfRows(self):
        return (len(self._theRows))
    
    def numOfCols(self):
        return (len(self._theRows[0]))
    
    def clear(self, value):
        for row in self._theRows:
            row.clear(value)
            
array2D = Array2D(3, 3)