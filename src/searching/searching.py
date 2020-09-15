def linear_search(arr, target):
    # Your code here
    isTarget = -1
    index = 0
    for i in arr:
        if i == target:
            isTarget = index
        index += 1
    return isTarget   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high: 
        mid = (high + low) // 2
  
        if arr[mid] < target: 
            low = mid + 1
        elif arr[mid] > target: 
            high = mid - 1
        else: 
            return mid 
    return -1
