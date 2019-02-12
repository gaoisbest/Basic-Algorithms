# 1. Introduction
Python implementation of basic algorithms in [Introduction to Algorithms](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/) class. Here is the [video 1](https://open.163.com/movie/2010/12/G/F/M6UTT5U0I_M6V2T1JGF.html) and [video 2](https://www.bilibili.com/video/av8481187).

# 2. Data structure
- **2.1 Stack**
    - **FILO**: elements are added from the front and removed from the front
    - Applications
        - [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/), [394. Decode String](https://leetcode.com/problems/decode-string/)
        - Recursive
        - DFS in graph

- [**2.2 Queue**](https://www.pythoncentral.io/use-queue-beginners-guide/)
    - **FIFO**: elements are added from the back and removed from the front
    - Applications
        - BFS in graph

- **2.3 Hash**
    - It is set: unique and non-order
    - (key, value), the key point of Hash is **index of key**
    - Applications
        - Unique `n` numbers with range `[0, m)`
            - Solution 1: Quicksort with time complexity `O(nlogn)` and space complexity `O(1)`
            - Solution 2: Countsort with time complexity `O(n + m)` and space complexity `O(m)`
            - Solution 3: hash
                - Mod operation
        - [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
                
- [**2.4 Tree**](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Tree/README.md)
    - Useful for **dynamic set**(i.e., insert or delete element) query
    - Applications
        - [144. Binary Tree Preorder Traversal - non recursive](https://leetcode.com/problems/binary-tree-preorder-traversal/)
        - [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)
        - [106. Construct Binary Tree from Inorder and Postorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)
        
- [**2.5 Heap**](https://towardsdatascience.com/data-structure-heap-23d4c78a6962)
    - It is always **complete** binary tree: root `i`, left `2*i`, right `2*i+1`
    - Applications
        - [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
        - [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
    
   
# 3. Algorithm

## 3.1 Algorithm attributes
- Finite (有穷性)
- Determinate (确定性)
- Feasible (可行性)
- Input & output

## 3.2 Algorithm complexity
- Time
    - Basic operation times
    - `O(nlgn)`
        - Expectation time of quicksort
        - Lower-bound of comparison-based sorting algorithms
- Space
    - Memory usage
- Difference
    - Space can be reused
    - Time and space can be interchanged (e.g. Hash)
- `O(1) < O(lgn) < O(n^(1/2)) < O(n) < O(nlgn) < O(n^2) < O(n^3) < O(2^n) < O(n!)`

## 3.3 Algorithm design technique
- 3.3.1 Exhaustive (穷举法)
    - N-queen
    - N permutation
- [3.3.2 Divide and Conquer](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Divide_and_Conquer/README.md)
    - Binary search
    - MergeSort
- [3.3.3 Dynamic Programming](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Dynamic_Programming/README.md)
    - Principle
        - **Cache**: 1d array, 2d matrix, 3d tensor, map
        - **bottom-up**
    - Scenario
        - [1] **Most**: big (最大), small (最小), long (最长), optimum (最优), counting (计数)
        - [2] **Recursive formula**: f(n) = F(n-1)
    - Applications
        - [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
        - [198. House Robber](https://leetcode.com/problems/house-robber/) **0/1 knapsack** without conditions
        - [416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/), [**0/1 knapsack**](https://www.cnblogs.com/Christal-R/p/Dynamic_programming.html)
        - [72. Edit Distance](https://leetcode.com/problems/edit-distance/)
        - [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/), **counting**
        - [322. Coin Change](https://leetcode.com/problems/coin-change/)
        
- 3.3.4 Greedy
    - Dijkstra
    - Prim
    - Kruskal

# 4. Lectures
- [Lecture 1](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-01.md): **introduction, analysis of algorithms, insertion sort, merge sort**.
- [Lecutre 2](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-02.md): **asymptotic notation, solving recurrences: substitution, recurrsion tree, master**.
- [Lecutre 3](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-03.md): **divide and conquer, binary search, merge sort, x to the power of n, matrix multiplication of Fibonacci numbers, Strassen matrix multiplication**.
- [Lecutre 4](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-04.md): **quick sort, randomized quick sort**.
- [Lecutre 5](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-05.md): **comparison sorting, decision tree model, sort in linear time: couting sort, radix sort, stable sorting algorithm**
- [Lecutre 6](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-06.md): **find the k-th element: quick select, worst-case linear-time order statistics**
- [Lecutre 7](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-07.md): **Hash, hash function, load factor, collision: chaining, open addressing**
- [Lecutre 8](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-08.md): **universal hashing**
- [Lecutre 9](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-09.md): **binary search tree, bst sort, Jensen's equality, convex, expected random build bst height is O(lgn)**
- [Lecutre 10](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-10.md): **red-black tree, rb-insert, rotation**
- [Lecutre 11](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-11.md): **dynamic order statistics, data structure augmentation, interval tree**
- [Lecutre 12](https://github.com/gaoisbest/Basic-Algorithms/blob/master/lectures/Lecture-12.md): **dynamic programming two hallmarks, longest common subsequence**
- Lecutre 13
- Lecutre 14
- Lecutre 15
- Lecutre 16
- Lecutre 17
- Lecutre 18
- Lecutre 19
- Lecutre 20
- Lecutre 21
- Lecutre 22
