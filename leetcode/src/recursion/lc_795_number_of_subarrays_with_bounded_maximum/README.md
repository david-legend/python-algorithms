<!-- <a name="687. Longest Univalue Path - Medium"></a> -->
# [LC 795. Number Of Subarrays With Bounded Maximum - Medium](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/)

Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].  

The test cases are generated so that the answer will fit in a 32-bit integer.       

<br>

### Example 1
```
Input: nums = [2,1,4,3], left = 2, right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
```


<br>

### Example 2
```
Input: nums = [2,9,2,5,6], left = 2, right = 8
Output: 7
```

### Constraints:

- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= left <= right <= 10^9