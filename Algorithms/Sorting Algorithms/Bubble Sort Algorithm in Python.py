"""
Author: Muhammad Usama
"""

"""
Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent
elements if they are in wrong order.
"""


def BubbleSort(sizeOfList, emptyList):
    for i in range(sizeOfList):
        for j in range(sizeOfList - i - 1):
            """
            Here we set j to (sizeOfList - i - 1) because in the second last element of the list
            lets say here the list is : [6, 8, 4, 2, 1]
            so we compare 2 with 1 means we compare the second last element with the last element
            because there is no way to compare 1 with other element because 1 is the last element
            so that's why the condition is (sizeOfList - i - 1)
            """
            if(emptyList[j] > emptyList[j + 1]):
                temp = emptyList[j]
                emptyList[j] = emptyList[j + 1]
                emptyList[j + 1] = temp
    
    print("List after applying Bubble Sort Algorithm is : ", emptyList)


# Driver Code/Main Section
sizeOfList = int(input("Enter size of the list: "))
emptyList = []
for i in range(sizeOfList):
    value = int(input("Enter value to store in a list: "))
    emptyList.append(value)
print(emptyList)
BubbleSort(sizeOfList, emptyList)