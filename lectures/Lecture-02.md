# Asymptotic notation
## Smaller than or equal to
`f(n) = O(g(n))` means there are constants `C>0, n_0>0`, such that `0 <= f(n) <= Cg(n)` for all `n>=n_0`. Ex. `2n^2 = O(n^3)`.  
Set definition: `O(g(n))` is a set. `n>=n_0` means `n` is sufficient large.

## Greater than or equal to
`f(n) = Ω(g(n))` means there are constants `C>0, n_0>0`, such that `0 <= Cg(n) <= f(n)` for all `n>=n_0`. Ex. `n^(1/2) = Ω(lgn)`

## Equal to
`θ(g(n)) = O(g(n)) join Ω(g(n)`. Ex. `n^2 = θ(n^2)`

# Solving recurrences
- Substitution method
    - Guess the form of the solution
    - Verify by induction
    - Solve for constants
    - Example: `T(n) = 4T(n/2) + n`
- Recursion-tree method
    - Example: `T(n) = T(n/4) + T(n/2) + n^2`
    - **Summation at each level**, find the pattern at each level, such as arithmetical series or geometrical series.
    - 1 + 1/2 + 1/4 + 1/8 + … = 2
- Master method
    - Very easy to use, can be viewed as an application of recursion tree.
    - Only applies to a particular family of recurrences.
    - `T(n) = aT(n/b) + f(n)`: a sub problems and each size is `n/b`.
    - `a >= 1, b > 1`, `f(n)` is asymptotic positive (when `n>n_0`, `f(n)` is positive)
    - Three cases about `f(n)` and `n^(logb_a)`
    - `n^(logb_a)` is number of leaves in recursion tree

