# Triplets with Smaller Sum (medium) ✩

Given an array arr of unsorted numbers and a target sum, 
count all triplets in it such that arr[i] + arr[j] + arr[k] < target 
where i, j, and k are three different indices. 
Write a function to return the count of such triplets.

### Example 1
Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


### Example 2
Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]



## Part B

After the solving the question above, you can try a variant of it 
that requires that you return the triplets instead of the count

Write a function to return the list of all such triplets instead of the count

### Example 1
Input: [-1, 0, 2, 3], target=3 
Output: [[-1, 0, 3], [-1, 0, 2]]
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]


### Example 2
Input: [-1, 4, 2, 1, 3], target=5 
Output: [[-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]]
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]