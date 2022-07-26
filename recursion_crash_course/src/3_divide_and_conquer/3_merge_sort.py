def merge_sort(nums, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(nums, start, mid)
        merge_sort(nums, mid + 1, end)
        merge(nums, start, mid, end)


def merge(nums, start, mid, end):
    temp = [None] * (end - start + 1)
    i, j, k = start, mid + 1, 0

    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1
        k += 1
    
    while i <= mid:
        temp[k] = nums[i]
        k += 1
        i += 1

    while j <= end:
        temp[k] = nums[j]
        k += 1
        j += 1
    
    i, j = 0, start
    while i < len(temp):
        nums[j] = temp[i]
        i += 1
        j += 1


data = [8, 5, 2, 9, 5, 6, 3]
merge_sort(data, 0, len(data) - 1)

print(data)