# [LC 687. Longest Univalue Path - Medium](https://leetcode.com/problems/longest-univalue-path/description/)

Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

### Example 1

![Longest Univalue Path Example 1](https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg)  


```
Input: root = [5,4,5,1,1,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 5).
```

### Example 2

![Longest Univalue Path Example 2](https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg)

```
Input: root = [1,4,5,4,4,null,5]
Output: 2
Explanation: The shown image shows that the longest path of the same value (i.e. 4).
```


### Constraints:

- The number of nodes in the tree is in the range [0, 10^4].
- -1000 <= Node.val <= 1000
- The depth of the tree will not exceed 1000.