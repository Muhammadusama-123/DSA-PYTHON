"""
Author: Muhammad Usama
"""

"""
Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

.) This algorithm performs better as compared to bubble sorting technique but still bubble sort
algorithm is favourable in most computer science applications like Computer Graphics.
"""


def InsertionSort(sizeOfList, emptyList):
    # ith loop starts from 1 because first item which is on 0th index is already sorted.
    for i in range(1, sizeOfList):
        temp = emptyList[i]
        j = i - 1
        while (j >= 0 and temp < emptyList[j]):
            emptyList[j + 1] = emptyList[j]
            j -= 1
        emptyList[j + 1] = temp
        
    print("List after applying Insertion Sort Algorithm is : ", emptyList)


# Driver Code/Main Section
sizeOfList = int(input("Enter size of the list: "))
emptyList = []
for i in range(sizeOfList):
    value = int(input("Enter value to store in a list: "))
    emptyList.append(value)
print(emptyList)
InsertionSort(sizeOfList, emptyList)