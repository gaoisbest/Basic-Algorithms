# Order statistics
Given an array, find the `n`th smallest element (element of rank `k`).

# Solution
- Sorting
If we first sort, using merge sort or heap sort, the problem can be solved in `O(nlgn)`.

- Rand-select
Our goal is find median in linear time.
Median is useful in divide and conquer technology.
Randomized divide and conquer: rand-select

- Worst-case linear-time order statistics
    - Idea: generate good pivot recursively
    - Useful code for finding the median
