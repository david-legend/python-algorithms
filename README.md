# Python Algorithms and Data Structures

This repository contains implementations of popular data structures and interview questions implemented in Python.

Each data structure has its own separate README
with related explanations and links for further reading (including ones
to YouTube videos).




*This project is my attempt to document the materials I have studied on my journey to understand data structures and also prepare for interviews.*


<br>
<br>


## Data Structures

A data structure is a particular way of organizing and storing data in a computer so that it can
be accessed and modified efficiently. More precisely, a data structure is a collection of data
values, the relationships among them, and the functions or operations that can be applied to
the data.

The explanations of the data structures below are from <a href="https://github.com/trekhleb/javascript-algorithms"> Oleksii Trekhleb's Project</a>

`B` - Beginner, `A` - Advanced

* `B` [Linked List](data-structures/src/linked-list)
* `B` [Circular Linked List](data-structures/src/circular-linked-list/circular_linked_list.py)
* `B` [Doubly Linked List](data-structures/src/doubly-linked-list)
* `B` [Circular Doubly Linked List](data-structures/src/circular-doubly-linked-list/circular_doubly_linked_list.py)
* `B` [Queue](data-structures/src/queue)
* `B` [Priority Queue](data-structures/src/priority_queue)
* `B` [Stack](data-structures/src/stack)
* `B` [Hash Table](data-structures/src/hashtable)
* `A` [Heap](data-structures/src/heap)
* `A` [Trie](data-structures/src/trie)
* `A` [Tree](data-structures/src/tree)
  * `A` [Binary Tree](data-structures/src/tree/binary-tree)
  * `A` [Binary Search Tree](data-structures/src/tree/binary-search-tree)
  * `A` [AVL Tree](data-structures/src/tree/avl-tree)
* `A` [Graphs](data-structures/src/graph)


<br>
<br>

## Patterns For Coding Interviews

This section categorizes coding interview problems into a set of 16 patterns. 
Under each pattern there will be a specific category of problems to solve. 
The goal is to develop an understanding of the underlying pattern, so that, we can apply that pattern to solve other problems.


* [Sliding Window](patterns/src/1_sliding_window)
* [Two Pointers](patterns/src/2_two_pointers)
* [Fast & Slow Pointers](patterns/src/3_fast_and_slow_pointers)
* [Merge Intervals](patterns/src/4_merge_intervals)
* [Cyclic Sort](patterns/src/5_cyclic_sort)
* [In-Place Reversal of Linkedlist](patterns/src/6_in_place_reversal_of_linkedlist)
* [Breath First Search](patterns/src/7_tree_breath_first_search)
* [Depth First Search](patterns/src/8_tree_depth_first_search)
* [Two Heaps](patterns/src/9_two_heaps)
* [Subsets](patterns/src/10_subsets)
* [Modified Binary Search](patterns/src/11_modified_binary_search)
* [Top K Elements](patterns/src/12_top_k_elements)
* [K Way Merge](patterns/src/13_k_way_merge)
* [Topological Sort](patterns/src/14_topological_sort)
* [Dynamic Programming Patterns](patterns/src/15_dynamic_programming)


<br>
<br>


## Elements Of Programming Interviews Prep

EPI is an invaluable book  textbook presents a comprehensive introduction to modern competitive programming.  
Below are solutions & questions found under various topics in the book.

* [Recursion](EPI_prep/src/recursion)
  * `E` [Greatest Common Divisor](EPI_prep/src/recursion/0_greatest_common_divisor/lca.py)
  * `M` [Towers Of Hanoi](EPI_prep/src/recursion/1_towers_of_hanoi/towers_of_hanoi.py)
  * `M` [Permutations](EPI_prep/src/recursion/3_permutations/permutations.py)
  * `M` [Power Set](EPI_prep/src/recursion/4_power_set/power_set.py)
  * `M` [Subset Of Size](EPI_prep/src/recursion/5_subset_of_size_k/combinations.py)
  * `M` [Kth Node in Inorder Traversal](EPI_prep/src/recursion/6_generate_balanced_parentheses/generate_balanced_parentheses.py)
  * `M` [Generate Palindromic Decompositions](EPI_prep/src/recursion/7_generate_palindromic_decompositions/palindromic_decompositions.py)
  * `M` [Generate Binary Trees](EPI_prep/src/recursion/8_generate_binary_trees/generate_binary_trees.py)
  * `M` [Compute Right Sibling Tree](EPI_prep/src/recursion/9_solve_sodoku/solve_sudoku.py)

