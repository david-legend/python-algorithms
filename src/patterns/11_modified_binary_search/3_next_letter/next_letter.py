# Time complexity
# Since, we are reducing the search range by half at every step, 
# this means that the time complexity of our algorithm will be O(logN) 
# where ‘N’ is the total elements in the given array.

# Space complexity
# The algorithm runs in constant space O(1).
def search_next_letter(letters, key):
    n = len(letters)
    start, end = 0, n - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if key < letters[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    while letters[start % n] == key:
            start += 1

    return letters[start % n]


def next_letter(letters, target):
    for letter in letters:
        if letter > target:
            return letter
    
    return letters[0]
     

print("Solution 1")
print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'c'))
print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))
print(search_next_letter(["e","e","e","k","q","q","q","v","v","y"], "q",))


print("\n\nSolution 2")
print(next_letter(['a', 'c', 'f', 'h'], 'f'))
print(next_letter(['a', 'c', 'f', 'h'], 'b'))
print(next_letter(['a', 'c', 'f', 'h'], 'c'))
print(next_letter(['a', 'c', 'f', 'h'], 'm'))
print(next_letter(["e","e","e","k","q","q","q","v","v","y"], "q",))