import math


class ArrayReader:

    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
            return math.inf
        return self.arr[index]


# Time complexity
# There are two parts of the algorithm. 
# In the first part, we keep increasing the bound’s size exponentially (double it every time) 
# while searching for the proper bounds. 
# Therefore, this step will take O(logN) assuming that the array will have maximum ‘N’ numbers. 
# In the second step, we perform the binary search which will take O(logN), 
# so the overall time complexity of our algorithm will be O(logN + logN), 
# which is asymptotically equivalent to O(logN).

# Space complexity
# The algorithm runs in constant space O(1).
def search_in_infinite_array(reader, key):
    # find the proper bounds first
    start, end = 0, 1
    while reader.get(end) < key:
        newStart = end + 1
        end += (end - start + 1) * 2
        # increase to double the bounds size
        start = newStart

    return binary_search(reader, key, start, end)


def binary_search(reader, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if key < reader.get(mid):
            end = mid - 1
        elif key > reader.get(mid):
            start = mid + 1
        else:  # found the key
            return mid

    return -1


reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
print(search_in_infinite_array(reader, 30))
print(search_in_infinite_array(reader, 11))
reader = ArrayReader([1, 3, 8, 10, 15])
print(search_in_infinite_array(reader, 15))
print(search_in_infinite_array(reader, 200))
