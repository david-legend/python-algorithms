# Ceiling of a Number (medium) ✩

Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. 
The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’

Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.

### Example 1
Input: [4, 6, 10], key = 6
Output: 1
Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

### Example 2
Input: [1, 3, 8, 10, 15], key = 12
Output: 3
Explanation: The smallest number greater than or equal to '12' is '15' having index '4'.

### Example 3
Input: [4, 6, 10], key = 17
Output: 2
Explanation: There is no number greater than or equal to '17' in the given array.

### Example 4
Input: [4, 6, 10], key = -1
Output: -1
Explanation: The smallest number greater than or equal to '-1' is '4' having index '0'.