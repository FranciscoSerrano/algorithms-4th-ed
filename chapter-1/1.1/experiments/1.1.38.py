'''
Time linear search vs binar search
'''
import random
import timeit
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

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
        else:
            continue
    return False

print(linear_search(array, 76))
