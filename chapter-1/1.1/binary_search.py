'''
Binary serach requires a SORTED array.
It works by cutting the array in half,
checking whether the target is to the left or right of the middle, 
then split in half again.
Repeat until target is found or does not exit.
You can tell if it doesnt exists if the left index is higher than the right index.
'''
import random
random.seed(42)
# create a sorted array.
array = []
for i in range(100):
    array.append(random.randint(1, 200))
array.sort()

# iterative binary search
def binary_search(arr, target):
    lo = 0
    hi = len(arr) - 1
    for i in range(len(arr)):
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

print(binary_search(array, 76))
print(array[binary_search(array, 76)])

# recursive binary search 
def recursive_binary_search(arr, target, lo, hi):
    if lo > hi:
        return False
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, hi)
    else:
        return recursive_binary_search(arr, target, lo, mid - 1)

print(recursive_binary_search(array, 76, 0, len(array)-1))
print(array[recursive_binary_search(array, 76, 0, len(array)-1)])