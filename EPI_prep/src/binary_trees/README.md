# Binary Trees

Formally, a binary tree is either empty, or a root node / together with a left binary tree and a right binary tree. The subtrees themselves are binary trees. The left binary tree is sometimes referred to as the left subtree of the root, and the right binary tree is referred to as the right subtree of the root.

<br> 

## Terminologies

<br>

### Full binary tree
A full binary tree is a binary tree in which every node other than the leaves has two children. 
 A perfect binary tree of height ft contains exactly 2h+1 - 1 nodes, of which 2h are leaves.

<br>

### Perfect binary tree
A perfect binary tree is a full binary tree in which all leaves are at the same depth, and in which every parent has two children. 

<br>

### Complete binary tree
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.

<br>

### Left-skewed tree & Right-skewed tree
* A left-skewed tree is a tree in which no node has a right child; 
* A right-skewed tree is a tree in which no node has a left child. 
* In either case, we refer to the binary tree as being skewed.



<br> <br>

## Questions

In this section we will solve common binary tree questions that will help you understand the data structure very well. This will in turn give you the ability to solve other binary questions

* [Binary Tree Traversal](0_binary_tree_traversal/tree_traversals.py)
* [Is Binary Tree Height Balanced](1_is_binary_tree_height_balanced/balanced_binary_tree.py)
* [Is Binary Tree Symmetric](2_is_binary_tree_symmetric/is_symetric.py)
* [Lowest Common Ancestor](3_lca/lca.py)
* [Lowest Common Ancestor With Parent Pointers](4_lca_with_parent_pointers/lca.py)
* [Sum root to leaf](5_sum_root_to_leaf/sum_root_to_leaf.py)
* [Root to leaf path with specified sum](6_root_leaf_path_with_specified_sum/has_path_sum.py)
    * [Root to leaf path sum (All Paths) ](6.1_root_to_leaf_sum_all_paths/all_paths.py)
* [Inorder Traversal Without Recursion](7_inorder_traversal_without_recursion/inorder_traversal.py)
* [Preorder Traversal Without Recursion](8_preorder_traversal_without_recursion/preorder_traversal.py)
* [Kth Node in Inorder Traversal](9_kth_node_in_inorder_traversal/kth_node.py)
* [Compute Successor](10_compute_sucessor/compute_sucessor.py)
* [Inorder Traversal in Constant Space](11_inorder_traversal_in_constant_space/inorder_traversal.py)
    * [Preorder Traversal in Constant Space](11.1_preorder_traversal_in_constant_space/preorder_traversal.py)
    * [Postorder Traversal in Constant Space](11.2_postorder_traversal_in_constant_space/postorder_traversal.py)
* [Reconstruct Binary Tree](12_reconstruct_binary_tree/reconstruct_bt.py)
* [Reconstruct Binary Tree](13_reconstruct_bt_from_preorder_traversal/reconstruct_bt_1.py)
    * [Reconstruct Binary Tree 2](13_reconstruct_bt_from_preorder_traversal/reconstruct_bt_2.py)
* [Form a LinkedList From Leaves Of Binary Tree](14_form_a_linkedlist_from_leaves_of_bt/create_list_of_leaves.py)
    * [Form a LinkedList From Leaves Of Binary Tree 2](14_form_a_linkedlist_from_leaves_of_bt/create_2.py)
* [Compute Exterior of Binary Tree](15_compute_exterior_of_binary_tree/exterior_bt.py)
* [Compute Right Sibling Tree](16_compute_right_sibling_tree/compute_right_sibling_tree.py)
    