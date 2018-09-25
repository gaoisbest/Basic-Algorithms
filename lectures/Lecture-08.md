# Weakness of hashing
For any choice of hash function, there exists bad set of keys that all hash to same slot.

# Universal hashing

Choose h randomly from Hashing set H, suppose we are hashing n keys into m slots in table T, then for given key x, the expected number of collisions with x is less than n/m.
