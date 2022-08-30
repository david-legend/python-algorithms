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
* `B` [Stack](data-structures/src/stack)
* `A` [Heap](data-structures/src/heap)
* `A` [Tree](data-structures/src/tree)
  * `A` [Binary Tree](data-structures/src/tree/binary-tree)
  * `A` [Binary Search Tree](data-structures/src/tree/binary-search-tree)
  * `A` [AVL Tree](data-structures/src/tree/avl-tree)


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
  * [Greatest Common Divisor](EPI_prep/src/recursion/0_greatest_common_divisor/lca.py)
  * [Towers Of Hanoi](EPI_prep/src/recursion/1_towers_of_hanoi/towers_of_hanoi.py)
  * [Permutations](EPI_prep/src/recursion/3_permutations/permutations.py)
  * [Power Set](EPI_prep/src/recursion/4_power_set/power_set.py)
  * [Subset Of Size](EPI_prep/src/recursion/5_subset_of_size_k/combinations.py)
  * [Kth Node in Inorder Traversal](EPI_prep/src/recursion/6_generate_balanced_parentheses/generate_balanced_parentheses.py)
  * [Generate Palindromic Decompositions](EPI_prep/src/recursion/7_generate_palindromic_decompositions/palindromic_decompositions.py)
  * [Generate Binary Trees](EPI_prep/src/recursion/8_generate_binary_trees/generate_binary_trees.py)
  * [Compute Right Sibling Tree](EPI_prep/src/recursion/9_solve_sodoku/solve_sudoku.py)

* [Binary Trees](EPI_prep/src/binary_trees)
  * [Binary Tree Traversal](EPI_prep/src/binary_trees/0_binary_tree_traversal/tree_traversals.py)
  * [Is Binary Tree Height Balanced](EPI_prep/src/binary_trees/1_is_binary_tree_height_balanced/balanced_binary_tree.py)
  * [Is Binary Tree Symmetric](EPI_prep/src/binary_trees/2_is_binary_tree_symmetric/is_symetric.py)
  * [Lowest Common Ancestor](EPI_prep/src/binary_trees/3_lca/lca.py)
  * [Lowest Common Ancestor With Parent Pointers](EPI_prep/src/binary_trees/4_lca_with_parent_pointers/lca.py)
  * [Sum root to leaf](EPI_prep/src/binary_trees/5_sum_root_to_leaf/sum_root_to_leaf.py)
  * [Root to leaf path with specified sum](EPI_prep/src/binary_trees/6_root_leaf_path_with_specified_sum/has_path_sum.py)
      * [Root to leaf path sum (All Paths) ](EPI_prep/src/binary_trees/6.1_root_to_leaf_sum_all_paths/all_paths.py)
  * [Inorder Traversal Without Recursion](EPI_prep/src/binary_trees/7_inorder_traversal_without_recursion/inorder_traversal.py)
  * [Preorder Traversal Without Recursion](EPI_prep/src/binary_trees/8_preorder_traversal_without_recursion/preorder_traversal.py)
  * [Kth Node in Inorder Traversal](EPI_prep/src/binary_trees/9_kth_node_in_inorder_traversal/kth_node.py)
  * [Compute Successor](EPI_prep/src/binary_trees/10_compute_sucessor/compute_sucessor.py)
  * [Inorder Traversal in Constant Space](EPI_prep/src/binary_trees/11_inorder_traversal_in_constant_space/inorder_traversal.py)
      * [Preorder Traversal in Constant Space](EPI_prep/src/binary_trees/11.1_preorder_traversal_in_constant_space/preorder_traversal.py)
      * [Postorder Traversal in Constant Space](EPI_prep/src/binary_trees/11.2_postorder_traversal_in_constant_space/postorder_traversal.py)
  * [Reconstruct Binary Tree](EPI_prep/src/binary_trees/12_reconstruct_binary_tree/reconstruct_bt.py)
  * [Reconstruct Binary Tree](EPI_prep/src/binary_trees/13_reconstruct_bt_from_preorder_traversal/reconstruct_bt_1.py)
      * [Reconstruct Binary Tree 2](EPI_prep/src/binary_trees/13_reconstruct_bt_from_preorder_traversal/reconstruct_bt_2.py)
  * [Form a LinkedList From Leaves Of Binary Tree](EPI_prep/src/binary_trees/14_form_a_linkedlist_from_leaves_of_bt/create_list_of_leaves.py)
      * [Form a LinkedList From Leaves Of Binary Tree 2](EPI_prep/src/binary_trees/14_form_a_linkedlist_from_leaves_of_bt/create_2.py)
  * [Compute Exterior of Binary Tree](EPI_prep/src/binary_trees/15_compute_exterior_of_binary_tree/exterior_bt.py)
  * [Compute Right Sibling Tree](EPI_prep/src/binary_trees/16_compute_right_sibling_tree/compute_right_sibling_tree.py)