* [Binary Trees](EPI_prep/src/binary_trees)
  * `E` [Binary Tree Traversal](EPI_prep/src/binary_trees/0_binary_tree_traversal/tree_traversals.py)
  * `E` [Is Binary Tree Height Balanced](EPI_prep/src/binary_trees/1_is_binary_tree_height_balanced/balanced_binary_tree.py)
  * `E` [Is Binary Tree Symmetric](EPI_prep/src/binary_trees/2_is_binary_tree_symmetric/is_symetric.py)
  * `M` [Lowest Common Ancestor](EPI_prep/src/binary_trees/3_lca/lca.py)
  * `M` [Lowest Common Ancestor With Parent Pointers](EPI_prep/src/binary_trees/4_lca_with_parent_pointers/lca.py)
  * `E` [Sum root to leaf](EPI_prep/src/binary_trees/5_sum_root_to_leaf/sum_root_to_leaf.py)
  * `E` [Root to leaf path with specified sum](EPI_prep/src/binary_trees/6_root_leaf_path_with_specified_sum/has_path_sum.py)
  * `M` [Root to leaf path sum (All Paths) ](EPI_prep/src/binary_trees/6.1_root_to_leaf_sum_all_paths/all_paths.py)
  * `E` [Inorder Traversal Without Recursion](EPI_prep/src/binary_trees/7_inorder_traversal_without_recursion/inorder_traversal.py)
  * `E` [Preorder Traversal Without Recursion](EPI_prep/src/binary_trees/8_preorder_traversal_without_recursion/preorder_traversal.py)
  * `E` [Kth Node in Inorder Traversal](EPI_prep/src/binary_trees/9_kth_node_in_inorder_traversal/kth_node.py)
  * `M` [Compute Successor](EPI_prep/src/binary_trees/10_compute_sucessor/compute_sucessor.py)
  * `M` [Inorder Traversal in Constant Space](EPI_prep/src/binary_trees/11_inorder_traversal_in_constant_space/inorder_traversal.py)
  * `M` [Preorder Traversal in Constant Space](EPI_prep/src/binary_trees/11.1_preorder_traversal_in_constant_space/preorder_traversal.py)
  * `M` [Postorder Traversal in Constant Space](EPI_prep/src/binary_trees/11.2_postorder_traversal_in_constant_space/postorder_traversal.py)
  * `M` [Reconstruct Binary Tree](EPI_prep/src/binary_trees/12_reconstruct_binary_tree_from_preorder_inorder_traversal/reconstruct_bt.py)
  * `M` [Reconstruct Binary Tree](EPI_prep/src/binary_trees/13_reconstruct_bt_from_preorder_traversal/reconstruct_bt_1.py)
  * `M` [Reconstruct Binary Tree 2](EPI_prep/src/binary_trees/13_reconstruct_bt_from_preorder_traversal/reconstruct_bt_2.py)
  * `M` [Form a LinkedList From Leaves Of Binary Tree](EPI_prep/src/binary_trees/14_form_a_linkedlist_from_leaves_of_bt/create_list_of_leaves.py)
  * `M` [Form a LinkedList From Leaves Of Binary Tree 2](EPI_prep/src/binary_trees/14_form_a_linkedlist_from_leaves_of_bt/create_2.py)
  * `M` [Compute Exterior of Binary Tree](EPI_prep/src/binary_trees/15_compute_exterior_of_binary_tree/exterior_bt.py)
  * `M` [Compute Right Sibling Tree](EPI_prep/src/binary_trees/16_compute_right_sibling_tree/compute_right_sibling_tree.py)

