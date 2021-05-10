# Approach 1: Traverse the tree in in-oreder way and store the values in a list and
# then construct a right-skewed tree from that.

# Approach 2:
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        temp = curr = TreeNode(-1)
        stack = []

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            curr.right = stack.pop()
            curr = curr.right
            curr.left = None
            root = curr.right

        return temp.right
