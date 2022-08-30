# Binary Search Trees

Formally, a binary tree is either empty, or a root node / together with a left binary tree and a right binary tree. The subtrees themselves are binary trees. The left binary tree is sometimes referred to as the left subtree of the root, and the right binary tree is referred to as the right subtree of the root.

<br>

BST is a binary tree as defined above. BST's are binary trees in which the nodes store keys that are comparable, eg, integers or strings. The keys stored at nodes have to respect the BST property which is --> the key stored at a node is greater than or equal to the keys stored at the nodes of its left subtree and less than or equal to the keys stored in the nodes of its right subtree.

<br>

<br>

### Benefits

They offer the ability to efficiently search for a key as well as find the min aurrd max elements, look for the successor or predecessor of a search key (which itself need not be present in the BST), and enumerate the keys in a range in sorted order.

With a BST you can iterate through elements in sorted order in time O(n) (regardless of whether it is balanced).

<br>

<br> <br>

## Questions

In this section we will solve common binary search tree questions that will help you understand the data structure very well. This will in turn give you the ability to solve other binary search questions

- [Search Binary Tree](0_search_bst/search_bst.py)
- [Check If Binary Search Tree Satisfies BST Property](1_check_if_bst_satisfies_bst_property/is_bst.py)
  - [Check If Binary Search Tree Satisfies BST Property - Solution 2](1_check_if_bst_satisfies_bst_property/is_bst_2.py)
- [Find the First Key Greater Than A Given Value In A BST](2_find_first_key_greater_than_a_value_in_bst/find_first_greater_than_k.py)
- [Find The K Largest Elements In A BST](3_k_largest_in_bst/k_largest_1.py)
  - [Find The K Largest Elements In A BST - Solution 2](3_k_largest_in_bst/k_largest_2.py)
  - [Find The K Largest Elements In A BST - Solution 3](3_k_largest_in_bst/k_largest_3.py)
- [Compute The LCA In A BST](3_k_largest_in_bst/k_largest_1.py)
- [Reconstruct A BST From Preorder Traversal Data](5_reconstruct_bst_from_preorder_traversal_data/reconstruct_bst.py)
- [Find The Closest Entries In Three Sorted Arrays](6_closest_entries_in_3_sorted_arrays/close_entries.py)
  - [Reconstruct A BST From Postorder Traversal Data](5.1_reconstruct_bst_from_post_order_traversal_data/reconstruct_bst.py) 
- [Reconstruct A BST From Inorder Traversal Data](5.2_reconstruct_bst_from_inorder_traversal_data/reconstruct_bst.py) 
- [Enumerate Numbers Of The Form a + b sqrt2](7_enumerate_numbers_of_the_form_a+b_sqrt2/enumerate_numbers_1.py)
  - [Enumerate Numbers Of The Form a + b sqrt2 - Solution 2](7_enumerate_numbers_of_the_form_a+b_sqrt2/enumerate_numbers.py)
- [Build A Minimum Height BST From A Sorted Array](8_build_minimum_height_bst/min_height_bst.py)
  - [Build A Minimum Height BST From A Sorted Array - Solution 2](8_build_minimum_height_bst/min_height_bst_2.py)
- [Test If Three BST Nodes Are Totally Ordered](9_ordered_bst_nodes/is_bst_ordered.py)
- [The Range Lookup Problem](10_range_look_up_problem/range_lookup.py)
- [Add Credits](11_add_credits/add_credits.py)
