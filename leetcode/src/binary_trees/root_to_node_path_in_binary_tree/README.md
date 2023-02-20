# [Root to Node Path In Binary Tree - Medium](https://www.interviewbit.com/problems/path-to-given-node/)

Given a Binary Tree A containing N nodes.  

You need to find the path from Root to a given node B.  

NOTE:  

No two nodes in the tree have same data values.
You can assume that B is present in the tree A and a path always exists.

### Example 1

```
Input:
 A =

           1
         /   \
        2     3
       / \   / \
      4   5 6   7 


B = 5
Output: [1, 2, 5]
```

### Example 2 

```
Input:
A = 
            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


B = 1

Output: [1]
```


### Constraints:

-  1 <= N <= 105 
-  1 <= Data Values of Each Node <= N
-  1 <= B <= N