#Time complexity for this algorithm is O(N)
#Space complexity is O(1)
def remove_duplicates(nums):
    l, r, n = 0, 1, len(nums)
    while r < n:
        if nums[l] == nums[r]:
            r += 1
        else:
            nums[l+1] = nums[r]
            l += 1
            r += 1
    return l + 1

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9])) #Output 4 : because first four elements after removing the duplicates will be [2, 3, 6, 9]
print(remove_duplicates([2, 2, 2, 11])) # Output 2 : because first two elements after removing the duplicates will be [2, 11]