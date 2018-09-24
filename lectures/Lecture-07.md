# Hashing

# Symbol-table problem
- Direct access table
- Hashing
    - Hash function `h` maps key `s` randomly into slots of table `T`
    - Collision
        - **Chaining**: link records in the same slot into list
        - **Open addressing**
            - Linear probing
            - Double hashing
                - The expected number of probes is `1/(1-load factor)`. This mean we do not want the hash table is too full.
    - **Load factor** of a hash table with `n` keys and `m` slots is `alpha=n/m`, which is average number of keys per slot (i.e., average length of chain).

**A hash table runs in constant search time is WRONG**! It depends the load factor.

# Hash function
- Division method
- Multiplication method
- Dot-product method

