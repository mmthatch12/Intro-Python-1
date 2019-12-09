arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def linear(array, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i 
    return -1


print(linear(arr, 2))

def binary(array, target):
    low = 0
    high = len(array)-1
    while low <= high:
        middle = (low+high)/2
        if target < array[middle]:
            high = middle-1
        elif target > array[middle]:
            low = middle+1
        else:
            return middle
    return -1

print(linear(arr, 2))
    
    
    
    # for x in array:
    #     if middle == target:
    #         return array.index(middle)
    #     else:
    #         if middle < target:
    #             if y in array[middle: ]:
    #                 middle = len(array[middle: ])/2