* [Binary Search Trees](EPI_prep/src/binary_search_trees)
  - [Search Binary Tree](EPI_prep/src/binary_search_trees/0_search_bst/search_bst.py)
  - [Check If Binary Search Tree Satisfies BST Property](EPI_prep/src/binary_search_trees/1_check_if_bst_satisfies_bst_property/is_bst.py)
    - [Check If Binary Search Tree Satisfies BST Property - Solution 2](EPI_prep/src/binary_search_trees/1_check_if_bst_satisfies_bst_property/is_bst_2.py)
  - [Find the First Key Greater Than A Given Value In A BST](EPI_prep/src/binary_search_trees/2_find_first_key_greater_than_a_value_in_bst/find_first_greater_than_k.py)
  - [Find The K Largest Elements In A BST](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_1.py)
    - [Find The K Largest Elements In A BST - Solution 2](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_2.py)
    - [Find The K Largest Elements In A BST - Solution 3](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_3.py)
  - [Compute The LCA In A BST](EPI_prep/src/binary_search_trees/3_k_largest_in_bst/k_largest_1.py)
  - [Reconstruct A BST From Preorder Traversal Data](EPI_prep/src/binary_search_trees/5_reconstruct_bst_from_preorder_traversal_data/reconstruct_bst.py)
  - [Find The Closest Entries In Three Sorted Arrays](EPI_prep/src/binary_search_trees/6_closest_entries_in_3_sorted_arrays/close_entries.py)
    - [Reconstruct A BST From Postorder Traversal Data](EPI_prep/src/binary_search_trees/5.1_reconstruct_bst_from_post_order_traversal_data/reconstruct_bst.py) 
  - [Reconstruct A BST From Inorder Traversal Data](EPI_prep/src/binary_search_trees/5.2_reconstruct_bst_from_inorder_traversal_data/reconstruct_bst.py) 
  - [Enumerate Numbers Of The Form a + b sqrt2](EPI_prep/src/binary_search_trees/7_enumerate_numbers_of_the_form_a+b_sqrt2/enumerate_numbers_1.py)
    - [Enumerate Numbers Of The Form a + b sqrt2 - Solution 2](EPI_prep/src/binary_search_trees/7_enumerate_numbers_of_the_form_a+b_sqrt2/enumerate_numbers.py)
  - [Build A Minimum Height BST From A Sorted Array](EPI_prep/src/binary_search_trees/8_build_minimum_height_bst/min_height_bst.py)
    - [Build A Minimum Height BST From A Sorted Array - Solution 2](EPI_prep/src/binary_search_trees/8_build_minimum_height_bst/min_height_bst_2.py)
  - [Test If Three BST Nodes Are Totally Ordered](EPI_prep/src/binary_search_trees/9_ordered_bst_nodes/is_bst_ordered.py)
  - [The Range Lookup Problem](EPI_prep/src/binary_search_trees/10_range_look_up_problem/range_lookup.py)
  - [Add Credits](EPI_prep/src/binary_search_trees/11_add_credits/add_credits.py)

