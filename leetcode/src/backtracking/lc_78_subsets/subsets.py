def subsets(nums):
    subsets = []
    subsets.append([])

    for num in nums:
        for i in range(len(subsets)):
            data = list(subsets[i])
            data.append(num)
            subsets.append(data)

    return subsets

def subsets_recursive(nums):
    result = []
    gen_subsets(0, nums, [], result)

    return result

def gen_subsets(idx, nums, data, result):
    if idx >= len(nums):
        result.append(list(data))
        return
    
    data.append(nums[idx])
    gen_subsets(idx + 1, nums, data, result)

    data.pop()
    gen_subsets(idx + 1, nums, data, result)


print("Iterative Solution \n")
print(subsets([1, 2, 3]))
print(subsets([1, 2, 3, 4]))

print("\nRecursive Solution")
print(subsets_recursive([1, 2, 3]))
print(subsets_recursive([1, 2, 3, 4]))