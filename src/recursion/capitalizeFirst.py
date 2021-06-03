# CapitalizFirst --> Given an array of words write a recursive function to capitalize the first letter of every word in the array

def capitalizeFirst(arr):
    resultArr = []
    if(len(arr) > 0):
        resultArr.append(arr[0].capitalize())
        resultArr.extend(capitalizeFirst(arr[1:]))
    
    return resultArr


dtSet1 = ["car", "taco", "banana"]
dtSet2 = ["mean", "average", "boom", "baba"]
dtSet3 = ["daisy", "john", "frank"]

print(capitalizeFirst(dtSet1))
print(capitalizeFirst(dtSet2))
print(capitalizeFirst(dtSet3))