* [Heaps](EPI_prep/src/heaps)
  - [Merge Sorted Arrays](EPI_prep/src/heaps/1_merge_sorted_arrays/merge_sorted_arrays.py)
  - [Sort An Increasing Decreasing Array](EPI_prep/src/heaps/2_sort_increasing_decreasing_array/sort_k_inc_dec_array.py)
  - [Sort An Almost Sorted Array](EPI_prep/src/heaps/3_sort_almost_sorted_array/sort_approximately_sorted_array.py)
  - [Compute the K closest Stars](EPI_prep/src/heaps/4_compute_k_closest_stars/k_closest_stars.py)
  - [Compute Median From A Stream](EPI_prep/src/heaps/5_compute_median_from_a_stream/compute_median.py)
  - [K Largest Elements In A Max Heap](EPI_prep/src/heaps/6_k_largest_elements_in_a_heap/k_largest_elements.py)
      - [K Largest Elements In A Max Heap - Solution 2](EPI_prep/src/heaps/6_k_largest_elements_in_a_heap/k_largest_elements_1.py)


* [Linkedlist](EPI_prep/src/linkedlist)
  - [Merge Two Sorted Lists](EPI_prep/src/linkedlist/1_merge_two_sorted_lists/merge_two_list.py)
  - [Merge Two Sorted Doubly LinkedList](EPI_prep/src/linkedlist/1.1_merge_two_sorted_doubly_linkedlist/merge_list.py)
  - [Reverse A Sublist](EPI_prep/src/linkedlist/2_reverse_a_single_sublist/reverse_sublist_1.py)
    - [Reverse A Sublist - Solution 2](EPI_prep/src/linkedlist/2_reverse_a_single_sublist/reverse_sublist_2.py)
    - [Reverse A Singly LinkedList](EPI_prep/src/linkedlist/2.1_reverse_singly_linkedlist/reverse_singly_linkedlist.py)
  - [Reverse Every K Sublist](EPI_prep/src/linkedlist/2.2_reverse_every_k_sublist/reverse_k_sublist.py)
  - [Test For Cyclicity](EPI_prep/src/linkedlist/3_test_for_cyclicity/has_cycle.py)
  - [Find The Start Of A Cycle In A LInkedList](EPI_prep/src/linkedlist/3.1_start_of_linkedlist_cycle/find_cycle_start_1.py)
    - [Find The Start Of A Cycle In A LInkedList - Solution 2](EPI_prep/src/linkedlist/3.1_start_of_linkedlist_cycle/find_cycle_start_2.py)
  - [Test For Overlapping List - Lists Are Cycle Free](EPI_prep/src/linkedlist/4_test_for_overlapping_lists/has_overlapping_list.py)
  - [Test For Overlapping List - Lists May Have Cycles](EPI_prep/src/linkedlist/4_test_for_overlapping_lists/has_overlapping_list.py)
  - [Delete Node From Singly Linkedlist](EPI_prep/src/linkedlist/6_delete_node_from_singly_linkedlist/delete_node.py)
  - [Remove Kth Last Element From List](EPI_prep/src/linkedlist/7_remove_kth_last_element_from_list/remove_kth_last_element.py)
  - [Remove Duplicates From Sorted Lists](EPI_prep/src/linkedlist/8_remove_duplicates_from_sorted_list/remove_duplicates.py)
  - [Implement Cyclic Right Shift For Singly LinkedList](EPI_prep/src/linkedlist/9_cyclic_right_shift_of_singly_linkedlist/cyclic_right_shift_list.py)
  - [Even Odd Merge](EPI_prep/src/linkedlist/10_even_odd_merge/even_odd_merge.py)
  - [Test If Singly LinkedList Is Palindromic](EPI_prep/src/linkedlist/11_palindromic_linkedlist/is_palindrome.py)
  - [Implement List Pivoting](EPI_prep/src/linkedlist/12_implement_list_pivoting/list_pivoting.py)
  - [Add Two LinkedLists](EPI_prep/src/linkedlist/13_add_two_linkedlists/add_lists.py)



<br>
<br>


## Blind 75 Questions

* [Two Sum](blind_75/src/two_sum)
* [Best Time To Buy And Sell Stock](blind_75/src/arrays/buy_and_sell_stock)
* [Contains Duplicate](blind_75/src/arrays/contains_duplicate)
* [Product of Array Except Self](blind_75/src/arrays/product_of_array_except_self)
* [Maximum Subarray](blind_75/src/arrays/maximum_subarray)



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

<br>
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