* [Binary Search Trees](EPI_prep/src/binary_search_trees)
  * `E` [Search Binary Tree](EPI_prep/src/binary_search_trees/0_search_bst/search_bst.py)
  * `E` [Check If Binary Search Tree Satisfies BST Property](EPI_prep/src/binary_search_trees/1_check_if_bst_satisfies_bst_property/is_bst.py)
  * `E` [Check If Binary Search Tree Satisfies BST Property - Solution 2](EPI_prep/src/binary_search_trees/1_check_if_bst_satisfies_bst_property/is_bst_2.py)
  * `E` [Find the First Key Greater Than A Given Value In A BST](EPI_prep/src/binary_search_trees/2_find_first_key_greater_than_a_value_in_bst/find_first_greater_than_k.py)
  * `E` [Find The K Largest Elements In A BST](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_1.py)
  * `E` [Find The K Largest Elements In A BST - Solution 2](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_2.py)
  * `E` [Find The K Largest Elements In A BST - Solution 3](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_3.py)
  * `M` [Compute The LCA In A BST](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_1.py)
  * `M` [Reconstruct A BST From Preorder Traversal Data](EPI_prep/src/binary_search_trees/5_reconstruct_bst_from_preorder_traversal_data/reconstruct_bst.py)
  * `M` [Find The Closest Entries In Three Sorted Arrays](EPI_prep/src/binary_search_trees/6_closest_entries_in_3_sorted_arrays/close_entries.py)
  * `M` [Reconstruct A BST From Postorder Traversal Data](EPI_prep/src/binary_search_trees/5.1_reconstruct_bst_from_post_order_traversal_data/reconstruct_bst.py) 
  * `M` [Reconstruct A BST From Inorder Traversal Data](EPI_prep/src/binary_search_trees/5.2_reconstruct_bst_from_inorder_traversal_data/reconstruct_bst.py) 
  * `M` [Enumerate Numbers Of The Form a + b sqrt2](EPI_prep/src/binary_search_trees/7_enumerate_numbers_of_the_form_a+b_sqrt2/enumerate_numbers_1.py)
  * `M` [Enumerate Numbers Of The Form a + b sqrt2 - Solution 2](EPI_prep/src/binary_search_trees/7_enumerate_numbers_of_the_form_a+b_sqrt2/enumerate_numbers.py)
  * `M` [Build A Minimum Height BST From A Sorted Array](EPI_prep/src/binary_search_trees/8_build_minimum_height_bst/min_height_bst.py)
  * `M` [Build A Minimum Height BST From A Sorted Array - Solution 2](EPI_prep/src/binary_search_trees/8_build_minimum_height_bst/min_height_bst_2.py)
  * `M` [Test If Three BST Nodes Are Totally Ordered](EPI_prep/src/binary_search_trees/9_ordered_bst_nodes/is_bst_ordered.py)
  * `M` [The Range Lookup Problem](EPI_prep/src/binary_search_trees/10_range_look_up_problem/range_lookup.py)
  * `M` [Add Credits](EPI_prep/src/binary_search_trees/11_add_credits/add_credits.py)

* [Heaps](EPI_prep/src/heaps)
  * `M` [Merge Sorted Arrays](EPI_prep/src/heaps/1_merge_sorted_arrays/merge_sorted_arrays.py)
  * `M` [Sort An Increasing Decreasing Array](EPI_prep/src/heaps/2_sort_increasing_decreasing_array/sort_k_inc_dec_array.py)
  * `M` [Sort An Almost Sorted Array](EPI_prep/src/heaps/3_sort_almost_sorted_array/sort_approximately_sorted_array.py)
  * `M` [Compute the K closest Stars](EPI_prep/src/heaps/4_compute_k_closest_stars/k_closest_stars.py)
  * `M` [Compute Median From A Stream](EPI_prep/src/heaps/5_compute_median_from_a_stream/compute_median.py)
  * `M` [K Largest Elements In A Max Heap](EPI_prep/src/heaps/6_k_largest_elements_in_a_heap/k_largest_elements.py)
  * `M` [K Largest Elements In A Max Heap - Solution 2](EPI_prep/src/heaps/6_k_largest_elements_in_a_heap/k_largest_elements_1.py)


* [Linkedlist](EPI_prep/src/linkedlist)
  * `E` [Merge Two Sorted Lists](EPI_prep/src/linkedlist/1_merge_two_sorted_lists/merge_two_list.py)
  * `E` [Merge Two Sorted Doubly LinkedList](EPI_prep/src/linkedlist/1.1_merge_two_sorted_doubly_linkedlist/merge_list.py)
  * `M` [Reverse A Sublist](EPI_prep/src/linkedlist/2_reverse_a_single_sublist/reverse_sublist_1.py)
  * `M` [Reverse A Sublist - Solution 2](EPI_prep/src/linkedlist/2_reverse_a_single_sublist/reverse_sublist_2.py)
  * `E` [Reverse A Singly LinkedList](EPI_prep/src/linkedlist/2.1_reverse_singly_linkedlist/reverse_singly_linkedlist.py)
  * `M` [Reverse Every K Sublist](EPI_prep/src/linkedlist/2.2_reverse_every_k_sublist/reverse_k_sublist.py)
  * `E` [Test For Cyclicity](EPI_prep/src/linkedlist/3_test_for_cyclicity/has_cycle.py)
  * `M` [Find The Start Of A Cycle In A LInkedList](EPI_prep/src/linkedlist/3.1_start_of_linkedlist_cycle/find_cycle_start_1.py)
  * `M` [Find The Start Of A Cycle In A LInkedList - Solution 2](EPI_prep/src/linkedlist/3.1_start_of_linkedlist_cycle/find_cycle_start_2.py)
  * `E` [Test For Overlapping List - Lists Are Cycle Free](EPI_prep/src/linkedlist/4_test_for_overlapping_lists/has_overlapping_list.py)
  * `M` [Test For Overlapping List - Lists May Have Cycles](EPI_prep/src/linkedlist/4_test_for_overlapping_lists/has_overlapping_list.py)
  * `E` [Delete Node From Singly Linkedlist](EPI_prep/src/linkedlist/6_delete_node_from_singly_linkedlist/delete_node.py)
  * `M` [Remove Kth Last Element From List](EPI_prep/src/linkedlist/7_remove_kth_last_element_from_list/remove_kth_last_element.py)
  * `E` [Remove Duplicates From Sorted Lists](EPI_prep/src/linkedlist/8_remove_duplicates_from_sorted_list/remove_duplicates.py)
  * `M` [Implement Cyclic Right Shift For Singly LinkedList](EPI_prep/src/linkedlist/9_cyclic_right_shift_of_singly_linkedlist/cyclic_right_shift_list.py)
  * `M` [Even Odd Merge](EPI_prep/src/linkedlist/10_even_odd_merge/even_odd_merge.py)
  * `E` [Test If Singly LinkedList Is Palindromic](EPI_prep/src/linkedlist/11_palindromic_linkedlist/is_palindrome.py)
  * `M` [Implement List Pivoting](EPI_prep/src/linkedlist/12_implement_list_pivoting/list_pivoting.py)
  * `M` [Add Two LinkedLists](EPI_prep/src/linkedlist/13_add_two_linkedlists/add_lists.py)



