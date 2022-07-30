# Recursion

Recursion is an approach to problem solving where the solution depends partially on solutions to smaller instances of related problems.

A recursive function consists of base cases and calls to the same function with different arguments. 
Two key ingredients to a successful use of recursion are identifying the base cases, which are to be solved directly, 
and ensuring progress, that is the recursion converges to the solution.

<br>

## Question to ask yourself when solving a recursion question

1. What is the base case ?
i.e. A stopping condition that allows you stop a recursive program or function

2. What is the least amount of work I can do in each Iteration (function call)

<br>

### Pros for using Recursion
1. Bridges the gap between elegance and complexity
2. Reduces the need for complex loops and auxilliary data structures
3. Can reduce time easily with memoization
4. Works really well with recursive data structures like trees & Graphs

<br>

### Cons for using Recursion
1. Slowness due to CPU Overload
2. Can lead to out of memory errors / Stack overflow exceptions
3. Can be unnecessarily complex if poorly constructed



## Questions

In this section we will solve common recursion questions that will help you understand the basics of recursion

* [Recursion With Strings](src/1_recursion_with_strings)
    * [Reverse String](src/1_recursion_with_strings/1_reverse_string.py)
    * [Palindrome](src/1_recursion_with_strings/2_palindrome.py)
* [Recursion With Numbers](src/2_recursion_with_numbers)
    * [Decimal To Binary](src/2_recursion_with_numbers/1_decimal_to_binary.py)
    * [Sum Of Natural Numbers](src/2_recursion_with_numbers/2_sum_of_natural_numbers.py)
* [Divide & Conquer](src/3_divide_and_conquer)
    * [Fibonacci](src/3_divide_and_conquer/1_fibonacci.py)
    * [Binary Search](src/3_divide_and_conquer/2_binary_search.py)
    * [Merge Sort 1](src/3_divide_and_conquer/3_merge_sort_2.py)
    * [Merge Sort 2](src/3_divide_and_conquer/3_merge_sort.py)
    * [Reverse Linkedlist](src/3_divide_and_conquer/4_reverse_linkedlist.py)
    * [Merge Two Sorted List](src/3_divide_and_conquer/5_merge_two_sorted_list.py)
    * [Insert Into Binary Search Tree](src/3_divide_and_conquer/6_insert_into_binary_search_tree.py)
    * [Get Leaf Nodes](src/3_divide_and_conquer/7_get_leaf_nodes.py)
    * [Depth First Search](src/3_divide_and_conquer/8_depth_first_search.py)



### References

[▶ Recursion in Programming - Full Course](https://www.youtube.com/watch?v=IJDJ0kBx2LM)