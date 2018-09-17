# How fast can we sort?

## Comparison sorting
- O(n^2): when swap adjacent elements is allowed.
- Heapsort, Quick sort, Merge sort, Insertion sort. All of the above models compare two elements, which is called comparison sorting.
- The lower bound is O(nlgn) for comparison sorting.

## Decision-tree model
- The above four sorting model can be converted to decision-tree model.
- The number of leaves is all permutation of the array, the order is O(n!)
- Theorem: any decision tree sorting n elements has height Ω(nlgn).
    - Stirling’s formula is an approximation for factorials.


## Sorting in linear time
Assume the number has a range.

### Counting sort
- Assumptions: 
    - The number is integers
    - The range of the integers is pretty small
- c[I]: count the occurrence of value
- Distribution step
- O(k+n), if k=O(n), the counting sort is linear time, if k=O(nlgn), then we can use merge sort instead.

## Stable sort preserves the relative order of the elements.
Stable sorting algorithms:
- Counting  sort
- 

## Radix sort
- Sort a much larger range of numbers in linear time
- Digit by digit sort
- Sort by the least significant digit.


