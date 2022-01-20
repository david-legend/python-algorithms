import math
def maximum_product_subarray(arr):
    max_product = -math.inf
    product, window_start = 1, 0
    
    for window_end in range(len(arr)):
        product *= arr[window_end]
        if product < max_product:
            window_start = max(window_start, window_end)
            product = arr[window_start]
        
        max_product = max(max_product, product)
        
    return max_product


print(maximum_product_subarray([1,2,-1,4,6]))
print(maximum_product_subarray([-1,-2,-1,-4,6]))
print(maximum_product_subarray([-1,6,2,0,7,9]))