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

## Blind 75 Questions

* [Two Sum](blind_75/src/two_sum)
* [Best Time To Buy And Sell Stock](blind_75/src/arrays/buy_and_sell_stock)
* [Contains Duplicate](blind_75/src/arrays/contains_duplicate)
* [Product of Array Except Self](blind_75/src/arrays/product_of_array_except_self)
* [Maximum Subarray](blind_75/src/arrays/maximum_subarray)



<br>
<br>

## Elements Of Programming Interviews Prep

EPI is an invaluable book  textbook presents a comprehensive introduction to modern competitive programming.
Below are solutions & questions found under various topics in the book.

* [Recursion](EPI_prep/src/recursion)
* [Binary Trees](EPI_prep/src/binary_trees)
* [Binary Search Trees](EPI_prep/src/binary_search_trees)



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


