# My Approach
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def univalTree(root: TreeNode, val: int) -> bool:
            if root is None: return True

            if root.val != val: return False

            if not root.left and not root.right: return True

            return univalTree(root.left, val) and univalTree(root.right, val)

        val = root.val
        return univalTree(root.left, val) and univalTree(root.right, val)

# Litle Better Approach:
class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct
