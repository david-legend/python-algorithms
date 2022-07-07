# Python Algorithms and Data Structures

This repository contains implementations of popular data structures and interview questions implemented in Python.

Each data structure has its own separate README
with related explanations and links for further reading (including ones
to YouTube videos).


The explanations of the data structures are from <a href="https://github.com/trekhleb/javascript-algorithms"> Oleksii Trekhleb's Project</a>

*This project is meant to help you on your job interview journey. I will be updating it as I embark on my own journey*

<br>

## Data Structures

A data structure is a particular way of organizing and storing data in a computer so that it can
be accessed and modified efficiently. More precisely, a data structure is a collection of data
values, the relationships among them, and the functions or operations that can be applied to
the data.

`B` - Beginner, `A` - Advanced

* `B` [Linked List](src/data-structures/linked-list)
* `B` [Circular Linked List](src/data-structures/circular-linked-list/circular_linked_list.py)
* `B` [Doubly Linked List](src/data-structures/doubly-linked-list)
* `B` [Circular Doubly Linked List](src/data-structures/circular-doubly-linked-list/circular_doubly_linked_list.py)
* `B` [Queue](src/data-structures/queue)
* `B` [Stack](src/data-structures/stack)
* `A` [Heap](src/data-structures/heap)
* `A` [Tree](src/data-structures/tree)
  * `A` [Binary Tree](src/data-structures/tree/binary-tree)
  * `A` [Binary Search Tree](src/data-structures/tree/binary-search-tree)
  * `A` [AVL Tree](src/data-structures/tree/avl-tree)


## Patterns For Coding Interviews

This section categorizes coding interview problems into a set of 16 patterns. 
Under each pattern there will be a specific category of problems to solve. 
The goal is to develop an understanding of the underlying pattern, so that, we can apply that pattern to solve other problems.


* [Sliding Window](src/patterns/1_sliding_window)
* [Two Pointers](src/patterns/2_two_pointers)
* [Fast & Slow Pointers](src/patterns/3_fast_and_slow_pointers)
* [Merge Intervals](src/patterns/4_merge_intervals)
* [Cyclic Sort](src/patterns/5_cyclic_sort)
* [In-Place Reversal of Linkedlist](src/patterns/6_in_place_reversal_of_linkedlist)
* [Breath First Search](src/patterns/7_tree_breath_first_search)
* [Depth First Search](src/patterns/8_tree_depth_first_search)
* [Two Heaps](src/patterns/9_two_heaps)
* [Subsets](src/patterns/10_subsets)
* [Modified Binary Search](src/patterns/11_modified_binary_search)
* [Top K Elements](src/patterns/12_top_k_elements)
* [K Way Merge](src/patterns/13_k_way_merge)
* [Topological Sort](src/patterns/14_topological_sort)
* [Dynamic Programming Patterns](src/patterns/15_dynamic_programming)


## Blind 75 Questions

* [Two Sum](src/blind_75/two_sum)
* [Best Time To Buy And Sell Stock](src/blind_75/arrays/buy_and_sell_stock)
* [Contains Duplicate](src/blind_75/arrays/contains_duplicate)
* [Product of Array Except Self](src/blind_75/arrays/product_of_array_except_self)
* [Maximum Subarray](src/blind_75/arrays/maximum_subarray)


## Elements Of Programming Interviews Prep

EPI is an invaluable book  textbook presents a comprehensive introduction to modern competitive programming.
Below are solutions & questions found under various topics in the book.

[LinkedList](src/EPI_prep/linkedlist)
[Recursion](src/EPI_prep/recursion)


## Useful Information

### References

[▶ Data Structures and Algorithms on YouTube](https://www.youtube.com/playlist?list=PLLXdhg_r2hKA7DPDsunoDZ-Z769jWn4R8)

### Big O Notation

*Big O notation* is used to classify algorithms according to how their running time or space requirements grow as the input size grows.
On the chart below you may find most common orders of growth of algorithms specified in Big O notation.

![Big O graphs](./assets/big-o-graph.png)

Source: [Big O Cheat Sheet](http://bigocheatsheet.com/).

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


