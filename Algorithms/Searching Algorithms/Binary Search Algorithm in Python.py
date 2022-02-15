'''
Author: Muhammad Usama
'''

'''
In Computer Science, Binary Search, also known as half-interval search, logarithmic search, or binary chop,
is a search algorithm that finds the position of a target value within a sorted array.Binary search 
compares the target value to the middle element of the array.
'''

# Implimentation of Binary Search Algorithm on sorted Ascending order list.


def BinarySearch(emptyList, searchValue):
    i = 0
    j = (len(emptyList)) - 1
    flag = 0
    while (i <= j and flag == 0):
        mid = (i + j) // 2
        if emptyList[mid] == searchValue:
            flag = 1
            position = mid
            key = emptyList[mid]
            print('Value found.')
        elif emptyList[mid] > searchValue:
            j = mid - 1
        elif emptyList[mid] < searchValue:
            i = mid + 1
    if flag == 1:
        print(f'Value found at {position + 1} position and the index of the value in a list is '
f'{position} and the value which is searched in a list is {key}.'
)


# Driver Code:
sizeOfList = int(input('Enter size of the list: '))
emptyList = [] # list must be sorted and in ascending order.
for i in range(sizeOfList):
    value = int(input('Enter values you want to add in a list in ascending order: '))
    emptyList.append(value)
print(emptyList)
searchValue = int(input('Enter value which you want to search in a list: '))
BinarySearch(emptyList, searchValue)