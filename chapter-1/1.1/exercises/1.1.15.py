'''
Write a static method histogram() that takes an array a[] of int values and an integer
m as arguments and returns an array of length m whose ith entry is the number of times 
that integer i appeared in the argument array. If the values in are all between 0 and m-1,
the sum of the values in the returned array should be equal to a.length.
'''


def histogram(arr, intt):
    hist = []
    for i in range(intt):
        # At the beginning we haven't encountered any instances of i yet.
        # The correct initial count value is 0.
        count = 0
        for j in range(len(arr)):
            if i == arr[j]:
                # We found an i. Add it to our running count.
                count += 1
        # We found all the i's we're going to find. Record that fact.
        hist.append(count)
    return hist

array = [1, 2, 4, 5, 6, 7, 2, 3, 4, 7, 7, 7 , 8, 2, 1]

print(histogram(array, 8))