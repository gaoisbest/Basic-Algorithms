
# Algorithm list
- [Binary Search Tree](https://github.com/gaoisbest/Basic-Algorithms/blob/master/Tree/Binary_Search_Tree.py)
    - BST sort, `O(nlogn)`
    - Three scenarios of node deletion
        - The node does not have children. Delete it directly.
        - The node has one child. Promote the child.
        - The node has two children. Promote leftmost child in the right subtree.
- Red-Black Tree by [others](https://github.com/stanislavkozlovski/Red-Black-Tree/blob/master/rb_tree.py)
    - **Balanced** search tree, quick for **searching `O(logn)`**
    - **Four properties**
        - Every node is red or black
        - The root and leaves are black
        - If a node is red, then its parent is black
        - All simple paths from any node `x` to a descendant leaf have the same number of black nodes = `black-height(x)`
- Interval Tree by [others](https://github.com/chaimleib/intervaltree)
    - Has `[low, high]` interval
    - **Augmented red-black tree** with `log(n)`
