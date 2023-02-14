# [LC 115. Distinct Subsequences- Medium](https://leetcode.com/problems/distinct-subsequences/description/)

Given two strings s and t, return the number of distinct subsequences of s which equals t.  

The test cases are generated so that the answer fits on a 32-bit signed integer.  


### Example 1

![Letter Case Permutation Example 1](https://assets.leetcode.com/uploads/2019/05/02/tree.png)  

```
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit
```

### Example 2 

```
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag
```


### Constraints:

- 1 <= s.length, t.length <= 1000
- s and t consist of English letters.