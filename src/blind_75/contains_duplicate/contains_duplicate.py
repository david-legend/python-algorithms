def contains_duplicate(nums):
    num_freq = {}
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1
        
        if num_freq[num] > 1:
            return True
    
    return False


def contains_duplicate_2(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        
        hashset.add(num)
    
    return False


print(contains_duplicate([1,2,3,1]))
print(contains_duplicate([1,2,3,4]))
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))

print("\n")

print(contains_duplicate_2([1,2,3,1]))
print(contains_duplicate_2([1,2,3,4]))
print(contains_duplicate_2([1,1,1,3,3,4,3,2,4,2]))
