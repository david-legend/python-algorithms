# [LC 230. Kth Smallest Element in a BST - Medium](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

### Example 1

![Kth Smallest Element in a BST Example 1](https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg)  

```
Input: root = [3,1,4,null,2], k = 1
Output: 1
```

### Example 2 

![Kth Smallest Element in a BST Example 2](https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg)  

```
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```


### Constraints:

- The number of nodes in the tree is n.
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4