from heapq import *
# def kth_greatest(arr, k):
#     min_heap = []

#     for i in range(k):
#         heappush(min_heap, arr[i])
    
#     for i in range(k, len(arr)):
#         heappushpop(min_heap, arr[i])
    
#     return min_heap[0]


# def get_greatest_elements(arr, k):
#     result, data = [], []
    
#     for i in range(len(arr)):
#         data.append(arr[i])
#         if len(data) >= k:
#             result.append(kth_greatest(data, k))
    
#     return result



# from heapq import *
def add(min_heap, num, k):
    min_heap = []
    heappush(min_heap, num)
    
    if len(min_heap) > k:
        heappop(min_heap)

    return min_heap[0]

def get_greatest_elements(arr, k):
    min_heap, result = [], []
    for i in range(k):
        ans = add(min_heap, arr[i], k)
        if len(min_heap) == k:
            result.append(min_heap[0])

    
    for i in range(k, len(arr)):
        ans = add(min_heap, arr[i], k)
        result.append(ans)
    
    return result

print(get_greatest_elements([2,4,5,1,4], 3)) # result --> [4, 4, 4, 4]
# print(get_greatest_elements([4,2,1,3], 1)) # result --> [4, 4, 4, 4]
# print(get_greatest_elements([4,2,1,3], 2)) # result --> [2, 2, 3]
# print(get_greatest_elements([4,2,1,3], 3)) # result --> [1, 2]
# print(get_greatest_elements([4,2,1,3], 4)) # result --> [1]


def hash(s):
    k = 0
    for i, st in enumerate(s):
        k += (i+1) * (ord(st) - ord('a') + 1)
    return k


print(hash("xwxx"))
print(hash("vztz"))
print(hash("uwvy"))
print(hash("gvzz"))
print(hash("tttt"))
print(hash("gvzz"))