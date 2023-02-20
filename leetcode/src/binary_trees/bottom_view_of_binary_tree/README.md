# [Bottom View of Binary Tree - Medium](https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1)

Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

<br>


### Example 1

```
Input:

       20
    /    \
  8       22
/   \        \
5     3       25
    /   \      
   10    14

Output: 
For the above tree, the bottom view is [5, 10, 3, 14, 25]
```

### Example 2

```
Input:

       20
    /    \
  8       22
/   \     /   \
5      3 4     25
     /    \      
    10     14

Output: [5, 10, 4, 14, 25]

Explanation:
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later one in level traversal. 
For example, in the diagram above, 3 and 4 are both the bottommost nodes at horizontal distance 0, we need to print 4.

```

### Constraints:

- 1 <= Number of nodes <= 10^5
- 1 <= Data of a node <= 10^5