<br>
<br>


## Blind 75 Questions

* [Arrays](blind_75/src/arrays)
  * `E` [Two Sum](blind_75/src/arrays/two_sum)
  * `E` [Best Time To Buy And Sell Stock](blind_75/src/arrays/buy_and_sell_stock)
  * `E` [Contains Duplicate](blind_75/src/arrays/contains_duplicate)
  * `M` [Product of Array Except Self](blind_75/src/arrays/product_of_array_except_self)
  * `E` [Maximum Subarray](blind_75/src/arrays/maximum_subarray)

* [Trees](blind_75/src/trees)
  * `M` [Validate Binary Search Tree](blind_75/src/trees/lc_98_validate_binary_search_tree/validate_binary_search_tree.py)
  * `E` [Same Tree](blind_75/src/trees/lc_100_same_tree/same_tree.py)
  * `M` [Binary Tree Level Order Traversal](blind_75/src/trees/lc_102_binary_tree_level_order_traversal/binary_tree_level_order_traversal.py)
  * `E` [Maximum Depth of Binary Tree](blind_75/src/trees/lc_104_max_depth_of_binary_tree/max_depth_of_binary_tree.py)
  * `M` [Construct Binary Tree from Preorder and Inorder Traversal ](blind_75/src/trees/lc_105_construct_binary_tree_from_preorder_inorder_traversal/construct_binary_tree_from_preorder_inorder_traversal.py)
  * `H` [Binary Tree Maximum Path Sum](blind_75/src/trees/lc_124_binary_tree_maximum_path_sum/binary_tree_maximum_path_sum.py)
  * `E` [Invert Binary Tree](blind_75/src/trees/lc_226_invert_binary_tree/invert_binary_tree.py)
  * `M` [Kth Smallest Element in a BST](blind_75/src/trees/lc_230_kth_smallest_in_bst/kth_smallest_in_bst.py)
  * `E` [Lowest Common Ancestor of a Binary Search Tree](blind_75/src/trees/lc_235_lca_of_binary_search_tree/lca_bst.py)
  * `H` [Serialize and Deserialize Binary Tree](blind_75/src/trees/lc_297_serialize_and_deserialize_binary_tree/serialize_and_deserialize_binary_tree.py)
  * `E` [Subtree of Another Tree ](blind_75/src/trees/lc_572_subtree_of_another_tree/subtree_of_another_tree.py)


* [LinkedLists](blind_75/src/linkedlists)
  * `M` [Remove Nth Node From End of List](blind_75/src/linkedlists/lc_19_remove_nth_node_from_list/remove_nth_node_from_list.py)
  * `E` [Merge Two Sorted Lists](blind_75/src/linkedlists/lc_21_merge_two_sorted_lists/merge_two_sorted_lists.py)
  * `E` [Merge k Sorted Lists](blind_75/src/linkedlists/lc_23_merge_k_sorted_lists/merge_k_sorted_lists.py)
  * `E` [Linked List Cycle](blind_75/src/linkedlists/lc_141_linkedlist_cycle/linkedlist_cycle.py)
  * `M` [Reorder List](blind_75/src/linkedlists/lc_143_reorder_list/reorder_list.py)
  * `E` [Reverse Linked List](blind_75/src/linkedlists/lc_206_reverse_linkedlist/reverse_linkedlist.py)
  
<br>
<br>

## Leetcode Questions Categorized By Concept & Data Structure

`E` - Easy, `M` - Medium , `H` - Hard,

* [Recursion](leetcode/src/recursion)
    * `M` [Longest Univalue Path](leetcode/src/recursion/lc_687_longest_univalue_path/longest_univalue_path.py)

