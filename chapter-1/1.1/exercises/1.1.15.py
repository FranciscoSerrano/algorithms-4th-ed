'''
Write a static method histogram() that takes an array a[] of int values and an integer
m as arguments and returns an array of length m whose ith entry is the number of times 
that integer i appeared in the argument array. If the values in are all between 0 and m-1,
the sum of the values in the returned array should be equal to a.length.
'''
'''
Time Complexity
Size of the problem: size of the inputs
Pay attention to all inputs. In this case array and int.

Opportunities:
count +=1 happens len(arr) times * int times

So my histogram is O(len(arr)*int)

So Josh's histogram is O(m + len(data))
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

# Create a histogram of integer values from 0 to m
def histogram_josh(data, m):
    # Create bins to keep track of how frequently
    # we encounter a value.
    # NOTE: At the beginning we haven't looked at any of
    # the data, so all the counts are zero.
    # Since we're keeping track of values from 0 to m, we need m + 1 bins.
    bins = [0] * (m + 1)
    for element in data:
        # Check to see if the current element is part of
        # the distribution we are counting
        if element > m:
            continue
        # Note that we saw another value of element
        bins[element] += 1
    # We counted everything. Return the bins
    return bins


array = [1, 2, 4, 5, 6, 7, 2, 3, 4, 7, 7, 7 , 8, 2, 1]

print(histogram(array, 8))
print(histogram_josh(array, 8))