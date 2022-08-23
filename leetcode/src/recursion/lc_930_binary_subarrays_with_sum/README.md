<!-- <a name="687. Longest Univalue Path - Medium"></a> -->
# [LC 930. Binary Subarrays With Sum - Medium](https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/description/)

Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.  

A subarray is a contiguous part of the array.        

<br>

### Example 1
```
Input: nums = [1,0,1,0,1], goal = 2
Output: 4
Explanation: The 4 subarrays are bolded and underlined below:
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
```


<br>

### Example 2
```
Input: nums = [0,0,0,0,0], goal = 0
Output: 15
```

### Constraints:

- 1 <= nums.length <= 3 * 104
- nums[i] is either 0 or 1.
- 0 <= goal <= nums.length