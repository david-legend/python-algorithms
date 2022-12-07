def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums) - 1)
    return nums

def quick_sort_helper(nums, start_idx, end_idx):
    if start_idx > end_idx:
        return
    
    pivot_idx, left_idx, right_idx = start_idx, start_idx + 1, end_idx
    
    while left_idx <= right_idx:
        if nums[left_idx] > nums[pivot_idx] and nums[right_idx] < nums[pivot_idx]:
            swap(left_idx, right_idx, nums)
        
        if nums[left_idx] <= nums[pivot_idx]:
            left_idx += 1
        
        if nums[right_idx] >= nums[pivot_idx]:
            right_idx -= 1
    
    swap(pivot_idx, right_idx, nums)
    quick_sort_helper(nums, start_idx, right_idx - 1)
    quick_sort_helper(nums, right_idx + 1, end_idx)


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

print(quick_sort([8, 5, 2, 9, 0, 5, 6, 3]))
print(quick_sort([9,7,6,10,12,11, 1]))