<br>

* [Binary Trees](leetcode/src/binary_trees)
    * `E` [Binary Tree Inorder Traversal](leetcode/src/binary_trees/lc_94_inorder_traversal/inorder_traversal.py)
    * `E` [Same Tree](leetcode/src/binary_trees/lc_100_same_tree/same_tree.py)
    * `E` [Symmetric Tree](leetcode/src/binary_trees/lc_101_symmetric_tree/symmetric_tree.py)
    * `E` [Maximum Depth of Binary Tree](leetcode/src/binary_trees/lc_104_max_depth_of_binary_tree/max_depth_of_binary_tree.py)
    * `E` [Convert Sorted Array to Binary Search Tree](leetcode/src/binary_trees/lc_108_converted_sorted_array_to_bst/converted_sorted_array_to_bst.py)
    * `E` [Balanced Binary Tree](leetcode/src/binary_trees/lc_110_balanced_binary_tree/balanced_binary_tree.py)
    * `E` [Minimum Depth of Binary Tree](leetcode/src/binary_trees/lc_111_min_depth_of_binary_tree/min_depth_of_binary_tree.py)
    * `E` [Path Sum](leetcode/src/binary_trees/lc_112_path_sum/path_sum.py)
    * `E` [Binary Tree Preorder Traversal](leetcode/src/binary_trees/lc_144_preorder_traversal/preorder_traversal.py)
    * `E` [Binary Tree Postorder Traversal](leetcode/src/binary_trees/lc_145_postorder_traversal/postorder_traversal.py)
    * `E` [Invert Binary Tree](leetcode/src/binary_trees/lc_226_invert_binary_tree/invert_binary_tree.py)
    * `E` [Lowest Common Ancestor of a Binary Search Tree](leetcode/src/binary_trees/lc_235_lca_of_binary_search_tree/lca_bst.py)
    * `E` [Binary Tree Paths](leetcode/src/binary_trees/lc_257_binary_tree_paths/lca_binary_tree_pathsbst.py)
    * `E` [Sum of Left Leaves](leetcode/src/binary_trees/lc_404_sum_of_left_leaves/sum_of_left_leaves.py)
    * `E` [Find Mode in Binary Search Tree](leetcode/src/binary_trees/lc_501_find_mode_in_bst/find_mode_in_bst.py)
    * `E` [Minimum Absolute Difference in BST](leetcode/src/binary_trees/lc_530_minimum_absolute_diff_in_bst/min_absolute_diff_in_bst.py)
    * `E` [Diameter of Binary Tree](leetcode/src/binary_trees/lc_543_diameter_of_a_tree/tree_diameter.py)
    * `E` [Binary Tree Tilt ](leetcode/src/binary_trees/lc_563_binary_tree_tilt/binary_tree_tilt.py)
    * `E` [Subtree of Another Tree ](leetcode/src/binary_trees/lc_572_subtree_of_another_tree/subtree_of_another_tree.py)
    * `E` [Construct String from Binary Tree ](leetcode/src/binary_trees/lc_606_construct_string_from_tree/construct_string_from_tree.py)
    * `E` [Merge Two Binary Trees ](leetcode/src/binary_trees/lc_617_merge_two_binary_trees/merge_two_binary_trees.py)
    * `E` [Average of Levels in Binary Tree ](leetcode/src/binary_trees/lc_637_average_of_levels_in_binary_tree/average_of_levels_in_binary_tree.py)
    * `E` [Two Sum IV - Input is a BST ](leetcode/src/binary_trees/lc_653_two_sum_IV/two_sum.py)
    * `E` [Second Minimum Node In a Binary Tree ](leetcode/src/binary_trees/lc_671_second_minimum_node_in_binary_tree/second_minimum_node_in_binary_tree.py)
    * `E` [Minimum Distance Between BST Nodes](leetcode/src/binary_trees/lc_783_min_distance_between_bst_nodes/min_distance_between_bst_nodes.py)
    * `M` [Unique Binary Search Trees II](leetcode/src/binary_trees/lc_95_unique_binary_search_trees_II/unique_binary_search_trees.py)
    * `M` [Unique Binary Search Trees](leetcode/src/binary_trees/lc_96_unique_binary_search_trees/unique_binary_search_trees.py)
    * `M` [Validate Binary Search Tree](leetcode/src/binary_trees/lc_98_validate_binary_search_tree/validate_binary_search_tree.py)
    * `M` [Recover Binary Search Tree](leetcode/src/binary_trees/lc_99_recover_binary_search_trees/recover_binary_search_trees.py)
    * `M` [Binary Tree Level Order Traversal](leetcode/src/binary_trees/lc_102_binary_tree_level_order_traversal/binary_tree_level_order_traversal.py)
    * `M` [Binary Tree Zigzag Level Order Traversal](leetcode/src/binary_trees/lc_103_binary_tree_zigzag_level_order_traversal/binary_tree_zigzag_level_order_traversal.py)
    * `M` [Construct Binary Tree from Preorder and Inorder Traversal ](leetcode/src/binary_trees/lc_105_construct_binary_tree_from_preorder_inorder_traversal/construct_binary_tree_from_preorder_inorder_traversal.py)
    * `M` [Construct Binary Tree from Inorder and Postorder Traversal](leetcode/src/binary_trees/lc_106_construct_binary_tree_from_inorder_postorder_traversal/construct_binary_tree_from_inorder_postorder_traversal.py)
    * `M` [Binary Tree Level Order Traversal II](leetcode/src/binary_trees/lc_107_binary_tree_level_order_traversal_II/binary_tree_level_order_traversal.py)
    * `M` [Path Sum II](leetcode/src/binary_trees/lc_113_path_sum_II/path_sum.py)
    * `M` [Flatten Binary Tree to Linked List](leetcode/src/binary_trees/lc_114_flatten_binary_tree_to_linkedlist/flatten_binary_tree_to_linkedlist.py)
    * `M` [Populating Next Right Pointers in Each Node](leetcode/src/binary_trees/lc_116_populate_next_right_pointers_in_each_node/populate_next_right_pointers.py)
    * `M` [Populating Next Right Pointers in Each Node II](leetcode/src/binary_trees/lc_117_populate_next_right_pointer_in_each_node_II/populate_next_right_pointers.py)
    * `M` [Sum Root to Leaf Numbers](leetcode/src/binary_trees/lc_129_sum_root_to_leaf_numbers/sum_root_to_leaf_numbers.py)
    * `M` [Binary Search Tree Iterator](leetcode/src/binary_trees/lc_173_binary_search_tree_iterator/binary_search_tree_iterator.py)
    * `M` [Binary Tree Right Side View](leetcode/src/binary_trees/lc_199_binary_tree_right_side_view/binary_tree_right_side_view.py)
    * `M` [Count Complete Tree Nodes](leetcode/src/binary_trees/lc_222_count_complete_tree_nodes/count_complete_tree_nodes.py)
    * `M` [Kth Smallest Element in a BST](leetcode/src/binary_trees/lc_230_kth_smallest_in_bst/kth_smallest_in_bst.py)
    * `M` [Lowest Common Ancestor of a Binary Tree](leetcode/src/binary_trees/lc_236_lowest_common_ancestor_of_binary_tree/lowest_common_ancestor_of_binary_tree.py)
    * `M` [House Robber III](leetcode/src/binary_trees/lc_337_house_robber_III/house_robber.py)
    * `M` [Path Sum III](leetcode/src/binary_trees/lc_437_path_sum_III/path_sum.py)
    * `M` [Serialize and Deserialize BST](leetcode/src/binary_trees/lc_449_serialize_deserialize_bst/serialize_deserialize_bst.py)
    * `M` [Delete Node in a BST](leetcode/src/binary_trees/lc_450_delete_bst_node/delete_bst_node.py)
    * `M` [Most Frequent Subtree Sum](leetcode/src/binary_trees/lc_508_most_frequent_subtree_sum/most_frequent_subtree_sum.py)
    * `M` [Find Bottom Left Tree Value](leetcode/src/binary_trees/lc_513_find_bottom_left_tree_value/find_bottom_left_tree_value.py)
    * `M` [Find Largest Value in Each Tree Row](leetcode/src/binary_trees/lc_515_find_largest_value_in_each_tree_row/find_largest_value_in_each_tree_row.py)
    * `M` [Convert BST to Greater Tree](leetcode/src/binary_trees/lc_538_convert_bst_to_greater_tree/convert_bst_to_greater_tree.py)
    * `M` [Add One Row to Tree](leetcode/src/binary_trees/lc_623_add_one_row_to_tree/add_one_row_to_tree.py)
    * `M` [Find Duplicate Subtrees](leetcode/src/binary_trees/lc_652_find_duplicate_subtrees/find_duplicate_subtrees.py)
    * `M` [Maximum Binary Tree](leetcode/src/binary_trees/lc_654_maximum_binary_tree/maximum_binary_tree.py)
    * `M` [Print Binary Tree](leetcode/src/binary_trees/lc_655_print_binary_tree/print_binary_tree.py)
    * `M` [Maximum Width of Binary Tree](leetcode/src/binary_trees/lc_662_maximum_width_of_binary_tree/maximum_width_of_binary_tree.py)
    * `M` [Trim a Binary Search Tree](leetcode/src/binary_trees/lc_669_trim_a_binary_search_tree/trim_a_binary_search_tree.py)
    * `M` [Longest Univalue Path](leetcode/src/binary_trees/lc_687_longest_univalue_path/longest_univalue_path.py)
    * `M` [All Nodes Distance K in Binary Tree](leetcode/src/binary_trees/lc_863_all_nodes_distance_k_binary_tree/all_nodes_distance_k_binary_tree.py)
    * `M` [Smallest String Starting From Leaf](leetcode/src/binary_trees/lc_988_smallest_string_starting_from_leaf/smallest_string_starting_from_leaf.py)
    * `M` [Maximum Binary Tree II](leetcode/src/binary_trees/lc_998_maximum_binary_tree_II/maximum_binary_tree.py)
    * `M` [Construct Binary Search Tree from Preorder Traversal](leetcode/src/binary_trees/lc_1008_construct_binary_tree_from_preorder_traversal/construct_binary_tree_from_preorder_traversal.py)
    * `H` [Binary Tree Maximum Path Sum](leetcode/src/binary_trees/lc_124_binary_tree_maximum_path_sum/binary_tree_maximum_path_sum.py)
    * `H` [Serialize and Deserialize Binary Tree](leetcode/src/binary_trees/lc_297_serialize_and_deserialize_binary_tree/serialize_and_deserialize_binary_tree.py)

