
# Time :O(nlog n + 2^n  * n)
# Space: O(2^n * k)
# Auxilliary Space of Recursion: O(n)

def subsets(nums):
    result = []
    nums.sort()
    subset_helper(nums, result, [], 0)
    return result

def subset_helper(nums, result, path, idx):
   
    result.append(list(path))

    for i in range(idx, len(nums)):
        if i > idx and nums[i] == nums[i-1]: continue
        path.append(nums[i])
        subset_helper(nums, result, path, i+1)

        path.pop()


print(subsets([1]))
print(subsets([1, 1]))
print(subsets([1,1,2]))
print(subsets([1, 2, 3]))
print(subsets([1, 2, 3, 4]))
