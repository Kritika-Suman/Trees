# Did it myself, got it accepeted in first attempt

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def depth(root: TreeNode, maxDepth: int) -> int:
            if root is None: return 0
            maxDepth += 1
            if not root.left and not root.right: return maxDepth
            return max(depth(root.left, maxDepth), depth(root.right, maxDepth))

        return depth(root, 0)