<br>

* [LinkedLists](leetcode/src/linkedlist )
    * `E` [Merge Two Sorted Lists](leetcode/src/linkedlist/lc_21_merge_two_sorted_lists/merge_two_sorted_lists.py)
    * `E` [Remove Duplicates from Sorted List I](leetcode/src/linkedlist/lc_83_remove_duplicates_from_sorted_list/remove_duplicates_from_sorted_list.py)
    * `E` [Linked List Cycle](leetcode/src/linkedlist/lc_141_linkedlist_cycle/linkedlist_cycle.py)
    * `E` [Intersection of Two Linked Lists](leetcode/src/linkedlist/lc_160_intersection_of_two_linkedlists/intersection_of_two_linkedlists.py)
    * `E` [Remove Linked List Elements](leetcode/src/linkedlist/lc_203_remove_linkedlist_elements/remove_linkedlist_elements.py)
    * `E` [Reverse Linked List](leetcode/src/linkedlist/lc_206_reverse_linkedlist/reverse_linkedlist.py)
    * `E` [Palindrome Linked List](leetcode/src/linkedlist/lc_234_palindrome_linkedlist/palindrome_linkedlist.py)
    * `M` [Add Two Numbers](leetcode/src/linkedlist/lc_2_add_two_numbers/add_two_numbers.py)
    * `M` [Remove Nth Node From End of List](leetcode/src/linkedlist/lc_19_remove_nth_node_from_list/remove_nth_node_from_list.py)
    * `M` [Swap Nodes in Pairs](leetcode/src/linkedlist/lc_24_swap_nodes_in_pairs/swap_nodes_in_pairs.py)
    * `M` [Rotate List](leetcode/src/linkedlist/lc_61_rotate_list/rotate_list.py)
    * `M` [Remove Duplicates from Sorted List II](leetcode/src/linkedlist/lc_82_remove_duplicates_from_sorted_list_II/remove_duplicates_from_sorted_list_II.py)
    * `M` [Partition List](leetcode/src/linkedlist/lc_86_partition_list/partition_list.py)
    * `M` [Reverse Linked List II](leetcode/src/linkedlist/lc_92_reverse_linkedlist_II/reverse_linkedlist_II.py)
    * `M` [Convert Sorted List to Binary Search Tree](leetcode/src/linkedlist/lc_109_convert_sorted_list_binary_tree/convert_sorted_list_binary_tree.py)
    * `M` [Copy List with Random Pointer](leetcode/src/linkedlist/lc_138_copy_list_with_random_pointer/copy_list_with_random_pointer.py)
    * `M` [Linked List Cycle II](leetcode/src/linkedlist/lc_142_linkedlist_cycle_II/linkedlist_cycle.py)
    * `M` [Reorder List](leetcode/src/linkedlist/lc_143_reorder_list/reorder_list.py)
    * `M` [Insertion Sort List](leetcode/src/linkedlist/lc_147_insertion_sort/insertion_sort.py)
    * `M` [Sort List](leetcode/src/linkedlist/lc_148_sort_list/sort_list.py)
    * `M` [Delete Node in a Linked List](leetcode/src/linkedlist/lc_237_delete_node_in_linkedlist/delete_node_in_linkedlist.py)
    * `M` [Odd Even Linked List](leetcode/src/linkedlist/lc_328_odd_even_linkedlist/odd_even_linkedlist.py)
    * `M` [Add Two Numbers II](leetcode/src/linkedlist/lc_445_add_two_numbers_II/add_two_numbers.py)
    * `M` [Split Linked List in Parts](leetcode/src/linkedlist/lc_725_split_linkedlist_in_parts/split_linkedlist_in_parts.py)
    * `H` [Merge k Sorted Lists](leetcode/src/linkedlist/lc_23_merge_k_sorted_lists/merge_k_sorted_lists.py)
    * `H` [Reverse Nodes in k-Groups](leetcode/src/linkedlist/lc_25_reverse_nodes_in_k_groups/reverse_nodes_in_k_groups.py)

