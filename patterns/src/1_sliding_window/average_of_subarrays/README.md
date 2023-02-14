# Average Of Subarrays (easy) ✩

Given an array, find the average of all subarrays of ‘K’ contiguous elements in it.


####  Example 1
```
Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
Output: [2.2, 2.8, 2.4, 3.6, 2.8]

Explanation

- For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2
- The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5 => 2.8
- For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4
- For the next 5 numbers (subarray from index 3-7), the average is: (6-1+4+1+8)/5 => 3.6
- For the next 5 numbers (subarray from index 4-8), the average is: (-1+4+1+8+2)/5 => 2.8

```