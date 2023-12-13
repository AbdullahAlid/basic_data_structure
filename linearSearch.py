
def linearSearch(array, value):

    for i in range(len(arr)):
        if arr[i] == val:
            return i
    return -1


arr = [5, 9, 4, 1, 8, 10]
val = 4
result = linearSearch(arr, val)
if result == -1:
    print(f"{val} is not included in given array")
else:
    print(f"{val} is included in given array at index {result}")
