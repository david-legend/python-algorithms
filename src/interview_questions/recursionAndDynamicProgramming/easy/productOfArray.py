# ProductOfArray --> Write a recursive function that takes an array of numbers and returns a product of all the elements

def productOfArray(arr):
    if(len(arr) == 1):
        return arr[0]
    else: 
        return arr[0] * productOfArray(arr[1: len(arr)])


sample1 = [1,2,3]
sample2 = [1,2,3,4]
sample3 = [1,2,3,10]

print(productOfArray(sample1)) #ans --> 6
print(productOfArray(sample2)) #ans --> 24
print(productOfArray(sample3)) #ans --> 60