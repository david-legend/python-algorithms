# Find the Duplicate Number (easy) ✩

## solve the above problem in O(1)O space and without modifying the input array
We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
The array has only one duplicate but it can be repeated multiple times. 
Find that duplicate number without using any extra space. 
You are, however, allowed to modify the input array.

#### Example 1
Input: [1, 4, 4, 3, 2]
Output: 4

#### Example 2
Input: [2, 1, 3, 3, 5, 4]
Output: 3

#### Example 3
Input: [2, 4, 1, 4, 4]
Output: 4


## Solution 

While doing the cyclic sort, we realized that the array will have a cycle 
due to the duplicate number and that the start of the cycle will always 
point to the duplicate number. This means that we can use the fast & the slow 
pointer method to find the duplicate number or the start of the cycle similar 
to Start of LinkedList Cycle.