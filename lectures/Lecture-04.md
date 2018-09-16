# Quicksort
- Divide and conquer
- Sort **‘in place’**, just like **insertion sort**. Merge sort need extra space to do the merge operation.
- Very practical
- Key step: partition

# Analysis
- Worst-case
    - Already sorted or inverse sorted
    - One side of partition has no element
    - T(n) = T(n-1) + T(0) + O(n)
    - O(n^2), arithmetic series
- Best-case
    - Partition at the middle
    - T(n) = 2T(n/2) +O(n)
    - O(nlgn)
- Case
    - T(n) = T(n * 1/10) + T(n * 9/10) + O(n)
    - Same as best-case

# Randomnized quicksort
- Randomnized quicksort is independent of input order.
- No assumption about input distribution.
- Worst-case determined only by random number generator
- Indicator random variable, 0 or 1

