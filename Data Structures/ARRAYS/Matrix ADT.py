from Array2D import Array2D

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows, numCols)
        self._theGrid.clear(0)
        
    def numRows(self):
        return (self._theGrid.numOfRows)
    
    def numCols(self):
        return (self._theGrid.numOfCols)
    
    def __getitem__(self, ndxTuple):
        return (self._theGrid[ndxTuple[0], ndxTuple[1]])
    
    def __setitem__(self, ndxTuple, scaler):
        self._theGrid[ndxTuple[0], ndxTuple[1]] = scaler
        
    def scaleBy(self, scaler):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r, c] *= scaler
                
'''
To be added.
'''
                
        
        
matrix = Matrix(3, 3)
matrix[0,0] = 1
matrix[0,1] = 2
matrix[0,2] = 3
matrix[1,0] = 4
matrix[1,1] = 5
matrix[1,2] = 6
matrix[2,0] = 7
matrix[2,1] = 8
matrix[2,2] = 9
print("Matrix is:")
print(matrix[0,0], matrix[0,1], matrix[0,2])
print(matrix[1,0], matrix[1,1], matrix[1,2])
print(matrix[2,0], matrix[2,1], matrix[2,2])
print()
print("Matrix after scale by is:")
matrix.scaleBy(2)
print(matrix[0,0], matrix[0,1], matrix[0,2])
print(matrix[1,0], matrix[1,1], matrix[1,2])
print(matrix[2,0], matrix[2,1], matrix[2,2])



