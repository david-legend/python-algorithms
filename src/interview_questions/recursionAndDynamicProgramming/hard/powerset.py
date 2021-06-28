# Power Set: Write a method to return all subsets of a set.

# For Eg. When given a set where n = 0, there is just one subset of an empty set: {} --> result will be [[]]
# For n = 1, There are 2 subsets of the set {1}:         {}, {1} --> result will be [[], [1]]
# For n = 2, There are 4 subsets of the set {1 , 2}:     {} ,{1}, {2}, {1 , 2}. --> result will be [[], [1], [2], [1,2]]
# For n = 3, There are 8 subsets of the set {1 , 2, 3}:  {}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3} 
#  --> result will be [[}, [1}, [2}, [3], [1, 2], [1, 3], [2, 3], [1, 2, 3] ]

set1 = []
set2 = [1]
set3 = [1,2]
set4 = [1,2,3]

#This solution will be O(n2n) in time and space
def getSubSets(setData, index):
    allSubSets = None
    if(len(setData) == index):
        allSubSets = [[]]
    else:
        allSubSets = getSubSets(setData, index+1)
        subsetItem = setData[index]
        moreSubsSets = []

        for subset in allSubSets: 
            newSubSet =  []
            newSubSet.extend(subset)
            newSubSet.append(subsetItem)
            moreSubsSets.append(newSubSet) 

        allSubSets.extend(moreSubsSets)
    
    return allSubSets

print("Running GetSubSets using Recursion: ")
print(getSubSets(set1, 0))
print(getSubSets(set2, 0))
print(getSubSets(set3, 0))
print(getSubSets(set4, 0))


#Solution #2: Combinatorics  (This solution is freaking confusing. WTF!!)
def getSubSets2(setData):
    allSubSets = []
    max = 1 << len(setData)
    for i in range(max):
        subset = convertToSet(i, setData)
        allSubSets.append(subset)

    return allSubSets;

def convertToSet(x, setData):
    subset = []
    index = 0

    i = x
    while i > 0:
        if((i & 1) == 1):
            subset.append(setData[index])
        i >>= 1
        index += 1

    return subset


print("\n\nRunning GetSubSets2 using Combinatorics: \n")
print(getSubSets2(set1))
print(getSubSets2(set2))
print(getSubSets2(set3))
print(getSubSets2(set4))