# Flatten --> write a recursion function called flatten 
# which accepts an array of arrays and returns a new array with all the values flattened

def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else: 
            resultArr.append(custItem)
    return resultArr 



dtSet0 = [1,2,3,4,5]
dtSet1 = [1,2,3,[4,5]]
dtSet2 = [1,[2,[3, 4], [[5]]]]
dtSet3 = [[[1,[[[2]]], [[[[[[[3]]]]]]]]]]

print(flatten(dtSet1))
print(flatten(dtSet2))
print(flatten(dtSet3))
