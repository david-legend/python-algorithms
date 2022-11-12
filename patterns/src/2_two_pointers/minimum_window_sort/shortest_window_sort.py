def findUnsortedSubarray(nums):
    left = find_min_index(nums)
    right = find_max_index(nums)
    result = right - left
    return result + 1 if result > 0 else 0
    
def find_min_index( nums):
    idx, stack = float('inf'), []
    for i in range(len(nums)):
        curr_val = nums[i]
        while stack and stack[-1][1] > curr_val:
            prev_val_idx,  _ = stack.pop()
            idx = min(idx, prev_val_idx)
        stack.append((i, curr_val))
    return 0 if idx == float('inf') else idx

def find_max_index( nums):
    idx, stack = 0, []
    for i in range(len(nums)-1, -1, -1):
        curr_val = nums[i]
        while stack and stack[-1][1] < curr_val:
            prev_val_idx, _ = stack.pop()
            idx = max(idx, prev_val_idx)
        stack.append((i, curr_val))
    return idx


print(findUnsortedSubarray([2,6,4,8,10,9,15]))  #5
print(findUnsortedSubarray([1,2,3,4]))  #0
print(findUnsortedSubarray([1, 3, 2, 0, -1, 7, 10]))    #5
print(findUnsortedSubarray([1,3,2,2,2]))    #4
print(findUnsortedSubarray([3, 2, 1]))  #3