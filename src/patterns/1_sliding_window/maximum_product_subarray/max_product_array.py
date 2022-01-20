import math
def maximum_product_subarray(arr):
    max_product = -math.inf
    product, window_start = 1, 0
    
    for window_end in range(len(arr)):
        product *= arr[window_end]
        
        while product < max_product and window_start < window_end:
            if arr[window_start] == 0:
                window_start += 1
            else:
                product = product / arr[window_start]
                window_start += 1
        
        max_product = max(max_product, product)
        
        if product == 0:
           window_start = max(window_start, window_end)
           product = arr[window_start]
           
    return max_product


print(maximum_product_subarray([1,2,-1,4,6]))
print(maximum_product_subarray([-1,-2,-1,-4,6]))
print(maximum_product_subarray([-1,6,2,0,7,9]))
print(maximum_product_subarray([-4, -3, -5]))
print(maximum_product_subarray([-2,0,3,5])) 