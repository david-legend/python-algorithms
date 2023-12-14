
# Time: O(n)
# Space: O(n)
def containsDuplicate(nums) -> bool:
        hash_set = set()
        for val in nums:
            if val in hash_set:
                return True
            hash_set.add(val)
        
        return False


# Time: O(n)
# Space: O(n)
def containsDuplicate2(nums) -> bool:
        num_freq = {}
        for val in nums:
            if val in num_freq:
                return True
            num_freq[val] = 1
        
        return False