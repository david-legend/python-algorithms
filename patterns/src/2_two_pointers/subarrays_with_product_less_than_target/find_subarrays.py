def find_subarrays(arr, target):
    result = []
    product, window_start = 1, 0
    
    for window_end in range(len(arr)):
        product *= arr[window_end]
        
        if arr[window_end] < target:
            result.append([arr[window_end]])
          
        if window_end - window_start + 1 > 1:
            if product < target:
                result.append(arr[window_start : window_end + 1])
            else:
                while product >= target:
                    product = product / arr[window_start]
                    window_start += 1
                if window_end - window_start + 1 > 1:
                    result.append(arr[window_start : window_end + 1])
                
    return result


print(find_subarrays([2, 5, 3, 10], target=30))
print(find_subarrays([8, 2, 6, 5], target=50 ))