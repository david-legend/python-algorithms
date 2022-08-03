# Binary Search Trees

Formally, a binary tree is either empty, or a root node / together with a left binary tree and a right binary tree. The subtrees themselves are binary trees. The left binary tree is sometimes referred to as the left subtree of the root, and the right binary tree is referred to as the right subtree of the root.

<br>

BST is a binary tree as defined above.  BST's are binary trees in which the nodes store keys that are comparable, eg, integers or strings. The keys stored at nodes have to respect the BST property which is --> the key stored at a node is greater than or equal to the keys stored at the nodes of its left subtree and less than or equal to the keys stored in the nodes of its right subtree.

<br> 


<br>

### Benefits
They offer the ability to efficiently search for a key as well as find the min aurrd max elements, look for the successor or predecessor of a search key (which itself need not be present in the BST), and enumerate the keys in a range in sorted order.

With a BST you can iterate through elements in sorted order in time O(n) (regardless of whether it is balanced).

<br>


<br> <br>

## Questions

In this section we will solve common binary search tree questions that will help you understand the data structure very well. This will in turn give you the ability to solve other binary search questions

* [Search Binary Tree](0_search_bst/search_bst.py)
    