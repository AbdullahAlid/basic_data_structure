# binary search in itaretive way
def binarySearch(array, value, first, last):
    while last >= first:
        mid = (first+last)//2
        if array[mid] == value:
            return mid
        elif value > arr[mid]:
            first = mid+1
        else:
            last = mid-1
    # else:
    return -1


arr = [1, 4, 5, 8, 9, 10]
val = 8
last = len(arr)-1
result = binarySearch(arr, val, 0, last)
if result == -1:
    print(f"{val} is not included in given array")
else:
    print(f"{val} is included in given array at index {result}")
