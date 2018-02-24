# Three steps
- **Divide** the problem into one or more sub-problems.
- **Conquer** each sub-problem recursively.
- **Combine** solutions.

# Algorithm list
- [Merge sort](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Divide_and_Conquer/Merge_sort.py)
  - Principle: **recursive merging** from bottom to up.
  - T(n) = 2T(n/2) + O(n)
  - O(nlgn)
- [Binary search](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Divide_and_Conquer/Binary_search.py)
  - T(n) = T(n/2) + O(1)
  - O(lgn)
- [X to the power of n](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Divide_and_Conquer/X_power_n.py)
  - T(n) = T(n/2) + O(1)
  - O(lgn)
- Quick sort
  - Sort in place, no extra space. Like insertion sort.
  - Principle: **recursive partitioning** from up to bottom.
  - Worst-case (i.e., reversed sorted) time complexity: O(n^2), T(n) = T(0) + T(n-1) + cn
