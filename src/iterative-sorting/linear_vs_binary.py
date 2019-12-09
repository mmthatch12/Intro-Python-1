arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def linear(array, target):
    for x in array:
        if x == target:
            return array.index(x)


print(linear(arr, 1.5))