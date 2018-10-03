
# Dynamic programming
- Algorithm design technique, like divide and conquer
- Solve maximize or minimize **optimization** problem
- DP = “careful brute force”, reduce exponential time to polynomial time
- DP = subproblems + reuse, subproblems is the first thing to know
- DP = recursion + memorization
- DP = shortest paths in some DAG
- Memorization DP algorithms
- Bottom-up DP algorithm
    - Topological sort of subproblem dependency DAG
    - Can save space

# DP hallmarks
- Optimal substructure
- Overlapping subproblems
    - Memorization with recursion
    - Bottom-up
        - Compute the table bottom-up

# 5 easy steps to DP
- Define subproblems
- guess (part of solution)
- Relate subproblem solution 
- Recurse & memorize or build DP table bottom-up
- Solve original problem

# Fibonacci numbers
- DP = recursion + memorization
- Memorization DP algorithms
    - fib(k) only recurses the first time 
    - Time = number of subproblems * time per subproblem, here is n * O(1) = O(n)
- Bottom-up DP algorithm
    - Topological sort of subproblem dependency DAG
    - Can save space


# Longest common subsequence (LCS) problem
- Brute force
    - How many subsequence of length m sequence
        - 2^m
    - What is the cost of checking each subsequence in sequence y (length of n) ?
        - O(n)
    - Total time: O(n * 2^m)
- Bottom-up DP
    - Compute C[i, j] from bottom to up
    - Construct LCS by tracing backwards


