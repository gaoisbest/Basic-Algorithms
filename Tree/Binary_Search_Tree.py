"""
Binary Search Tree

Time complexity
- Tree insert time
    - Good: O(nlgn)
        - O(lgn) for one insertion; O(nlgn) for n insertion.
    - Bad: O(n^2)
        - When the array is sorted. O(n) for one insertion; O(n^2) for n insertion.
- Tree Walk time: O(n)

BST sort vs quicksort
- BST sort and quick sort make same comparison but in a different order.

Randomized BST
- Randomly permute array A
- BST sort(A)
- Equal to randomized quick sort, O(nlgn)

Theorem
- Expectation of height of random build BST is O(lgn).
"""


class Node:
    """
    Node class, includes value, left and right child.
    """
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    """
    Binary Search Tree class.
    """
    def __init__(self):
        self.root = None

    def _insert(self, node, val):
        if val < node.val:
            # first determine if left child is None
            if node.left is None:
                node.left = Node(val)
            else:
                self._insert(node.left, val)
        elif val > node.val:
            # first determine if right child is None
            if node.right is None:
                node.right = Node(val)
            else:
                self._insert(node.right, val)
        else:
            # omit the equal one
            print('Duplicate value: %s' % str(val))

    def insert(self, val):
        """Insert new node"""
        # first determine if root is None
        if self.root is None:
            self.root = Node(val)
        else:
            self._insert(self.root, val)

    def _find_leftmost(self, node_par, node):
        """Find left most node"""
        if node.left is not None:
            return self._find_leftmost(node, node.left)
        else:
            return node_par, node

    def _delete(self, node, val):
        if node.val == val:
            if (node.left is not None) and (node.right is not None):
                # leftmost child in the right subtree
                leftmost_par, left_most = self._find_leftmost(node, node.right)
                # remove leftmost node
                # left_most only has right children
                if leftmost_par.left == left_most:
                    leftmost_par.left = left_most.right
                else:
                    leftmost_par.right = left_most.right

                # remove node
                left_most.left = node.left
                left_most.right = node.right

                return left_most
            elif node.left is not None:
                # promote left node
                return node.left
            elif node.right is not None:
                # promote right node
                return node.right
            else:
                # the node has no children
                return None
        elif val < node.val:
            if node.left is not None:
                # new left node
                node.left = self._delete(node.left, val)
        elif val > node.val:
            if node.right is not None:
                # new right node
                node.right = self._delete(node.right, val)
        return node

    def delete(self, val):
        """
        Delete node
        - 1. The node to remove has no child
            - delete it directly
        - 2. The node to remove has 1 child (left or right)
            - the child node can just be promoted
        - 3. The node to remove has 2 children
            - leftmost child in the right subtree, which has 0 or 1 right children
            - rightmost child in the left subtree, which has 0 or 1 left children
        """
        if self.root is not None:
            self.root = self._delete(self.root, val)

    def _search(self, node, val):
        if val == node.val:
            return True
        # two conditions here
        elif (val < node.val) and (node.left is not None):
            return self._search(node.left, val)
        elif (val > node.val) and (node.right is not None):
            return self._search(node.right, val)
        else:
            return False

    def search(self, val):
        """If success search, return True"""
        if self.root is not None:
            return self._search(self.root, val)
        else:
            return False

    def _height(self, node, height):
        if node is None:
            return height
        else:
            left_height = self._height(node.left, height+1)
            right_height = self._height(node.right, height+1)
            return max(left_height, right_height)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _in_order(self, node):
        # if clause is necessary here
        if node is not None:
            self._in_order(node.left)
            print(node.val)
            self._in_order(node.right)

    def in_order(self):
        """In-order traverse"""
        if self.root is not None:
            self._in_order(self.root)


if __name__ == '__main__':
    print('Build tree...')
    tree = Tree()
    tree.insert(7)
    tree.insert(3)
    tree.insert(10)
    tree.insert(8)
    tree.insert(12)
    tree.insert(15)
    tree.insert(-10)
    '''
         7
        / \
       3  10
      /  /  \
   -10  8   12
             \
             15
    '''
    print('In-order traverse: ')
    tree.in_order()
    print('Delete node: ')
    tree.delete(7)
    tree.in_order()

    print('Search tree: ', tree.search(10))
    print('Tree height: %d' % tree.height())