# Binary Search Tree

## Tree sort
- Sort: In-order tree walk
    - Walk time: `O(n)`
- Tree insert time:
    - Good: `O(nlgn)`. `O(lgn)` for one insertion; `O(nlgn)` for `n` insertion. 
    - Bad: `O(n^2)` when the array is sorted. `O(n)` for one insertion; `O(n^2)` for `n` insertion. 

## Relation to quick sort
BST sort and quick sort make same comparison but in a different order.


## Randomized BST
- Randomly permute array A
- BST sort(A)
- Equal to randomized quick sort, `O(nlgn)`

## Theorem 
**Expectation of height of random build BST is O(lgn).**

## Jensen’s equality
`f(E(x)) <= E(f(x))` for convex function `f`.

In geometry, if you have two points `p` and `q`, and the line determined by them is `alpha * p + beta * q`, where `alpha + beta = 1`. If `alpha >=0` and `beta >=0`, then the line is a segmentation between `p` and `q`.

## Convex definition
`f(alpha*x + beta*y) <= alpha*f(x) + beta*f(y)` for all `alpha >=0, beta >=0` and `alpha + beta = 1`.