<br>

## Algorithms

A list of popular algorithms asked during Interviews

* [Graph Algorithms](algorithms/src/graph_algorithms)
* [Greedy Algorithms](algorithms/src/greedy_algorithms)
* [Sorting Algorithms](algorithms/src/sorting_algorithms)
* [General Algorithms](algorithms/src/general_algorithms)


<br>
<br>

## Recursion Crash Course
A simple crash course to get you up and started with recursion

* [Recursion With Strings](recursion_crash_course/src/1_recursion_with_strings)
* [Recursion With Numbers](recursion_crash_course/src/2_recursion_with_numbers)
* [Divide & Conquer](recursion_crash_course/src/3_divide_and_conquer)



<br>
<br>


## Useful Information

### References

[▶ Data Structures and Algorithms on YouTube](https://www.youtube.com/playlist?list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)

<br>

### Big O Notation

*Big O notation* is used to classify algorithms according to how their running time or space requirements grow as the input size grows.
On the chart below you may find most common orders of growth of algorithms specified in Big O notation.

![Big O graphs](./assets/big-o-graph.png)

Source: [Big O Cheat Sheet](http://bigocheatsheet.com/).

<br>
<br>

Below is the list of some of the most used Big O notations and their performance comparisons against different sizes of the input data.

| Big O Notation | Computations for 10 elements | Computations for 100 elements | Computations for 1000 elements  |
| -------------- | ---------------------------- | ----------------------------- | ------------------------------- |
| **O(1)**       | 1                            | 1                             | 1                               |
| **O(log N)**   | 3                            | 6                             | 9                               |
| **O(N)**       | 10                           | 100                           | 1000                            |
| **O(N log N)** | 30                           | 600                           | 9000                            |
| **O(N^2)**     | 100                          | 10000                         | 1000000                         |
| **O(2^N)**     | 1024                         | 1.26e+29                      | 1.07e+301                       |
| **O(N!)**      | 3628800                      | 9.3e+157                      | 4.02e+2567                      |


<br>
<br>

### Data Structure Operations Complexity

| Data Structure          | Access    | Search    | Insertion | Deletion  | Comments  |
| ----------------------- | :-------: | :-------: | :-------: | :-------: | :-------- |
| **Array**               | 1         | n         | n         | n         |           |
| **Stack**               | n         | n         | 1         | 1         |           |
| **Queue**               | n         | n         | 1         | 1         |           |
| **Linked List**         | n         | n         | 1         | n         |           |
| **Hash Table**          | -         | n         | n         | n         | In case of perfect hash function costs would be O(1) |
| **Binary Search Tree**  | n         | n         | n         | n         | In case of balanced tree costs would be O(log(n)) |
| **B-Tree**              | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **Red-Black Tree**      | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **AVL Tree**            | log(n)    | log(n)    | log(n)    | log(n)    |           |
| **Bloom Filter**        | -         | 1         | 1         | -         | False positives are possible while searching |


<br>
<br>

### Array Sorting Algorithms Complexity

| Name                  | Best            | Average             | Worst               | Memory    | Stable    | Comments  |
| --------------------- | :-------------: | :-----------------: | :-----------------: | :-------: | :-------: | :-------- |
| **Bubble sort**       | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Yes       |           |
| **Insertion sort**    | n               | n<sup>2</sup>       | n<sup>2</sup>       | 1         | Yes       |           |
| **Selection sort**    | n<sup>2</sup>   | n<sup>2</sup>       | n<sup>2</sup>       | 1         | No        |           |
| **Heap sort**         | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | 1         | No        |           |
| **Merge sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n&nbsp;log(n)       | n         | Yes       |           |
| **Quick sort**        | n&nbsp;log(n)   | n&nbsp;log(n)       | n<sup>2</sup>       | log(n)    | No        | Quicksort is usually done in-place with O(log(n)) stack space |
| **Shell sort**        | n&nbsp;log(n)   | depends on gap sequence   | n&nbsp;(log(n))<sup>2</sup>  | 1         | No         |           |
| **Counting sort**     | n + r           | n + r               | n + r               | n + r     | Yes       | r - biggest number in array |
| **Radix sort**        | n * k           | n * k               | n * k               | n + k     | Yes       | k - length of longest key |


