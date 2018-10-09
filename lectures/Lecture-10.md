# Balanced Search Tree
Insert, delete and query operations is O(lgn)
- AVL
- 2-3 tree
- 2-3-4 tree
    - Every internal node has 2, 3, or 4 children
    - Every leaf has same depth (i.e., black-height(root)), i.e., all leaves are in the same level
- B-tree
- Red-black tree

# Red­Black Tree
## Definition
It is a binary search tree with extra color field for each node, satisfying red-black properties:
- 1. Every node is either red or black
- 2. The root and leaves (nil’s) are black
- 3. Every red node has black parent
- 4. All simple paths from a node x to a descendant leaf of x have same number of black nodes = `black-height(x)` (does not count x itself)

## Tree update (i.e., insert and delete)
- BST operation
- Color changes
- Restructuring of links via rotations
    - Right-rotate
    - Left-rotate
    - O(1)

### RB-Insert
- Always red color to preserve property 4
    - If the parent’s color is red, then recoloring or rotation

