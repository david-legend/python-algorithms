# [LC 653. Two Sum IV - Input is a BST - Easy](https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/)

Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.   

### Example 1

![Two Sum IV - Input is a BST Example 1](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg)  

```
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
```

### Example 2 

![Two Sum IV - Input is a BST Example 2](https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg)  

```
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
```


### Constraints:

- The number of nodes in the tree is in the range [1, 10^4].
- -10^4 <= Node.val <= 10^4
- root is guaranteed to be a valid binary search tree.
- -10^5 <= k <= 10^5