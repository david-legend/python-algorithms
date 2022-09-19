# [LC 222. Count Complete Tree Nodes - Medium](https://leetcode.com/problems/count-complete-tree-nodes/description/)

Given the root of a complete binary tree, return the number of the nodes in the tree.  

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.  

Design an algorithm that runs in less than O(n) time complexity.   

### Example 1

![Most Frequent Subtree Sum Example 1](https://assets.leetcode.com/uploads/2021/01/14/complete.jpg)  

```
Input: root = [1,2,3,4,5,6]
Output: 6
```

### Example 2 

```
Input: root = []
Output: 0
```

### Example 3 

```
Input: root = [1]
Output: 1
```

### Constraints:

- The number of nodes in the tree is in the range [1, 10^4].
- -10^5 <= Node.val <= 10^5