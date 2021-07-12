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

## Interview Questions

Below is a list of interview questions. Will keep on adding as I encounter them

`E` - Easy, `M` - Medium, `H` - Hard, `VH` - Very Hard

### Questions by Topic

* **Recursion & Dynamic Programming**
  * `E` [Capitalize First](src/interview_questions/recursionAndDynamicProgramming/easy/capitalizeFirst.py) - Given an array of words write a recursive function to capitalize the first letter of every word in the array.
  * `E` [Collect Strings](src/interview_questions/recursionAndDynamicProgramming/easy/collectStrings.py) - Write a function that accepts objects and returns an array of all the values in the object that have a typeof string.
  * `E` [Decimal to Binary](src/interview_questions/recursionAndDynamicProgramming/easy/decToBinary.py) - Write a recursive function that converts a decimal number to binary.
  * `E` [Factorial](src/interview_questions/recursionAndDynamicProgramming/easy/factorial.py) - Write a recursive function that computes the factorial of a given number
  * `E` [Fibonacci](src/interview_questions/recursionAndDynamicProgramming/easy/fibonacci.py) - Given a  value 'n' Write a recursive function to compute the fibonacci number at position 'n' 
  * `E` [Flatten](src/interview_questions/recursionAndDynamicProgramming/easy/flatten.py) - write a recursion function called flatten which accepts an array of arrays and returns a new array with all the values flattened.
  * `E` [Greatest Common Divisor](src/interview_questions/recursionAndDynamicProgramming/easy/greatestCommonDivisor.py) - Write a recursive function that computes the greatest common divisor of number.
  * `E` [isPalindrome](src/interview_questions/recursionAndDynamicProgramming/easy/isPalindrome.py) - Write a recursive function if the string passed to is a palindrome, otherwise return false.
  * `E` [nestedEvenSum](src/interview_questions/recursionAndDynamicProgramming/easy/nestedEvenSum.py) - Write a recursive function to return the sum of all even numbers in an object which may contain nested objects.
  * `E` [Power of Number](src/interview_questions/recursionAndDynamicProgramming/easy/powerOfNumber.py) - Write a recursive function that computes the power of a number
  * `E` [Product of Array](src/interview_questions/recursionAndDynamicProgramming/easy/productOfArray.py) - Write a recursive function that takes an array of numbers and returns a product of all the elements
  * `E` [Recursive Range](src/interview_questions/recursionAndDynamicProgramming/easy/recursiveRange.py) - Write a recursive function that accepts a number and adds all the number from 0 to the number passed
  * `E` [Reverse](src/interview_questions/recursionAndDynamicProgramming/easy/reverse.py) -  Write a recursive function that accepts a string and returns a new string in reverse
  * `E` [Some Recursive](src/interview_questions/recursionAndDynamicProgramming/easy/someRecursive.py) - Write a recursive function which accepts an array and a callback. The function returns true if a single value in the array returns true when passed to the callback, otherwise it returns false
  * `E` [Stringify Numbers](src/interview_questions/recursionAndDynamicProgramming/easy/stringifyNumbers.py) - Write a function that takes in an object and finds all the values which are numbers and converts them to strings. 
  * `E` [Sum of digits](src/interview_questions/recursionAndDynamicProgramming/easy/sumOfDigits.py) - Write a function that sums up a number recursively
  * `H` [Magic Index](src/interview_questions/recursionAndDynamicProgramming/hard/magicIndex.py) - A magic index in an array A[ 1.•.n-1] is defined to be an index such that A[ i] = i. 
  Given a sorted array of distinct integers, write a method to find a magic index, if one exists, in array A.
  * `H` [PowerSet](src/interview_questions/recursionAndDynamicProgramming/hard/powerset.py) - Write a method to return all subsets of a set.
  * `H` [Recursive Multiply](src/interview_questions/recursionAndDynamicProgramming/hard/recursiveMultiply.py) - Write a recursive function to multiply two positive integers without using the * operator (or / operator). 
  * `H` [Robot In A Grid](src/interview_questions/recursionAndDynamicProgramming/hard/robot_in_a_grid.py) - Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
  * `H` [Triple Step](src/interview_questions/recursionAndDynamicProgramming/hard/tripleStep.py) - A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs.
  * `H` [Unique Paths](src/interview_questions/recursionAndDynamicProgramming/hard/uniquePaths.py) - The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
  How many possible unique paths are there?

* **Arrays**
  * `E` [Two Number Sum](src/interview_questions/arrays/easy/twoNumberSum/twoNumberSum.py) - Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
  If any two numbers in the input array sum up to the target sum, the function should return them in an array

* **Stacks**
  * `M` [Min Max Stack](src/interview_questions/stacks/medium/min-max-stack/min_max_stack.py) - Write a MinMaxStack class for a Min Max Stack. The class should support pushing, popping, peeking and Getting both the minimum and the maximum values in the stack at any given point in time. All class methods, when considered independently, should run in constant time and with constant space.

  
### Interview Questions By Company

Here is a list of popular interview questions given asked by Big Companies

**Google**

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


