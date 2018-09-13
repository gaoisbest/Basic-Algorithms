# Analysis of Algorithms
The theoretical study of computer program **performance** and resource usage.  
Algorithm just like money. If you have money, you can buy other things. Algorithm supports user-friendly, performance, etc.

# Running time
- Depends on input (e.g., inverse sorted is the worst case)
- Depends on input size
- Want upper bound

# Kinds of analysis
- Worst-case (usually) 
    - T(n) = max time on any input size n
- Average-case (sometime) 
    - T(n) = expected time over all input size n
- Best-case (bogus)

# Asymptotic analysis
Look at growth of T(n) as n->∞
- Drop low order terms
- Ignore leading constants

# Sorting
Permutation is rearrangement of the numbers.

## Insertion sort
- Worst case: input reverse sorted

## Merge sort
- Merge operation: linear time (O(n))
- Recursion tree
    - T(n) = 2T(n/2) + O(n)
    - Tree depth: lgn
    - Tree leaves: n
    - nlgn

