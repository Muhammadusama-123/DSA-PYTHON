'''
Author: Muhammad Usama
'''

'''
In Computer Science, Linear search is a very simple search algorithm. In this type of search, 
a sequential search is made over all items one by one. Every item is checked and if a match is 
found then that particular item and its position is returned, otherwise the search continues till
the last item of the list.
'''


# This algorithm is written with the help of a function and a for loop.

def LinearSearch(emptyList, sizeOfList, searchValue):
    flag = 0
    for i in range(sizeOfList):
        if emptyList[i] == searchValue:
            flag = 1
            position = i
            key = emptyList[i]
            break
    if flag == 1:
        print(f'Value found at {position + 1} position and the index of a value in a list is {position} '
              f'and the value which is searched in a list is {key}.')


# Driver code:
sizeOfList = int(input('Enter size of the list: '))
emptyList = [] # initialies an empty list.
for i in range(sizeOfList):
    value = int(input('Enter values to store in a list: '))
    emptyList.append(value)
print(emptyList)
searchValue = int(input('Enter value you want to search in a list: '))
LinearSearch(emptyList, sizeOfList, searchValue)