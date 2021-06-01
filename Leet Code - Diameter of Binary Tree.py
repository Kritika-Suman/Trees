class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def helper(root):
            if root:
                if not root.right and not root.left:
                    return 1
                return 1 + max(helper(root.left), helper(root.right))
            return 0
        if root:
            return max(helper(root.left) + helper(root.right), self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return 0
