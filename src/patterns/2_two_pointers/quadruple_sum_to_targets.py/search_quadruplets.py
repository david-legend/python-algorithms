from tkinter import N


# Time complexity O(N^3)
# Sorting the array will take O(N*logN). 
# Overall searchQuadruplets() will take O(N * logN + N^3), 
# which is asymptotically equivalent to O(N^3).

# Space complexity O(N)
# The space complexity of the algorithm is O(N),
# since O(N) space is required for sorting.
def search_quadruplets(arr, target):
    quadruplets = []
    arr.sort()
    
    for i in range(0, len(arr) - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr) -2):
            if j > i+1 and arr[j] == arr[j-1]:
                continue
            search_pair(arr, target, i, j, quadruplets)
    return quadruplets


def search_pair(arr, target, first, second, quadruplets):
    left = second + 1
    right = len(arr) -1
    
    while left < right:
        quad_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if quad_sum == target:
            quadruplets.append([first, second, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif quad_sum > target:
            right -= 1
        else: 
            left += 1
                
print(search_quadruplets([4, 1, 2, -1, 1, -3], target=1))
print(search_quadruplets([2, 0, -1, 1, -2, 2], target=2))
            